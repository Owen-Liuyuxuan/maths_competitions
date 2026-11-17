#!/usr/bin/env python3
"""Build an offline local reader, or an allowlisted metadata-only public index."""
import argparse
import json
import shutil
from pathlib import Path
from check_delivery import asset_paths
from editorial import edition_questions, clean_title
from teaching import apply_teaching

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--public', action='store_true', help='Metadata and external source links only')
args = parser.parse_args()
dest = ROOT / ('dist/public' if args.public else 'dist/library')
dest.mkdir(parents=True, exist_ok=True)
if args.public and any(p.name not in {'index.html','app.css','app.js','data.js','vendor'} for p in dest.iterdir()):
    raise SystemExit('Public destination contains unexpected files; inspect it before rebuilding.')
resources = json.loads((ROOT/'catalog/resources.json').read_text())
question_path=ROOT/'catalog/questions.json'
if not question_path.exists() and not args.public:
    raise SystemExit('Run scripts/index.py first to generate local question slices, or use --public.')
questions = json.loads((question_path if question_path.exists() else ROOT/'catalog/question-index.json').read_text())
competitions = json.loads((ROOT/'catalog/competitions.json').read_text())
review = json.loads((ROOT/'catalog/review-queue.json').read_text())
questions, aliases = edition_questions(ROOT, resources, questions, render=not args.public)
questions = apply_teaching(ROOT, resources, questions, include_content=not args.public)
for resource in resources:
    resource['title'] = clean_title(resource['title'])
resources = [r for r in resources if not (r['contest']=='EGMO' and 'English' in r['part'] and any(
    s['contest']=='EGMO' and s['year']==r['year'] and s['part']==r['part'].replace('English','ChineseSimplified')
    for s in resources))]
if args.public:
    # Explicit allowlists, not denylist subtraction.
    resources = [{k:r[k] for k in ('id','contest','year','part','role','title','authority','status','source_url','url','multi_year','completeness','parent_resource_id') if k in r} for r in resources]
    questions = [{**{k:q[k] for k in ('id','resource_id','contest','year','number','title','level','tags','teaching_tags','teaching_difficulty','teaching_methods','teaching_pitfalls','teaching_outcome','has_teaching','tag_status','crop_status','authority','question_unit','editorial_status') if k in q},'has_solution':bool(q.get('solution') or q.get('has_solution'))} for q in questions]
else:
    for folder in ('originals','derived'):
        shutil.copytree(ROOT/folder, dest/folder, dirs_exist_ok=True)
for name in ('index.html', 'app.css', 'app.js'):
    shutil.copy2(ROOT/'web'/name, dest/name)
shutil.copytree(ROOT/'web/vendor',dest/'vendor',dirs_exist_ok=True)
data = dict(mode='public' if args.public else 'local', competitions=competitions,
            resources=resources, questions=questions, review=review,
            aliases=aliases, as_of='2026-11-16', years=list(range(2020,2027)),
            vendor_assets=sorted(str(p.relative_to(ROOT/'web')) for p in (ROOT/'web/vendor').rglob('*') if p.is_file()))
(dest/'data.js').write_text('window.MATH_ATLAS = '+json.dumps(data, ensure_ascii=False)+';\n')
if not args.public:
    missing=[path for path in asset_paths(data) if not (dest/path).is_file()]
    if missing:
        raise SystemExit('Built reader has missing assets: '+', '.join(missing[:10]))
print(dest)
