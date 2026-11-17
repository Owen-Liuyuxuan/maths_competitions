"""Apply source-bound blind-solve records, teaching tags, and pedagogical analyses."""
import copy
import json
import re
from pathlib import Path


def _clean_math_punctuation(val):
    if isinstance(val, str):
        val = re.sub(r"([。，、；：]+)(\s*)(\\\]|\\\))", r"\3\1\2", val)
        val = re.sub(r"，(\s*\\q?quad\b)", r",\1", val)
        return val
    if isinstance(val, list):
        return [_clean_math_punctuation(v) for v in val]
    if isinstance(val, dict):
        return {k: _clean_math_punctuation(v) for k, v in val.items()}
    return val

METHOD_TAGS = [
    "放缩与估值",
    "构造与反例",
    "不变量与单调量",
    "极端原理",
    "奇偶与同余",
    "对称与轮换",
    "变量代换与重参数化",
    "生成函数与多项式",
    "归纳与递推",
    "辅助线与几何变换",
    "局部-整体转化",
    "算子与线性化",
    "概率方法与算两次",
    "反证与分类讨论",
]

PITFALL_TAGS = [
    "易错:边界与退化情形",
    "易错:定义域与分母为零",
    "易错:符号与方向",
    "易错:充分性与必要性混淆",
    "易错:隐含假设与越界推广",
    "易错:计数重复与漏算",
    "易错:极限与积分交换",
    "易错:计算精度与等价替换",
]

DIFFICULTY_TAGS = [
    "训练:基础热身",
    "训练:技巧进阶",
    "训练:压轴攻坚",
]

OUTCOME_LABELS = {
    "correct": "盲解完全正确",
    "different_valid_method": "盲解正确（不同有效解法）",
    "partial": "盲解部分做出（存在跳步或遗漏）",
    "incorrect": "盲解存在错误（对照修正）",
    "stuck": "盲解受阻（参考答案破局）",
}


def load_teaching_map(root, resources):
    """Load and verify all source-bound teaching records from catalog/teaching/*.json."""
    rmap = {r["id"]: r for r in resources}
    tdir = root / "catalog/teaching"
    tmap = {}
    if not tdir.exists():
        return tmap
    for path in sorted(tdir.glob("*.json")):
        pack = json.loads(path.read_text())
        rid = pack["resource_id"]
        resource = rmap.get(rid)
        if not resource:
            raise ValueError(f"Unknown teaching resource: {path.name} -> {rid}")
        if pack.get("source_sha256") != resource.get("sha256"):
            raise ValueError(f"Teaching source changed: {path.name}")
        srid = pack.get("solution_resource_id")
        if srid:
            sres = rmap.get(srid)
            if not sres or pack.get("solution_sha256") != sres.get("sha256"):
                raise ValueError(f"Teaching solution source changed: {path.name}")
        if pack.get("method") != "blind-then-verify":
            raise ValueError(f"Expected blind-then-verify provenance: {path.name}")
        for item in pack.get("questions", []):
            qid = item["id"]
            if qid in tmap:
                raise ValueError(f"Duplicate teaching record: {qid}")
            tmap[qid] = item
    return tmap


def apply_teaching(root, resources, questions, include_content=True):
    """Attach teaching tags (always) and full teaching breakdowns (when include_content=True)."""
    tmap = load_teaching_map(root, resources)
    questions = copy.deepcopy(questions)
    for q in questions:
        rec = tmap.get(q["id"])
        if not rec:
            q.setdefault("teaching_tags", [])
            continue
        an = rec["analysis"]
        difficulty = an["difficulty_tag"]
        methods = list(an.get("method_tags", []))
        pitfalls = list(an.get("pitfall_tags", []))
        topics = list(an.get("topic_tags", []))
        q["teaching_tags"] = [difficulty, *methods, *pitfalls]
        q["teaching_difficulty"] = difficulty
        q["teaching_methods"] = methods
        q["teaching_pitfalls"] = pitfalls
        q["teaching_topics"] = topics
        q["teaching_outcome"] = an["outcome"]
        q["has_teaching"] = True
        if include_content:
            q["teaching"] = {
                "problem_statement_zh": rec["blind_attempt"]["problem_statement_zh"],
                "blind_attempt": rec["blind_attempt"],
                "outcome": an["outcome"],
                "outcome_label": OUTCOME_LABELS.get(an["outcome"], an["outcome"]),
                "comparison_summary": an["comparison_summary"],
                "topic_tags": topics,
                "method_tags": methods,
                "pitfall_tags": pitfalls,
                "difficulty_tag": difficulty,
                "problem_decomposition": an["problem_decomposition"],
                "difficulties": an["difficulties"],
                "solution_breakdown": an["solution_breakdown"],
                "common_pitfalls": an["common_pitfalls"],
                "teaching_takeaway": an["teaching_takeaway"],
            }
    return questions


def write_teaching_records(root, resources, results):
    """Save batch results into source-bound catalog/teaching/<resource_id>.json and docs/teaching/*.md."""
    rmap = {r["id"]: r for r in resources}
    tdir = root / "catalog/teaching"
    tdir.mkdir(parents=True, exist_ok=True)
    grouped = {}
    for item in results:
        grouped.setdefault(item["resource_id"], []).append(item)

    for rid, items in grouped.items():
        res = rmap[rid]
        path = tdir / f"{rid}.json"
        existing = {}
        if path.exists():
            old_pack = json.loads(path.read_text())
            existing = {q["id"]: q for q in old_pack.get("questions", [])}
        for item in items:
            srid = item["solution_resource_id"]
            existing[item["id"]] = _clean_math_punctuation(item)
        ordered = sorted(existing.values(), key=lambda x: (str(x["number"]), x["id"]))
        srid0 = ordered[0]["solution_resource_id"]
        pack = {
            "resource_id": rid,
            "source_sha256": res["sha256"],
            "solution_resource_id": srid0,
            "solution_sha256": rmap[srid0]["sha256"],
            "method": "blind-then-verify",
            "questions": ordered,
        }
        path.write_text(json.dumps(pack, ensure_ascii=False, indent=2) + "\n")

    export_markdown_records(root, resources)


def export_markdown_records(root, resources):
    """Generate standalone human-readable markdown logs in docs/teaching/ and docs/TEACHING_RECORDS.md."""
    tmap = load_teaching_map(root, resources)
    docs_dir = root / "docs/teaching"
    docs_dir.mkdir(parents=True, exist_ok=True)
    by_contest = {}
    for rec in tmap.values():
        by_contest.setdefault(rec["contest"], []).append(rec)

    summary_lines = [
        "# 数学竞赛单题盲解与教学分析独立记录",
        "",
        "本目录及 `catalog/teaching/*.json` 记录在**只看原题（未看任何解答）**条件下的独立盲解尝试，以及随后对照参考解答所作的难点剖析、易错点分析、问题拆解、答案拆解与教学标签标注。",
        "",
        "| 赛事 | 学段 | 已记录题数 | 盲解完全正确 | 盲解不同有效解法 | 盲解部分做出 | 盲解有误/受阻 | 详细记录 |",
        "|---|---|---:|---:|---:|---:|---:|---|",
    ]

    for contest in sorted(by_contest):
        items = sorted(by_contest[contest], key=lambda x: (x["year"], str(x["number"]), x["id"]))
        levels = "/".join(sorted({it["level"] for it in items}))
        c_corr = sum(1 for it in items if it["analysis"]["outcome"] == "correct")
        c_diff = sum(1 for it in items if it["analysis"]["outcome"] == "different_valid_method")
        c_part = sum(1 for it in items if it["analysis"]["outcome"] == "partial")
        c_err = sum(1 for it in items if it["analysis"]["outcome"] in ("incorrect", "stuck"))
        summary_lines.append(
            f"| {contest} | {levels} | {len(items)} | {c_corr} | {c_diff} | {c_part} | {c_err} | [{contest}.md](teaching/{contest}.md) |"
        )

        md = [
            f"# {contest} 盲解复盘与竞赛教学记录",
            "",
            f"共记录 {len(items)} 道题（{levels}）。每题均按「只看原题盲解 → 对照参考解答复盘 → 问题与答案拆解 → 易错点分析」流程完成。",
            "",
        ]
        for it in items:
            an = it["analysis"]
            ba = it["blind_attempt"]
            tags = [an["difficulty_tag"], *an["method_tags"], *an["pitfall_tags"]]
            md.extend([
                f"## {it['title']}（`{it['id']}`）",
                "",
                f"- **学段**：{it['level']} · **盲解结果**：{OUTCOME_LABELS.get(an['outcome'], an['outcome'])}",
                f"- **教学标签**：{' / '.join(tags)}",
                f"- **知识专题**：{' / '.join(an['topic_tags'])}",
                "",
                "### 原题整理",
                "",
                ba["problem_statement_zh"],
                "",
                "### 1. 只看原题盲解尝试",
                "",
                f"**切入思路**：{ba['approach']}",
                "",
                "**推演步骤**：",
                *[f"- {s}" for s in ba["steps"]],
                "",
                f"**盲解结论**：{ba['final_answer']}",
                "",
            ])
            if ba.get("uncertainties"):
                md.append("**盲解时的疑虑/卡点**：" + "；".join(ba["uncertainties"]))
                md.append("")
            md.extend([
                "### 2. 对照答案复盘",
                "",
                an["comparison_summary"],
                "",
                "### 3. 困难点与破局关键",
                "",
                *[f"- **{d['title']}**：{d['detail']}" for d in an["difficulties"]],
                "",
                "### 4. 问题拆解（教学引导）",
                "",
                *[f"- **{p['step']}**：{p['detail']}" for p in an["problem_decomposition"]],
                "",
                "### 5. 答案拆解（逻辑骨架）",
                "",
                *[f"- **{s['step']}**（*动机*：{s['motivation']}）：{s['detail']}" for s in an["solution_breakdown"]],
                "",
                "### 6. 易错点分析",
                "",
                *[
                    f"- **{e['title']}**：常见错法——{e['mistake']}；错因——{e['why_wrong']}；避坑策略——{e['how_to_avoid']}"
                    for e in an["common_pitfalls"]
                ],
                "",
                f"**教学小结**：{an['teaching_takeaway']}",
                "",
                "---",
                "",
            ])
        (docs_dir / f"{contest}.md").write_text("\n".join(md))

    total = len(tmap)
    summary_lines.extend([
        "",
        f"合计已独立记录并核验 **{total}** 道竞赛题。",
        "",
    ])
    (root / "docs/TEACHING_RECORDS.md").write_text("\n".join(summary_lines))


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Ingest blind-solve teaching results and export markdown logs.")
    parser.add_argument("inputs", nargs="*", help="Batch JSON files to ingest")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    resources = json.loads((root / "catalog/resources.json").read_text())
    results = []
    for inp in args.inputs:
        items = json.loads(Path(inp).read_text())
        for item in items:
            if not item:
                continue
            an = item["analysis"]
            an["method_tags"] = [t for t in an.get("method_tags", []) if t in METHOD_TAGS]
            an["pitfall_tags"] = [t for t in an.get("pitfall_tags", []) if t in PITFALL_TAGS]
            if an.get("difficulty_tag") not in DIFFICULTY_TAGS:
                an["difficulty_tag"] = "训练:技巧进阶"
            results.append(item)
    if results:
        write_teaching_records(root, resources, results)
    else:
        export_markdown_records(root, resources)
    tmap = load_teaching_map(root, resources)
    print(f"Total teaching records stored: {len(tmap)}")


if __name__ == "__main__":
    main()

