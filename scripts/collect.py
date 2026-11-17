#!/usr/bin/env python3
"""Collect source-linked contest PDFs; cache originals and record every failure.

Run from any directory. No authentication, paywalls or CAPTCHA bypassing.
"""
from __future__ import annotations

import concurrent.futures
import hashlib
import io
import json
import re
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin
from urllib.parse import quote

import pymupdf as fitz
import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
YEARS = range(2020, 2027)
NOW = datetime.now(timezone.utc).isoformat()
RESOURCES: list[dict] = []
LOG: list[dict] = []


def save(path, obj):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')


def get(url):
    r = requests.get(url, timeout=(10, 50), headers={'User-Agent': 'MathAtlasResearch/0.1 (educational archive; source links retained)'})
    r.raise_for_status()
    return r


def soup(url):
    r = get(url)
    return BeautifulSoup(r.content, 'html.parser')


def add(contest, year, part, role, url, source, title='', authority='official', **extra):
    rid = f'{contest.lower()}-{year}-{part}-{role}'
    RESOURCES.append(dict(id=rid, contest=contest, year=year, part=part, role=role,
                          url=url, source_url=source, title=title or f'{contest} {year} {part}',
                          authority=authority, rights='Copyright retained by original authors; redistribution permission not established.',
                          **extra))


def discover_international():
    for year in YEARS:
        source = f'https://www.imo-official.org/problems/{year}/'
        try:
            for a in soup(source).select('a[href]'):
                h = urljoin(source, a['href'])
                if re.search(rf'/{year}_eng\.pdf$', h):
                    add('IMO', year, 'main', 'questions', h, source)
        except Exception as e:
            LOG.append(dict(url=source, error=str(e)))
        source = f'https://www.egmo.org/egmos/egmo{year-2011}/'
        try:
            for a in soup(source).select('a[href]'):
                h = urljoin(source, a['href'])
                m = re.search(r'paper-day([12])-(English|ChineseSimplified)\.pdf$', h)
                if m:
                    add('EGMO', year, f'day{m[1]}-{m[2]}', 'questions', h, source,
                        language='zh-Hans' if m[2] == 'ChineseSimplified' else 'en')
                elif re.search(r'/solutions\.pdf$', h):
                    add('EGMO', year, 'both-days', 'solutions', h, source)
        except Exception as e:
            LOG.append(dict(url=source, error=str(e)))
        source = f'https://imc-math.org.uk/?item=problems&year={year}'
        try:
            for a in soup(source).select('a[href]'):
                h = urljoin(source, a['href'])
                m = re.search(r'Day[_ -]?([12])[_ -]?(Questions|Solutions)\.pdf$', h, re.I)
                if m:
                    add('IMC', year, f'day{m[1]}', m[2].lower(), h, source)
        except Exception as e:
            LOG.append(dict(url=source, error=str(e)))


def discover_cmc():
    source = 'https://gdjpkc.xmu.edu.cn/DocumentList.aspx?cID=22&dID=383'
    try:
        doc = soup(source)
        for a in doc.select('a[href*="FlashShow"]'):
            title = a.get_text(' ', strip=True)
            if not re.search(r'202[0-6]', title) or '全国' not in title:
                continue
            # Download controls live in the same nested table, not the title row.
            table = a.find_parent('table')
            downloads = table.select('a[href*="FileDown"]') if table else []
            if not downloads:
                LOG.append(dict(url=urljoin(source, a['href']), title=title, error='Flash-only entry; PDF download not exposed'))
                continue
            year = int(re.search(r'202[0-6]', title)[0])
            lid = re.search(r'lID=(\d+)', a['href'])[1]
            for i, d in enumerate(downloads):
                add('CMC', year, f'xmu-{lid}-{i}', 'combined', urljoin(source, d['href']),
                    urljoin(source, a['href']), title, authority='university-mirror',
                    date_note='Year follows source title; edition and actual sitting date need separate verification.')
    except Exception as e:
        LOG.append(dict(url=source, error=str(e)))


def discover_mirrors():
    source = 'https://nhatchim37-sudo.github.io/cmc-preliminary-papers/'
    numerals = {'十二': 12, '十三': 13, '十四': 14, '十五': 15, '十六': 16, '十七': 17}
    seen = set()
    for a in soup(source).select('a[href$=".pdf"]'):
        h = a['href']
        if h in seen or h.startswith('https:'):
            continue
        seen.add(h)
        m = re.search(r'finals/edition-(\d+)/(.+)\.pdf', h)
        if m:
            edition = int(m[1])
            if edition < 11:
                continue
            year = {11: 2021, 12: 2021, 13: 2023, 14: 2023, 15: 2024, 16: 2025}[edition]
            part = f'final-{edition}-{m[2]}'
            title = f'第{edition}届 CMC 决赛 {m[2]}'
        else:
            m = re.search(r'第(十二|十三|十四|十五|十六|十七)届', h)
            if not m:
                continue
            edition = numerals[m[1]]
            year = edition + 2008
            part = 'preliminary-' + hashlib.sha256(h.encode()).hexdigest()[:10]
            title = Path(h).stem
        role = 'solutions' if h.endswith('-solutions.pdf') else 'questions' if h.endswith('-questions.pdf') else 'combined'
        add('CMC', year, part, role, urljoin(source, quote(h)), source, title,
            'community-mirror', edition=edition,
            date_note='Final year is actual sitting year (pandemic postponements); preliminary makeup sitting date requires checking.')
    checkout = ROOT / 'tmp/putnam-source'
    if checkout.exists():
        import subprocess
        commit = subprocess.check_output(['git', '-C', str(checkout), 'rev-parse', 'HEAD'], text=True).strip()
        for p in checkout.rglob('*.pdf'):
            m = re.fullmatch(r'(202[0-5])(s?)\.pdf', p.name)
            if not m:
                continue
            year = int(m[1])
            role = 'solutions' if m[2] else 'questions'
            h = f'https://raw.githubusercontent.com/rpxgit/The-Putnam-Archive/{commit}/' + quote(str(p.relative_to(checkout)))
            add('PUTNAM', year, 'AB', role, h, 'https://kskedlaya.org/putnam-archive/',
                f'Putnam {year} {role} (Kedlaya archive community mirror)', 'community-mirror',
                mirror_url=f'https://github.com/rpxgit/The-Putnam-Archive/tree/{commit}',
                date_note='2020 edition held in February 2021; 2026 competition not yet held as of 2026-11-16.')


def collect_yau():
    url = 'https://www.yau-contest.com/index/reldown?id=9'
    archive_path = ROOT / 'originals/yau/written-archive.zip'
    try:
        archive_path.parent.mkdir(parents=True, exist_ok=True)
        if not archive_path.exists():
            archive_path.write_bytes(get(url).content)
        with zipfile.ZipFile(archive_path) as z:
            for member in z.infolist():
                if not member.filename.lower().endswith('.pdf') or Path(member.filename).name.startswith('._'):
                    continue
                # Match directory year, not the range in the top-level directory.
                m = re.search(r'/(202[0-6])/', member.filename)
                if not m:
                    continue
                year = int(m[1])
                digest = hashlib.sha256(member.filename.encode()).hexdigest()[:10]
                role = 'solutions' if re.search(r'soln|solution', member.filename, re.I) else 'questions'
                rid = f'yau-{year}-{digest}-{role}'
                data = z.read(member)
                p = ROOT / f'originals/yau/{year}/{digest}.pdf'
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_bytes(data)
                with fitz.open(stream=data, filetype='pdf') as pdf:
                    pages = len(pdf)
                RESOURCES.append(dict(id=rid, contest='YAU', year=year, part=digest, role=role,
                    title=Path(member.filename).name, url=url, source_url='https://www.yau-contest.com/lists-jxxg.html',
                    archive_member=member.filename, archive_sha256=hashlib.sha256(archive_path.read_bytes()).hexdigest(),
                    authority='official', status='downloaded', local_path=str(p.relative_to(ROOT)),
                    sha256=hashlib.sha256(data).hexdigest(), bytes=len(data), pages=pages, fetched_at=NOW,
                    rights='Copyright retained by contest and problem authors; local research copy.'))
    except Exception as e:
        LOG.append(dict(url=url, error=str(e)))


def discover_china():
    # Known direct assets plus article crawling; never infer PDF identity from URL alone.
    add('CHSMO', 2020, 'B-round1', 'combined',
        'https://cdn.gaokzx.com/zixunzhan/202403/31f87db7-f145-4489-ad79-1d18134045bf.pdf',
        'https://www.gaokzx.com/', '2020 全国高中数学联赛 一试 B卷及参考答案', 'third-party')
    add('CHSMO', 2021, 'A-round1', 'combined',
        'https://www.gaokzx.com/Fup/document/202109/09-13_094942-10105.pdf',
        'https://www.gaokzx.com/c/202109/56002_5.html', '2021 全国高中数学联赛 一试 A卷答案', 'third-party')
    add('CHSMO', 2021, 'B-round1', 'combined',
        'https://www.gaokzx.com/Fup/document/202109/09-13_140215-10105.pdf',
        'https://www.gaokzx.com/c/202109/55976.html', '2021 全国高中数学联赛 一试 B卷答案', 'third-party')
    add('CHSMO', 2023, 'A-round1', 'combined',
        'https://www.gaokzx.com/Fup/document/202309/09-10_164405-10171.pdf',
        'https://www.gaokzx.com/', '2023 全国高中数学联赛 一试 A卷试题答案', 'third-party')
    add('CMO', 2024, 'both-days', 'combined',
        'https://cdn.gaokzx.com/17328441195182024CMO完整试题及解析(encrypted).pdf',
        'https://www.gaokzx.com/', '2024 CMO 完整试题及第三方解析', 'third-party')
    add('CMO', 2020, 'historical-compilation', 'compilation',
        'https://upload.xuanyan.ws/chinese-mathematical-olympiads.pdf',
        'https://upload.xuanyan.ws/chinese-mathematical-olympiads.pdf',
        '中国数学奥林匹克历年试题汇编（需按卷内年份索引）', 'third-party', multi_year=True)
    articles = [
        ('CHSMO', 2021, 'https://www.gaokzx.com/c/202109/55976.html'),
        ('CHSMO', 2022, 'https://www.gaokzx.com/c/202211/66231.html'),
        ('CMO', 2022, 'https://www.gaokzx.com/c/202212/67119.html'),
        ('CHSMO', 2024, 'https://www.gaokzx.com/gk/shitiku/127695.html'),
        ('CHSMO', 2024, 'https://www.gaokzx.com/gk/shitiku/127696.html'),
        ('CHSMO', 2024, 'https://www.gaokzx.com/gk/shitiku/127697.html'),
        ('CMO', 2025, 'https://www.gaokzx.com/gk/gaozhongjingsai/150370.html'),
    ]
    for contest, year, source in articles:
        try:
            doc = soup(source)
            found = set()
            for a in doc.select('[href],iframe[src],embed[src]'):
                h = urljoin(source, a.get('href') or a.get('src'))
                if '.pdf' in h.lower() and h not in found:
                    found.add(h)
                    add(contest, year, 'article-' + hashlib.sha256(h.encode()).hexdigest()[:8],
                        'combined', h, source, doc.title.get_text() if doc.title else '', 'third-party',
                        identity_review='Article-derived PDF: verify paper heading before indexing.')
            if not found:
                LOG.append(dict(url=source, error='No direct PDF exposed; article may use images or gated download.'))
        except Exception as e:
            LOG.append(dict(url=source, error=str(e)))


def collect_image_paper():
    source = 'https://www.latexstudio.net/index/details/index/mid/5107.html'
    try:
        images = [urljoin(source, i['src']) for i in soup(source).select('.picList img[src]')]
        target = ROOT / 'originals/chsmo/2026/chsmo-2026-A-retypeset.pdf'
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists():
            pdf = fitz.open()
            image_sources = []
            for n, u in enumerate(images):
                data = get(u).content
                ip = target.parent / f'page-{n+1}.jpg'
                ip.write_bytes(data)
                image_sources.append(dict(url=u, local_path=str(ip.relative_to(ROOT)), sha256=hashlib.sha256(data).hexdigest()))
                im = fitz.open(stream=data, filetype='jpg')
                converted = fitz.open(stream=im.convert_to_pdf(), filetype='pdf')
                pdf.insert_pdf(converted)
            pdf.save(target)
            save('catalog/chsmo-2026-image-provenance.json', image_sources)
        add('CHSMO', 2026, 'A-retypeset', 'combined', source, source,
            '2026 全国高中数学联赛 A卷试题与参考答案（第三方重排图）', 'third-party',
            status='downloaded', local_path=str(target.relative_to(ROOT)),
            pages=len(fitz.open(target)), sha256=hashlib.sha256(target.read_bytes()).hexdigest(),
            bytes=target.stat().st_size, fetched_at=NOW, format_note='Derived PDF from six source JPEGs; not an original official PDF.')
    except Exception as e:
        LOG.append(dict(url=source, error=str(e)))


def download(r):
    if r.get('status') == 'downloaded':
        return r
    p = ROOT / f'originals/{r["contest"].lower()}/{r["year"]}/{r["id"]}.pdf'
    try:
        data = p.read_bytes() if p.exists() else get(r['url']).content
        if not data.lstrip().startswith(b'%PDF-'):
            raise ValueError('Response is not a PDF')
        with fitz.open(stream=data, filetype='pdf') as pdf:
            pages = len(pdf)
            head = pdf[0].get_text()[:1800]
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)
        r.update(status='downloaded', local_path=str(p.relative_to(ROOT)), bytes=len(data),
                 sha256=hashlib.sha256(data).hexdigest(), pages=pages, fetched_at=NOW,
                 first_page_excerpt=head)
    except Exception as e:
        r.update(status='failed', error=str(e), checked_at=NOW)
    return r


def main():
    discover_international()
    discover_cmc()
    discover_mirrors()
    discover_china()
    collect_yau()
    collect_image_paper()
    unique = {r['id']: r for r in RESOURCES}
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        records = list(pool.map(download, unique.values()))
    records.sort(key=lambda r: (r['contest'], r['year'], r['id']))
    compilation = next((r for r in records if r['id']=='cmo-2020-historical-compilation-compilation' and r['status']=='downloaded'), None)
    if compilation:
        for year, start in [(2020, 66), (2021, 68), (2022, 70)]:
            item = dict(compilation)
            item.update(id=f'cmo-{year}-compilation-extract-questions', year=year, part='compilation-extract', role='questions',
                        title=f'CMO {year} 试题（第三方汇编）', page_range=[start, start+2], multi_year=False)
            records.append(item)
    previous_path = ROOT/'catalog/resources.json'
    previous = json.loads(previous_path.read_text()) if previous_path.exists() else []
    merged = {r['id']: r for r in previous}
    merged.update({r['id']:r for r in records})
    records = [r for r in merged.values() if not re.search(r'模拟|赏析',r['title'])]
    save('catalog/resources.json', sorted(records,key=lambda r:(r['contest'],r['year'],r['id'])))
    save('catalog/collection-log.json', LOG)
    print(json.dumps(dict(resources=len(records), downloaded=sum(r['status']=='downloaded' for r in records),
                          discovery_issues=len(LOG)), ensure_ascii=False))


if __name__ == '__main__':
    main()
