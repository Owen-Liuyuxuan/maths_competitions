#!/usr/bin/env python3
"""Cache OCR line coordinates for scanned papers, leaving originals unchanged."""
import concurrent.futures
import json
import os
import argparse
import re
from pathlib import Path
import pymupdf as fitz

ROOT=Path(__file__).resolve().parents[1]
TESSDATA=Path(os.environ.get('TESSDATA_PREFIX',ROOT/'tmp/ocr-runtime/root/usr/share/tesseract-ocr/4.00/tessdata'))
DPI=400


def run(record):
    os.environ['OMP_THREAD_LIMIT']='1'
    out=ROOT/'catalog/ocr'/f'{record["id"]}.json'
    if out.exists():
        cached=json.loads(out.read_text())
        if cached.get('dpi',170)==DPI and cached['sha256']==record['sha256']:
            return record['id']+' cached'
    doc=fitz.open(ROOT/record['local_path'])
    pages=[]
    for page in doc:
        # Very tall image pages can exceed Tesseract's raster limits.
        for dpi in (DPI,200,100):
            try:
                tp=page.get_textpage_ocr(language='chi_sim+eng',dpi=dpi,full=True,tessdata=str(TESSDATA))
                break
            except Exception as exc:
                if dpi==100:
                    raise RuntimeError(f"OCR failed: {record['id']} page {page.number+1}: {exc}") from None
        ls=[]
        for b in page.get_text('dict',textpage=tp)['blocks']:
            for line in b.get('lines',[]):
                ls.append([''.join(s['text'] for s in line['spans']).strip(),list(line['bbox'])])
        pages.append(ls)
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(dict(resource_id=record['id'],sha256=record['sha256'],dpi=DPI,engine=f'MuPDF/Tesseract chi_sim+eng {DPI}dpi',purpose='heading coordinates only; not proofread mathematical transcription',pages=pages),ensure_ascii=False,indent=2)+'\n')
    return record['id']+' '+str(len(pages))+' pages'


if __name__=='__main__':
    if not (TESSDATA/'chi_sim.traineddata').exists():
        raise SystemExit('Set TESSDATA_PREFIX to tessdata containing chi_sim and eng traineddata.')
    records=json.loads((ROOT/'catalog/resources.json').read_text())
    jobs=[]
    for r in records:
        if r['status']!='downloaded' or r['contest'] not in ('CHSMO','CMO','CMC') or r.get('multi_year') or r.get('parent_resource_id'):
            continue
        doc=fitz.open(ROOT/r['local_path'])
        text=''.join(p.get_text() for p in doc)
        if len(text.strip())<100 or (r['contest']=='CMC' and len(re.findall(r'[\u4e00-\u9fff]',text))<30):
            jobs.append(r)
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as pool:
        for result in pool.map(run,jobs):
            print(result,flush=True)
