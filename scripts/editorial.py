"""Apply model-read, source-bound question editions. Never use OCR as prose."""
import copy
import json
import re
import pymupdf as fitz


def clean_title(title):
    title = re.sub(r'[（(][^（）()]*?(?:第三方|转载|公开预览|重排图|非完整|非官方)[^（）()]*[）)]', '', title)
    title = title.replace('完整试题及第三方解析', '试题与解答')
    return re.sub(r'\s+', ' ', title.replace('_', ' ')).strip()


def edition_questions(root, resources, questions, render=True):
    """Return edited copies and language aliases; preserve archival master records."""
    rmap = {r['id']: r for r in resources}
    questions = copy.deepcopy(questions)
    for path in sorted((root/'catalog/editorial').glob('*.json')):
        edition = json.loads(path.read_text())
        resource = rmap[edition['resource_id']]
        if edition['source_sha256'] != resource.get('sha256'):
            raise ValueError(f'Editorial source changed: {path.name}')
        if edition.get('read_method') != 'model-visual':
            raise ValueError(f'Expected visual reading provenance: {path.name}')
        previous = {q['number']: q for q in questions if q['resource_id'] == resource['id']}
        if edition.get('replace_questions'):
            questions = [q for q in questions if q['resource_id'] != resource['id']]
        for item in edition['questions']:
            if not item.get('body_zh') or not item.get('tags') or '待标注' in item['tags']:
                raise ValueError(f'Incomplete editorial question: {path.name} #{item["number"]}')
            qid = resource['id'] + '-q' + item['number']
            q = previous.get(item['number'], dict(
                id=qid, resource_id=resource['id'], contest=resource['contest'], year=resource['year'],
                number=item['number'], level='本科' if resource['contest'] in ('CMC','YAU','IMC','PUTNAM') else '高中',
                title=resource['title']+' · '+item['number'], segments=[], solution=None,
                source_sha256=resource['sha256'], authority=resource['authority']))
            q.update({k:v for k,v in item.items() if k not in ('question_regions','solution_regions')})
            q.update(editorial_status='model-visual', tag_status='model-content',
                     crop_status='visual-reviewed', question_unit='problem')
            q.setdefault('segments', [])
            q.pop('solution_note', None)
            q['text'] = item['body_zh']
            for field, regions in [('segments',item.get('question_regions')),('solution',item.get('solution_regions'))]:
                if regions is None: continue
                segments = []
                for i, region in enumerate(regions):
                    rel = f'derived/editorial/{qid}/{field}-{i+1}.png'
                    if render:
                        with fitz.open(root/resource['local_path']) as doc:
                            page = doc[region['page']-1]
                            clip = fitz.Rect(region['bbox'])
                            if clip.is_empty or not clip in page.rect:
                                raise ValueError(f'Invalid editorial crop: {qid}')
                            output = root/rel; output.parent.mkdir(parents=True,exist_ok=True)
                            page.get_pixmap(matrix=fitz.Matrix(2,2),clip=clip,alpha=False).save(output)
                    segments.append(dict(page=region['page'],bbox=region['bbox'],image=rel))
                if field == 'segments': q[field] = segments
                else: q[field] = dict(resource_id=resource['id'],segments=segments,status='visual-reviewed') if segments else None
            if render and not q['segments'] and not item.get('question_regions'):
                raise ValueError(f'No source image for editorial question: {qid}')
            questions = [old for old in questions if old['id'] != qid]
            questions.append(q)
    groups = {}
    for q in questions:
        if q['contest'] == 'EGMO': groups.setdefault((q['year'],q['number']),[]).append(q)
    aliases = {}
    for group in groups.values():
        canonical = next((q for q in group if 'ChineseSimplified' in q['resource_id']), group[0])
        if not canonical.get('solution'):
            paired = next((q for q in group if q.get('solution')), None)
            if paired:
                canonical['solution'] = paired['solution']
        if any(q.get('has_solution') for q in group):
            canonical['has_solution'] = True
        for q in group:
            if q is not canonical: aliases[q['id']] = canonical['id']
    questions = [q for q in questions if q['id'] not in aliases]
    for q in questions:
        q['title'] = clean_title(q['title'])
        if q.get('editorial_status') != 'model-visual': q['tags'] = []
    return questions, aliases
