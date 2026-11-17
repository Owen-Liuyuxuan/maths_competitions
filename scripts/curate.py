#!/usr/bin/env python3
"""Apply source-specific, reviewed metadata and page scopes after collection."""
import json
import hashlib
from pathlib import Path
import pymupdf as fitz

ROOT=Path(__file__).resolve().parents[1]
path=ROOT/'catalog/resources.json'
records=json.loads(path.read_text())
updates=json.loads((ROOT/'catalog/curation.json').read_text())
for r in records:
    r.update(updates.get(r['id'],{}))
    if r['id'] in {'chsmo-2026-images-6383343cd3-combined','cmo-2023-images-db13680339-combined'} and r['status']=='downloaded':
        manifest=ROOT/r['local_path'];manifest=manifest.parent/'provenance.json'
        images=json.loads(manifest.read_text())
        selected=[im for im in images if (
            '/wx' in im['url'] if r['contest']=='CHSMO'
            else '1701227702-6-1701227702.jpeg' in im['url'])]
        if selected and len(selected)!=len(images):
            output=fitz.open()
            for im in selected:
                image=fitz.open(ROOT/im['path'])
                output.insert_pdf(fitz.open(stream=image.convert_to_pdf(),filetype='pdf'))
            output.save(ROOT/r['local_path'])
            manifest.write_text(json.dumps(selected,ensure_ascii=False,indent=2)+'\n')
            r.update(pages=len(output),sha256=hashlib.sha256((ROOT/r['local_path']).read_bytes()).hexdigest(),bytes=(ROOT/r['local_path']).stat().st_size)
by_id={r['id']:r for r in records}
parent=by_id.get('chsmo-2026-images-6383343cd3-combined')
if parent:
    # The article appends unrelated round-one images after the four add-on solutions.
    # Keep the old question IDs valid, but restrict indexing to the actual add-on paper.
    parent.update(role='questions',part='B-additional',page_range=[1,2],
        format_note='来源图共9页；第2页为加试B卷四题，第3–6页为第三方解答。后附一试图不混入加试索引。')
    rid='chsmo-2026-scoped-B-additional-solutions'
    by_id[rid]={**parent,'id':rid,'role':'solutions','page_range':[2,6],
        'title':'2026 全国高中数学联赛 加试 B卷第三方解答（转载图）',
        'parent_resource_id':parent['id']}
by_id.pop('chsmo-2026-scoped-A-additional-solutions',None)
parent=by_id.get('chsmo-2026-A-retypeset-combined')
if parent:
    parent['skip_index']=True
    for part,role,pages,name in [
        ('A-round1','questions',[0,1],'一试 A卷试题'),
        ('A-additional','questions',[1,2],'加试 A卷试题'),
        ('A-round1','solutions',[2,6],'一试 A卷参考答案')]:
        rid=f'chsmo-2026-scoped-{part}-{role}'
        by_id[rid]={**parent,'id':rid,'part':part,'role':role,'page_range':pages,
            'title':f'2026 全国高中数学联赛 {name}（第三方重排）',
            'parent_resource_id':parent['id'],'skip_index':False}
parent=by_id.get('chsmo-2025-images-7786ec90d8-combined')
if parent:
    parent['skip_index']=True
    for part,role,pages,name in [
        ('A-round1','questions',[0,2],'一试 A卷试题'),
        ('A-round1','solutions',[2,7],'一试 A卷参考答案'),
        ('A-additional','questions',[7,8],'加试 A卷试题'),
        ('A-additional','solutions',[8,16],'加试 A卷参考答案')]:
        rid=f'chsmo-2025-scoped-{part}-{role}'
        by_id[rid]={**parent,'id':rid,'part':part,'role':role,'page_range':pages,
            'title':f'2025 全国高中数学联赛 {name}（转载图）',
            'parent_resource_id':parent['id'],'skip_index':False}
path.write_text(json.dumps(sorted(by_id.values(),key=lambda r:(r['contest'],r['year'],r['id'])),ensure_ascii=False,indent=2)+'\n')
