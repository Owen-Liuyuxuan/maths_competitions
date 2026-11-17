"""Source-bound visual editions must not silently drift or regress."""
import json
from pathlib import Path
import tempfile
import shutil
import subprocess
import sys
import unittest

from editorial import clean_title, edition_questions


class EditorialTests(unittest.TestCase):
    def test_clean_titles(self):
        self.assertEqual(clean_title('2026 CMC（第三方重排图） · 1'), '2026 CMC · 1')
        self.assertEqual(clean_title('2024 CMO 完整试题及第三方解析'), '2024 CMO 试题与解答')

    def test_egmo_prefers_chinese_and_preserves_alias(self):
        qs = [dict(id='english', resource_id='egmo-English', contest='EGMO',year=2025,number='1',title='English',tags=['old']),
              dict(id='chinese', resource_id='egmo-ChineseSimplified',contest='EGMO',year=2025,number='1',title='中文',tags=['old'])]
        with tempfile.TemporaryDirectory() as tmp:
            result, aliases = edition_questions(Path(tmp), [], qs, render=False)
        self.assertEqual([q['id'] for q in result], ['chinese'])
        self.assertEqual(aliases, {'english': 'chinese'})
        self.assertEqual(result[0]['tags'], [])
        self.assertEqual(len(qs), 2)

    def test_editions_are_bound_to_source_and_have_real_tags(self):
        root = Path(__file__).resolve().parents[1]
        resources = json.loads((root/'catalog/resources.json').read_text())
        master = json.loads((root/'catalog/question-index.json').read_text())
        result, _ = edition_questions(root, resources, master, render=False)
        edited = [q for q in result if q.get('editorial_status') == 'model-visual']
        self.assertGreaterEqual(len(edited), 136)
        for q in edited:
            self.assertTrue(q['body_zh'])
            self.assertTrue(q['tags'])
            self.assertEqual(q['tag_status'], 'model-content')
            self.assertNotIn('待标注', q['tags'])
        cmc = [q for q in edited if q['resource_id'] == 'cmc-2026-images-2c0689e373-combined']
        self.assertEqual({q['number'] for q in cmc}, {'1.1','1.2','1.3','1.4',*(str(i) for i in range(2,11))})
        self.assertEqual(sum(q['contest']=='IMO' for q in edited),42)
        self.assertEqual(sum(q['contest']=='EGMO' for q in edited),42)
        changed = [dict(r) for r in resources]
        next(r for r in changed if r['id']==edited[0]['resource_id'])['sha256']='changed'
        with self.assertRaisesRegex(ValueError, 'source changed'):
            edition_questions(root, changed, master, render=False)

    def test_public_build_without_local_questions_or_originals(self):
        root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as tmp:
            fixture = Path(tmp)
            shutil.copytree(root/'scripts', fixture/'scripts')
            shutil.copytree(root/'web', fixture/'web')
            (fixture/'catalog').mkdir()
            for name in ('resources.json','question-index.json','competitions.json','review-queue.json'):
                shutil.copy2(root/'catalog'/name, fixture/'catalog'/name)
            shutil.copytree(root/'catalog/editorial', fixture/'catalog/editorial')
            subprocess.run([sys.executable,str(fixture/'scripts/build.py'),'--public'],check=True,capture_output=True,text=True)
            data=json.loads((fixture/'dist/public/data.js').read_text().removeprefix('window.MATH_ATLAS = ').rstrip(';\n'))
            self.assertEqual(len([q for q in data['questions'] if q['contest']=='EGMO']),42)
            for q in data['questions']:
                self.assertFalse({'body_zh','text','segments','solution','source_sha256'} & q.keys())


if __name__ == '__main__':
    unittest.main()
