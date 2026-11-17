# 调研与收集缺口

基准日：2026-11-16。只整理来源已有题解，不自行补写解法。

## 范围与命名

- 中国高中“复赛”按全国高中数学联赛层级收录，包含一试、加试；排除省级预赛、训练题、模拟卷。
- CMO 指中国决赛/冬令营，与加拿大同缩写赛事区分。2020–2022 中文资料来自第三方历史汇编，保留原始 PDF 页号。
- 本科采用 CMC（课程知识）、丘成桐（专业分科）、IMC 和 Putnam（综合证明）形成互补。建模竞赛需要数据包和长篇论文，暂不混入逐题型首版。
- 国际高中首选 IMO、EGMO：官方逐年资料清晰，便于与国内加试比较。USAMO、BMO、RMM 等为后续扩展。
- CMC 决赛按实际举行年与届次双重索引；疫情期间与初赛年错位。Putnam 2020 届于 2021 年举行，保留届次年。

## 来源路线

| 赛事 | 优先来源与本次实际路线 |
|---|---|
| IMO | [官方题目](https://www.imo-official.org/problems/)；主赛英文卷，不把 shortlist 当主卷 |
| EGMO | [官方逐届档案](https://www.egmo.org/egmos/)；英文、简体中文、解答分别记录 |
| IMC | [官方档案](https://imc-math.org.uk/?item=archive)逐日题目与解答 |
| 丘成桐 | [官方竞赛相关](https://www.yau-contest.com/lists-jxxg.html)公开笔试 ZIP，保留成员路径 |
| Putnam | [MAA](https://maa.org/maa-putnam-archive/)及[Kedlaya](https://kskedlaya.org/putnam-archive/)本次访问受限，采用[社区镜像](https://github.com/rpxgit/The-Putnam-Archive)，固定 `bd9408c626737480f9b76ab7e287dad6980154c8`，不标为官方下载 |
| CMC | [厦门大学课程站](https://gdjpkc.xmu.edu.cn/DocumentList.aspx?cID=22&dID=383)不少为 Flash 入口；批量 PDF 来自[社区整理](https://nhatchim37-sudo.github.io/cmc-preliminary-papers/)，2026 补充公开文章图 |
| 国内高中 | [中国数学会](https://www.cms.org.cn/)为赛事入口；实际题解补充自武汉教育云教师工作室、LaTeX 工作室、竞赛资讯转载，逐文件标记 third-party |

`cmathc.org.cn` 为资料聚合网站，不因域名或自称认定官方；本次发现的 `cmathc.cn` 连接超时，未依赖其内容证明完整度。

## 待补与待核

1. **2025 高中联赛**：已从[江苏招生考试网](https://m.jszs.com/n/474973.html)补入 A卷一试与加试题面、解答共16图。另一路预览 CDN 403；B卷仍缺可用原件。模拟卷已排除。
2. **CMO 2023**：现有第一天回忆版；[NUS 两日英文卷](https://sms.math.nus.edu.sg/Simo/CMO/CMO-2023_files/Problems.pdf)下载超时。中文定稿、两日整卷及解答待补。
3. **CMO 2026**：基准日未获得已发布试题；赛期需以主办方通知核实。
4. **CMC 2026**：初赛公开资料存在部分预览；第17届决赛高年级组有转载图，其余组别及官方完整定稿待补。
5. **国内图片卷**：OCR 漏题号、题解交错、同卷多个场次须人工修正；不能凭下载份数判齐。
6. **丘成桐**：官方笔试 ZIP 并非每年都提供答案；口试暂不收录。
7. **国际题解**：IMO 主卷未配到本次官方页面的解答，不以 shortlist 解答错配。Putnam 2026 基准日尚未举行。

“已下载”表示有文件与哈希，不表示整场/全版本/题解齐全。`partial-preview`、`partial-recall`、`needs-review` 分别标记不完整来源；候选切片与关键词标签不代表人工通过。优先级：补国内真题缺卷 → 修正边界 → 审核配对/标签 → 扩展赛事。
