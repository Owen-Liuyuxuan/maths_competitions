# 数据约定与复核

## 主数据

- `competitions.json`：稳定赛事 ID、学段、地区、范围和官网入口。
- `resources.json`：来源 URL、类型、年份、届次、题解角色、状态；下载成功后保存相对路径、页数、字节数、SHA-256。同 PDF 可按页范围索引多个场次，通过 `parent_resource_id` 关联。
- `questions.json`：资源外键、题号、主题、题面和解答切片。每个 segment 保存 1 起始页码、PDF point 坐标 `bbox=[x0,y0,x1,y1]` 和图像路径。

`role` 为 questions / solutions / combined / compilation；`authority` 为 official / university-mirror / community-mirror / third-party，仅表示下载来源，不认证数学正确性。页范围采用 0 起始半开区间；界面页码 1 起始。

## 原件与切分

直接下载 PDF 保留字节。文章图另存原始字节与 `provenance.json`（URL、路径、哈希）；组装 PDF 明示为派生资料。原图切片保持原样，正文另行读图重排。

英文 Problem/Question、中文题号和 Putnam A1–B6 按版式提取；Putnam 双栏按栏遍历。图片卷使用与原件哈希绑定的 OCR 行坐标。合卷出现明确“解/答案/解析”标题才尝试分离，否则显示待分界。检测不到可靠题号的资料保留整卷并进入复核队列。

`auto-candidate`、`keyword-suggestion` 均待人工核验；`section-with-subquestions` 是包含小题的大题组。检查 `review-queue.json`、`split-report.json`，重点复核非预期题数和多页末题。

## 人工覆盖

`catalog/anchor-overrides.json` 按资源 ID 提供：

```json
{"resource-id":{"reason":"对照原卷的依据","anchors":[{"number":"1","page":0,"y":120,"x":40}],"terminal":{"page":1,"y":700}}}
```

`terminal` 为最后一题结束位置，阻止末题吞入后续答案。`overrides.json` 以题目 ID 覆盖标签、状态等字段。人工通过才标 reviewed；抽样仅标 sample-reviewed。

验证脚本检查 ID、外键、原件哈希、页数、切片文件、坐标、题解赛事年份配对及公开版白名单。通过不代表数学内容正确、赛事全集完整或全部切片已视觉通过。

## 模型读图正文

`catalog/editorial/*.json` 保存按原图阅读的 `body_zh`、内容标签和可选题面／解答裁框，使用 `source_sha256` 绑定原件，`read_method=model-visual` 标明处理方式。`scripts/editorial.py` 在构建时应用这些编辑，不覆盖自动索引；未编辑题目的旧关键词标签不进入阅读界面。`replace_questions` 可重建漏题严重的整卷。

EGMO 按年份和题号合并语言版本，优先中文，保留旧英文 ID 的别名。题目正文不进入公开构建；公开版仍只含元数据和标签。界面不展示哈希和坐标，后台保留用于可追溯校验。

运行 `node scripts/check_formulas.cjs` 检查全部正文的公式与分隔符，运行 `python3 -m unittest discover -s scripts` 检查来源绑定、去重和无本地题面情况下的公开构建。
