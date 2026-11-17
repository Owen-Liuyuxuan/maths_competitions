#!/usr/bin/env python3
"""Validate archive integrity; never promotes automatic crops to reviewed."""
import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
import pymupdf as fitz
from editorial import edition_questions
from teaching import load_teaching_map

ROOT=Path(__file__).resolve().parents[1]


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--metadata-only',action='store_true')
    args=parser.parse_args()
    resources=json.loads((ROOT/'catalog/resources.json').read_text())
    questions=json.loads((ROOT/'catalog'/('question-index.json' if args.metadata_only else 'questions.json')).read_text())
    questions, aliases=edition_questions(ROOT,resources,questions,render=False)
    teaching_map=load_teaching_map(ROOT,resources)
    errors=[]
    def check(ok,message):
        if not ok: errors.append(message)
    for label,items in [('resources',resources),('questions',questions)]:
        ids=[i['id'] for i in items]
        check(len(ids)==len(set(ids)),f'Duplicate IDs: {label}')
    rmap={r['id']:r for r in resources}
    checked=set()
    for r in resources:
        check(2020<=r['year']<=2026,'Year out of range: '+r['id'])
        check(not any(t in r['title'] for t in ('模拟','赏析')),'Excluded content: '+r['id'])
        if args.metadata_only or r['status']!='downloaded': continue
        path=ROOT/r['local_path']
        check(path.is_file(),'Missing original: '+str(path))
        if not path.is_file(): continue
        if str(path) not in checked:
            check(hashlib.sha256(path.read_bytes()).hexdigest()==r['sha256'],'Hash mismatch: '+r['id'])
            checked.add(str(path))
            manifest=path.parent/'provenance.json'
            if manifest.exists():
                for im in json.loads(manifest.read_text()):
                    ip=ROOT/im['path']
                    check(ip.is_file(),'Missing source image: '+str(ip))
                    if ip.is_file():
                        check(hashlib.sha256(ip.read_bytes()).hexdigest()==im['sha256'],
                              'Image hash mismatch: '+str(ip))
        with fitz.open(path) as doc:
            check(len(doc)==r['pages'],'Page count mismatch: '+r['id'])
            if 'page_range' in r:
                lo,hi=r['page_range'];check(0<=lo<hi<=len(doc),'Invalid page range: '+r['id'])
    for q in questions:
        check(q['resource_id'] in rmap,'Broken question resource: '+q['id'])
        if args.metadata_only or q['resource_id'] not in rmap: continue
        groups=[(rmap[q['resource_id']],q['segments'])]
        if q.get('solution'):
            sr=rmap.get(q['solution']['resource_id'])
            check(bool(sr),'Missing solution source: '+q['id'])
            if sr:
                check((sr['contest'],sr['year'])==(q['contest'],q['year']),'Cross-contest/year answer: '+q['id'])
                groups.append((sr,q['solution']['segments']))
        for r,segments in groups:
            check(bool(segments),'Empty crop: '+q['id'])
            with fitz.open(ROOT/r['local_path']) as doc:
                for s in segments:
                    check(1<=s['page']<=len(doc),'Crop page out of range: '+q['id'])
                    if not 1<=s['page']<=len(doc):continue
                    rect=fitz.Rect(s['bbox']);page=doc[s['page']-1].rect
                    check(not rect.is_empty and rect in page,'Invalid crop bounds: '+q['id'])
                    check((ROOT/s['image']).is_file(),'Missing crop: '+s['image'])
    public=ROOT/'dist/public'
    if public.exists():
        check({p.name for p in public.iterdir()}=={'index.html','app.css','app.js','data.js','vendor'},'Unexpected public files')
        data=json.loads((public/'data.js').read_text().removeprefix('window.MATH_ATLAS = ').rstrip(';\n'))
        for q in data['questions']:
            check(not any(k in q for k in ('text','body_zh','solution','segments','source_sha256','teaching')),'Content leaked to public index')
        for r in data['resources']:
            check('local_path' not in r,'Local file leaked to public index')
    summary=dict(resources=len(resources),downloaded=sum(r['status']=='downloaded' for r in resources),questions=len(questions),
        paired=sum(bool(q.get('solution') or q.get('has_solution')) for q in questions),teaching=len(teaching_map),errors=errors,mode='metadata' if args.metadata_only else 'full')
    print(json.dumps(summary,ensure_ascii=False,indent=2))
    if errors: raise SystemExit(1)
    (ROOT/'catalog/validation-report.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    rows=['# 年份覆盖','', '自动生成：下载记录数含语言、解答及页范围版本，不代表完整度。','',
        '|赛事|'+ '|'.join(map(str,range(2020,2027)))+'|','|---|'+'---|'*7]
    for c in json.loads((ROOT/'catalog/competitions.json').read_text()):
        counts=Counter(r['year'] for r in resources if r['contest']==c['id'] and r['status']=='downloaded' and not r.get('multi_year'))
        rows.append('|'+c['id']+'|'+ '|'.join(str(counts[y]) if counts[y] else '待补/未发布' for y in range(2020,2027))+'|')
    rows+=['','未完成逐题人工认证；已知缺口见 [RESEARCH.md](RESEARCH.md)。','']
    (ROOT/'docs/COVERAGE.md').write_text('\n'.join(rows))


if __name__=='__main__': main()
