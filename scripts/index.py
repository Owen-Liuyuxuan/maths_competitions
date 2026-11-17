#!/usr/bin/env python3
"""Index PDFs and render provenance-preserving problem/solution crops.

Automatic coordinates are explicitly candidates, never human-verified. Documents
without reliable headings remain available as full papers and enter review queue.
"""
from __future__ import annotations
import hashlib
import json
import re
from pathlib import Path
import pymupdf as fitz

ROOT = Path(__file__).resolve().parents[1]
OCR = {}


def write(path, data):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


def lines(page):
    result = []
    for b in page.get_text('dict')['blocks']:
        for line in b.get('lines', []):
            text = ''.join(s['text'] for s in line['spans']).strip()
            result.append((text, list(line['bbox'])))
    return result


def source_lines(doc, r, pi):
    cache = OCR.get(r['id'])
    return cache['pages'][pi] if cache else lines(doc[pi])


def subject(text):
    """Conservative keyword suggestions; taxonomy can be overridden per question."""
    rules = {
        '几何': r'triangle|circle|quadrilateral|polygon|perpendicular|三角形|圆心|平面|内切|外接|多边形',
        '数论': r'prime|divisib|integer|modulo|素数|正整数|整除|同余|质数',
        '组合': r'permutation|colou?r|graph|subset|pebbles|tournament|排列|染色|棋盘|机场|组合|子集',
        '代数': r'polynomial|inequal|real numbers|多项式|不等式|实数',
        '线性代数': r'matri[xc]|determinant|eigenvalue|vector space|矩阵|行列式|特征值',
        '分析': r'integral|derivative|continuous|differential|converge|limit|积分|导数|极限|级数|微分',
        '概率统计': r'probability|random|expectation|variance|distribution|概率|随机|统计',
        '几何拓扑': r'manifold|topolog|homolog|homotop|流形|拓扑',
        '应用计算': r'numerical|algorithm|runge|finite element|算法|数值',
    }
    tags = [k for k, v in rules.items() if re.search(v, text, re.I)]
    return tags or ['待标注']


def anchors(doc, r):
    candidates = []
    lo, hi = r.get('page_range', [0, len(doc)])
    for pi in range(lo, hi):
        for text, box in source_lines(doc, r, pi):
            if r['contest']=='CHSMO' and re.search(r'评阅试卷|考生的解答|评卷|阅卷',text):
                continue
            # A problem title must begin a line. Solution variants aren't titles.
            m = re.match(r'^(?:Problem\s*|Question\s*|题目\s*|P(?=\d)|Solutions?\s+(?:to\s+)?Problem\s*)(\d{1,2})\b', text, re.I)
            if m:
                candidates.append(dict(number=m[1], page=pi, y=box[1], x=box[0], text=text))
            elif r['contest'] == 'PUTNAM':
                m = re.match(r'^([AB])\s*([1-6])\s*[.．:]?\s', text)
                if m:
                    candidates.append(dict(number=m[1]+m[2], page=pi, y=box[1], x=box[0], text=text))
            elif r['contest'] in ('CMO', 'CMC', 'CHSMO', 'YAU'):
                m = re.match(r'^(\d{1,2})[.．、]\s*', text)
                if m and box[0] < doc[pi].rect.width * .22:
                    candidates.append(dict(number=m[1], page=pi, y=box[1], x=box[0], text=text))
                elif r['contest']=='CMC' or (r['contest']=='CHSMO' and '加试' in r['title'] and '一试' not in r['title']):
                    m = re.match(r'^([一二三四五六七八九十])[、．.\s]*[（(、．.]', text)
                    if m:
                        number = str('一二三四五六七八九十'.index(m[1])+1)
                        candidates.append(dict(number=number, page=pi, y=box[1], x=box[0], text=text, grouped=r['contest']=='CMC'))
                if r['contest']=='CMO':
                    m=re.match(r'^第\s*([一二三四五六])\s*题',text)
                    if m:
                        candidates.append(dict(number=str('一二三四五六'.index(m[1])+1),page=pi,y=box[1],x=box[0],text=text))
    if r['contest'] == 'EGMO' and r['role'] == 'solutions':
        preferred = [a for a in candidates if re.match(r'^Solutions?\s+(?:to\s+)?Problem', a['text'], re.I)]
        if preferred:
            candidates = preferred
        else:
            # Some years repeat statements before the solutions; retain the last cycle.
            ones = [i for i, a in enumerate(candidates) if a['number'] == '1']
            if len(ones) > 1:
                candidates = candidates[ones[-1]:]
    if r['contest']=='CMC' and any(a.get('grouped') for a in candidates):
        # A fill-in section contains its own 1,2,... numbering; it is not the
        # document's main sequence. Keep explicit section units instead.
        candidates=[a for a in candidates if a.get('grouped')]
    # First strictly ordered cycle rejects subpart numbering and repeated titles.
    selected = []
    for a in candidates:
        if not selected:
            if a['number'] in ('1', '4', '5', '6', 'A1'):
                selected.append(a)
            continue
        prev = selected[-1]['number']
        if prev.startswith(('A', 'B')):
            expect = 'B1' if prev == 'A6' else prev[0] + str(int(prev[1:])+1)
        else:
            expect = str(int(prev)+1)
        if a['number'] == expect:
            selected.append(a)
    if r['contest'] == 'PUTNAM':
        for a in selected:
            a['column'] = int(a['x'] > doc[a['page']].rect.width * .48)
    return selected


def slices(doc, r, points, outdir, terminal=None):
    result = []
    lo, hi = r.get('page_range', [0, len(doc)])
    for i, a in enumerate(points):
        end = points[i+1] if i+1 < len(points) else terminal or dict(page=hi-1, y=doc[hi-1].rect.height-12, column=1)
        boundary = a.get('answer_start')
        if r['role'] == 'combined' and not boundary:
            for pi in range(a['page'], end['page']+1):
                for txt, box in source_lines(doc,r,pi):
                    if (pi>a['page'] or box[1]>a['y']+8) and (pi<end['page'] or box[1]<end['y']):
                        if re.match(r'^[【\[（(]?\s*(?:解析|解答|答案|证明|解)\s*[】\]）):：.．]',txt) and not re.match(r'^证明[：:]',txt):
                            boundary=dict(page=pi,y=box[1])
                            break
                if boundary:
                    break
        parts = []
        text = []
        two_col = r['contest'] == 'PUTNAM'
        units = range(a['page']*2+a.get('column',0), end['page']*2+end.get('column',0)+1) if two_col else range(a['page'], end['page']+1)
        for unit in units:
            pi, col = divmod(unit, 2) if two_col else (unit, 0)
            page = doc[pi]
            is_start = pi == a['page'] and (not two_col or col==a['column'])
            is_end = pi == end['page'] and (not two_col or col==end['column'])
            padding = 2 if r['id'] in OCR else 5
            y0 = max(0, a['y']-padding) if is_start else 0
            y1 = end['y']-padding if is_end else page.rect.height
            if y1 <= y0:
                continue
            x0, x1 = (0, page.rect.width)
            if two_col:
                x0, x1 = (25, page.rect.width/2-7) if col==0 else (page.rect.width/2+3, page.rect.width-22)
            clip = fitz.Rect(x0, y0, x1, y1)
            path = outdir / f'q{a["number"]}-p{pi+1}-c{col}.png'
            path.parent.mkdir(parents=True, exist_ok=True)
            page.get_pixmap(matrix=fitz.Matrix(1.65, 1.65), clip=clip, alpha=False).save(path)
            parts.append(dict(page=pi+1, bbox=list(clip), image=str(path.relative_to(ROOT))))
            text.extend(txt for txt,box in source_lines(doc,r,pi) if clip.intersects(fitz.Rect(box)))
        # Split an interleaved answer using an explicit heading, never guessed prose.
        answer_parts=[]
        if boundary:
            question_parts=[]
            for part in parts:
                pi=part['page']-1
                box=part['bbox']
                for kind, y0, y1 in [('question',box[1], min(box[3],boundary['y']-2) if pi==boundary['page'] else box[3]),
                                      ('answer',max(box[1],boundary['y']-2) if pi==boundary['page'] else box[1],box[3])]:
                    if (kind=='question' and pi>boundary['page']) or (kind=='answer' and pi<boundary['page']) or y1<=y0:
                        continue
                    clip=fitz.Rect(box[0],y0,box[2],y1)
                    path=outdir/f'q{a["number"]}-{kind}-p{pi+1}.png'
                    doc[pi].get_pixmap(matrix=fitz.Matrix(1.65,1.65),clip=clip,alpha=False).save(path)
                    (question_parts if kind=='question' else answer_parts).append(dict(page=pi+1,bbox=list(clip),image=str(path.relative_to(ROOT))))
            if question_parts and answer_parts:
                parts=question_parts
                text=[txt for part in parts for txt,box in source_lines(doc,r,part['page']-1) if fitz.Rect(part['bbox']).intersects(fitz.Rect(box))]
        result.append(dict(number=a['number'], segments=parts, answer_segments=answer_parts, text='\n'.join(text), grouped=a.get('grouped',False)))
    return result


def pair_key(r):
    if r['contest'] == 'YAU':
        name = Path(r.get('archive_member', r['title'])).stem.lower()
        name = re.sub(r'soln|solutions?|[\W_]|20\d{2}|\d{2}s?', '', name)
        return (r['contest'], r['year'], name)
    if r['contest'] == 'EGMO':
        return ('EGMO', r['year'], 'all')
    return (r['contest'], r['year'], r['part'])


def main():
    resources = json.loads((ROOT/'catalog/resources.json').read_text())
    questions, review, solutions = [], [], {}
    split_records = []
    anchor_path=ROOT/'catalog/anchor-overrides.json'
    anchor_overrides=json.loads(anchor_path.read_text()) if anchor_path.exists() else {}
    for r in resources:
        if r['status'] != 'downloaded' or r.get('multi_year') or r.get('skip_index'):
            continue
        doc = fitz.open(ROOT/r['local_path'])
        cache_path=ROOT/'catalog/ocr'/f'{r.get("parent_resource_id",r["id"])}.json'
        if cache_path.exists():
            cache=json.loads(cache_path.read_text())
            if cache['sha256']==r['sha256']:
                OCR[r['id']]=cache
        points = anchors(doc, r)
        override=anchor_overrides.get(r['id'],{})
        if override:
            points=override['anchors']
        if not points:
            review.append(dict(resource_id=r['id'], reason='No reliable text headings; scanned PDF or unsupported numbering.', priority='high' if r['contest'] in ('CMO','CHSMO','CMC') else 'normal'))
            continue
        chunks = slices(doc, r, points, ROOT/'derived'/r['id'],override.get('terminal'))
        expected = 6 if r['contest'] in ('IMO','CMO','EGMO') else 12 if r['contest']=='PUTNAM' else None
        if r['contest']=='EGMO' and r['role']=='questions': expected=3
        if r['contest']=='CHSMO':
            expected=4 if '加试' in r['title'] and '一试' not in r['title'] else 11 if '一试' in r['title'] and '加试' not in r['title'] else None
        if expected and len(chunks)!=expected:
            review.append(dict(resource_id=r['id'],reason=f'Heading count {len(chunks)} differs from expected {expected}; inspect boundaries and missing numbers.',priority='high'))
        split_records.append(dict(resource_id=r['id'], count=len(chunks), numbers=[c['number'] for c in chunks]))
        if r['role'] == 'solutions':
            for c in chunks:
                solutions[(*pair_key(r), c['number'])] = dict(resource_id=r['id'], segments=c['segments'], status='auto-candidate')
            continue
        for c in chunks:
            qid = r['id'] + '-q' + c['number']
            questions.append(dict(id=qid, resource_id=r['id'], contest=r['contest'], year=r['year'],
                number=c['number'], title=f'{r["title"]} · {c["number"]}',
                level='本科' if r['contest'] in ('CMC','IMC','YAU','PUTNAM') else '高中',
                tags=subject(c['text']), tag_status='keyword-suggestion', text=c['text'],
                segments=c['segments'], crop_status='auto-candidate', ocr_used=r['id'] in OCR,
                solution=dict(resource_id=r['id'],segments=c['answer_segments'],status='auto-boundary-candidate') if c['answer_segments'] else None,
                question_unit='section-with-subquestions' if c['grouped'] else 'problem',
                source_sha256=r['sha256'], authority=r['authority']))
        doc.close()
    rmap = {r['id']: r for r in resources}
    for q in questions:
        r = rmap[q['resource_id']]
        q['solution'] = q['solution'] or solutions.get((*pair_key(r), q['number']))
        if r['role'] == 'combined' and not q['solution']:
            q['solution_note'] = '题解合卷；当前切片含题面与解答，待核定题解分界。'
    overrides_path = ROOT/'catalog/overrides.json'
    if overrides_path.exists():
        for q in questions:
            q.update(json.loads(overrides_path.read_text()).get(q['id'], {}))
    write('catalog/questions.json', questions)
    write('catalog/question-index.json', [{**{k:q[k] for k in ('id','resource_id','contest','year','number','title','level','tags','tag_status','crop_status','authority','question_unit')},'has_solution':bool(q.get('solution'))} for q in questions])
    write('catalog/review-queue.json', review)
    write('catalog/split-report.json', split_records)
    print(json.dumps(dict(questions=len(questions), paired=sum(bool(q['solution']) for q in questions), review_documents=len(review))))


if __name__ == '__main__':
    main()
