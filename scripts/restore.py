#!/usr/bin/env python3
"""Restore byte-identical direct PDFs. Reject drift; never replace existing files."""
import hashlib
import io
import json
import zipfile
from collect import ROOT,get

records=json.loads((ROOT/'catalog/resources.json').read_text())
archives={}
seen=set()
for r in records:
    if r['status']!='downloaded' or r.get('parent_resource_id'):continue
    path=ROOT/r['local_path']
    if path.exists() or path in seen:continue
    seen.add(path)
    try:
        if 'images-' in r['id'] or 'retypeset' in r['id']:
            print('Recollect article images:',r['id']);continue
        if r.get('archive_member'):
            if r['url'] not in archives:archives[r['url']]=zipfile.ZipFile(io.BytesIO(get(r['url']).content))
            data=archives[r['url']].read(r['archive_member'])
        else:data=get(r['url']).content
        if hashlib.sha256(data).hexdigest()!=r['sha256']:
            raise ValueError('SHA-256 mismatch; refusing changed bytes')
        path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(data)
        print('Restored',r['id'])
    except Exception as e:print('Failed',r['id'],str(e))
