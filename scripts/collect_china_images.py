#!/usr/bin/env python3
"""Supplement fragmented Chinese archives from openly visible article images.

Source images and their hashes remain intact. Generated PDFs are explicitly
marked as image-derived research copies, not official PDF originals.
"""
import concurrent.futures
import hashlib
import json
import re
import io
import argparse
import requests
from PIL import Image
from pathlib import Path
from urllib.parse import urljoin
import pymupdf as fitz
from collect import ROOT, NOW, get, soup, save

BASE = 'https://studio.wuhaneduyun.cn/'


def discover(page):
    url = BASE + f'index.php?catid=3774&page={page}&r=studio%2Fpost%2FGetContentListByCatid&sid=347'
    output = []
    for a in soup(url).select('a[href]'):
        title = a.get_text(' ', strip=True)
        # Exclude provincial heats, training commentary and mock tests.
        if re.search(r'202[0-6]年?全国高中数学(?:联合竞赛|联赛)(?:一试|加试|[ABC]卷及答案|[（(]A)', title) and not re.search(r'第\d+题|模拟|赏析',title):
            output.append((urljoin(BASE, a['href']), re.sub(r'卢琼.*$', '', title).strip()))
    return output


def archive(spec):
    url, title, contest, year, selector = spec
    slug = hashlib.sha256(url.encode()).hexdigest()[:10]
    rid = f'{contest.lower()}-{year}-images-{slug}-combined'
    folder = ROOT/f'originals/{contest.lower()}/{year}/{slug}'
    target = folder/'paper.pdf'
    folder.mkdir(parents=True, exist_ok=True)
    if not target.exists():
        # Ordinary HTML variant: some publishers hide article markup from custom bot UAs.
        from bs4 import BeautifulSoup
        response=requests.get(url,timeout=(10,30))
        response.raise_for_status()
        doc = BeautifulSoup(response.content,'html.parser')
        imgs = list(dict.fromkeys(urljoin(url, i['src']).replace('http://wx','https://wx') for i in doc.select(selector)))
        if not imgs:
            raise ValueError(f'No article images: {url}')
        output = fitz.open()
        provenance = []
        for n, src in enumerate(imgs):
            image_response=requests.get(src,headers={'Referer':url},timeout=(10,30))
            image_response.raise_for_status()
            data = image_response.content
            try:
                im = fitz.open(stream=data)
            except Exception:
                buffer=io.BytesIO()
                Image.open(io.BytesIO(data)).convert('RGB').save(buffer,format='PNG')
                im=fitz.open(stream=buffer.getvalue())
            pdf = fitz.open(stream=im.convert_to_pdf(), filetype='pdf')
            output.insert_pdf(pdf)
            path = folder/f'page-{n+1}.img'
            path.write_bytes(data)
            provenance.append(dict(url=src, path=str(path.relative_to(ROOT)), sha256=hashlib.sha256(data).hexdigest()))
        output.save(target)
        save(str(folder.relative_to(ROOT)/'provenance.json'), provenance)
    return dict(id=rid, contest=contest, year=year, title=title, part=slug, role='combined',
                url=url, source_url=url, authority='third-party', status='downloaded',
                local_path=str(target.relative_to(ROOT)), sha256=hashlib.sha256(target.read_bytes()).hexdigest(),
                pages=len(fitz.open(target)), bytes=target.stat().st_size, fetched_at=NOW,
                format_note='Derived PDF of openly visible article images. Not an official PDF original.',
                rights='Copyright retained by original authors. Local research copy; public build excludes content.')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--url',help='Collect only this configured supplemental article')
    args=parser.parse_args()
    specs = []
    errors = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        for batch in pool.map(discover, [] if args.url else range(1, 14)):
            for url, title in batch:
                specs.append((url, title, 'CHSMO', int(re.search(r'202[0-6]',title)[0]), '.art_con img[src]'))
    specs = list({s[0]:s for s in specs}.values())
    specs.append(('https://www.jingsailian.com/news/1619545.html', '2025 CMO 试题解答与评分标准（转载图）', 'CMO', 2025, '.article-content img[src*="/2025/11/"]'))
    # Article has .content.article container; selector is inspected, not global img.
    specs[-1] = (*specs[-1][:4], '.bpp-post-content img[src*="/2025/11/"]')
    supplemental=ROOT/'catalog/image-sources.json'
    supplements=json.loads(supplemental.read_text()) if supplemental.exists() else []
    specs.extend((s['url'],s['title'],s['contest'],s['year'],s['selector']) for s in supplements)
    if args.url: specs=[s for s in specs if s[0]==args.url]
    records = json.loads((ROOT/'catalog/resources.json').read_text())
    excluded = [r for r in records if re.search(r'模拟|赏析', r['title'])]
    records = [r for r in records if r not in excluded]
    save('catalog/excluded-resources.json', excluded)
    by_id = {r['id']:r for r in records}
    for spec in specs:
        try:
            r = archive(spec)
            extra=next((s for s in supplements if s['url']==spec[0]),{})
            r.update(extra.get('metadata',{}))
            by_id[r['id']] = r
            print(r['id'],r['pages'],flush=True)
        except Exception as e:
            errors.append(dict(url=spec[0],error=str(e)))
            if spec[0] in {s['url'] for s in supplements}:
                rid=f'{spec[2].lower()}-{spec[3]}-images-{hashlib.sha256(spec[0].encode()).hexdigest()[:10]}-combined'
                by_id.setdefault(rid,dict(id=rid,contest=spec[2],year=spec[3],title=spec[1],part='source-lead',role='combined',url=spec[0],source_url=spec[0],authority='third-party',status='download-failed',error=str(e)))
    save('catalog/resources.json', sorted(by_id.values(),key=lambda r:(r['contest'],r['year'],r['id'])))
    save('catalog/china-image-log.json',errors)
    print('Added',len(by_id)-len(records),'records; errors:',len(errors))


if __name__=='__main__':
    main()
