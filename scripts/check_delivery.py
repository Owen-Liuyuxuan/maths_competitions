#!/usr/bin/env python3
"""Check the built reader's actual HTTP assets, not just source files."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import io
import json
from pathlib import Path
from urllib.parse import urljoin, quote
from urllib.request import urlopen
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]


def asset_paths(data):
    paths = {'index.html', 'app.js', 'app.css', 'data.js'}
    paths.update(data.get('vendor_assets', []))
    for resource in data['resources']:
        if resource.get('local_path'):
            paths.add(resource['local_path'])
    for question in data['questions']:
        for group in (question.get('segments', []), (question.get('solution') or {}).get('segments', [])):
            paths.update(segment['image'] for segment in group)
    return sorted(paths)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--url', default='http://127.0.0.1:8092/')
    args = parser.parse_args()
    # Read the same manifest that the browser receives, so stale served data is detected.
    with urlopen(urljoin(args.url, 'data.js'), timeout=10) as response:
        manifest = response.read().decode()
    data = json.loads(manifest.removeprefix('window.MATH_ATLAS = ').rstrip(';\n'))
    if data['mode'] != 'local':
        parser.error('Expected the full local reader, not the public metadata index')

    def check(path):
        try:
            local = ROOT / 'dist/library' / path
            with urlopen(urljoin(args.url, quote(path)), timeout=30) as response:
                body = response.read()
                if response.status != 200:
                    raise ValueError(f'HTTP {response.status}')
            if body != local.read_bytes():
                raise ValueError('served bytes differ from built file')
            if path.endswith('.png'):
                with Image.open(io.BytesIO(body)) as image:
                    image.verify()
            if path.endswith('.pdf') and not body.startswith(b'%PDF-'):
                raise ValueError('not a PDF response')
            return None
        except Exception as exc:
            return {'path': path, 'error': str(exc)}

    paths = asset_paths(data)
    with ThreadPoolExecutor(max_workers=8) as pool:
        errors = [error for error in pool.map(check, paths) if error]
    report = {'url': args.url, 'assets': len(paths), 'images': sum(p.endswith('.png') for p in paths),
              'pdfs': sum(p.endswith('.pdf') for p in paths), 'errors': errors}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    (ROOT / 'catalog/delivery-report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
