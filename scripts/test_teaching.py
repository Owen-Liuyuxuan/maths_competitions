"""Source-bound blind-solve teaching records must stay consistent and never leak to public builds."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from editorial import edition_questions
from teaching import DIFFICULTY_TAGS, METHOD_TAGS, PITFALL_TAGS, apply_teaching, load_teaching_map


class TeachingTests(unittest.TestCase):
    def test_teaching_records_bound_to_sources_and_tags(self):
        root = Path(__file__).resolve().parents[1]
        resources = json.loads((root / "catalog/resources.json").read_text())
        master = json.loads((root / "catalog/question-index.json").read_text())
        edited, _ = edition_questions(root, resources, master, render=False)
        tmap = load_teaching_map(root, resources)
        self.assertGreaterEqual(len(tmap), 7)
        for qid, rec in tmap.items():
            an = rec["analysis"]
            self.assertIn(an["difficulty_tag"], DIFFICULTY_TAGS)
            self.assertTrue(set(an["method_tags"]).issubset(METHOD_TAGS))
            self.assertTrue(set(an["pitfall_tags"]).issubset(PITFALL_TAGS))
            self.assertTrue(an["problem_decomposition"])
            self.assertTrue(an["solution_breakdown"])
            self.assertTrue(an["common_pitfalls"])

        applied = apply_teaching(root, resources, edited, include_content=True)
        with_teaching = [q for q in applied if q.get("has_teaching")]
        self.assertEqual(len(with_teaching), len(tmap))

        changed = [dict(r) for r in resources]
        first_rid = next(iter(tmap.values()))["resource_id"]
        next(r for r in changed if r["id"] == first_rid)["sha256"] = "changed"
        with self.assertRaisesRegex(ValueError, "source changed"):
            load_teaching_map(root, changed)

    def test_public_build_keeps_teaching_tags_only(self):
        root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as tmp:
            fixture = Path(tmp)
            shutil.copytree(root / "scripts", fixture / "scripts")
            shutil.copytree(root / "web", fixture / "web")
            (fixture / "catalog").mkdir()
            for name in ("resources.json", "question-index.json", "competitions.json", "review-queue.json"):
                shutil.copy2(root / "catalog" / name, fixture / "catalog" / name)
            shutil.copytree(root / "catalog/editorial", fixture / "catalog/editorial")
            shutil.copytree(root / "catalog/teaching", fixture / "catalog/teaching")
            subprocess.run([sys.executable, str(fixture / "scripts/build.py"), "--public"], check=True, capture_output=True, text=True)
            data = json.loads((fixture / "dist/public/data.js").read_text().removeprefix("window.MATH_ATLAS = ").rstrip(";\n"))
            taught = [q for q in data["questions"] if q.get("has_teaching")]
            self.assertGreaterEqual(len(taught), 7)
            for q in data["questions"]:
                self.assertNotIn("teaching", q)
                self.assertFalse({"body_zh", "text", "segments", "solution", "source_sha256"} & q.keys())


if __name__ == "__main__":
    unittest.main()
