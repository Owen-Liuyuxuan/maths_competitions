"""Regression coverage for assets actually referenced by the built reader."""
import unittest
import json
from pathlib import Path
from check_delivery import asset_paths


class DeliveryTests(unittest.TestCase):
    def test_2026_b_additional_excludes_appended_round_one(self):
        root = Path(__file__).resolve().parents[1]
        records = {r['id']: r for r in json.loads((root/'catalog/resources.json').read_text())}
        rid = 'chsmo-2026-images-6383343cd3-combined'
        self.assertEqual(records[rid]['page_range'], [1, 2])
        self.assertEqual(records[rid]['role'], 'questions')
        answers = records['chsmo-2026-scoped-B-additional-solutions']
        self.assertEqual(answers['page_range'], [2, 6])
        self.assertEqual(records[rid]['part'], answers['part'])
        anchors = json.loads((root/'catalog/anchor-overrides.json').read_text())
        self.assertEqual([a['number'] for a in anchors[rid]['anchors']], ['1', '2', '3', '4'])

    def test_includes_question_answer_and_original(self):
        data = {'resources': [{'local_path': 'originals/paper.pdf'}, {'status': 'download-failed'}],
                'questions': [{'segments': [{'image': 'derived/question.png'}],
                               'solution': {'segments': [{'image': 'derived/answer.png'}]}}]}
        self.assertEqual(asset_paths(data), sorted([
            'index.html', 'app.js', 'app.css', 'data.js', 'originals/paper.pdf',
            'derived/question.png', 'derived/answer.png']))

    def test_shared_slices_are_checked_once(self):
        segment = {'image': 'derived/shared.png'}
        data = {'resources': [], 'questions': [
            {'segments': [segment], 'solution': None},
            {'segments': [segment], 'solution': {'segments': [segment]}}]}
        self.assertEqual(asset_paths(data).count('derived/shared.png'), 1)

    def test_includes_offline_math_dependencies(self):
        data = {'resources': [], 'questions': [], 'vendor_assets': [
            'vendor/katex/katex.min.js', 'vendor/katex/katex.min.css',
            'vendor/katex/fonts/KaTeX_Main-Regular.woff2']}
        self.assertTrue(set(data['vendor_assets']).issubset(asset_paths(data)))


if __name__ == '__main__':
    unittest.main()
