# CMO 盲解复盘与竞赛教学记录

共记录 13 道题（高中）。每题均按「只看原题盲解 → 对照参考解答复盘 → 问题与答案拆解 → 易错点分析」流程完成。

## CMO 2021 试题 · 1（`cmo-2021-compilation-extract-questions-q1`）

- **学段**：高中 · **盲解结果**：盲解完全正确
- **教学标签**：训练:技巧进阶 / 对称与轮换 / 辅助线与几何变换 / 反证与分类讨论 / 易错:边界与退化情形 / 易错:充分性与必要性混淆
- **知识专题**：平面几何 / 轨迹问题 / 筝形与内切圆

### 原题整理

给定正数 \(a, b\) 和平面上的一条长度为 \(a\) 的线段 \(AB\)。设此平面上的两个动点 \(C, D\) 满足四边形 \(ABCD\) 是一个非退化的凸四边形，且 \(BC = CD = b\)，\(DA = a\)。已知存在圆 \(I\) 与四边形 \(ABCD\) 的四边都相切。求圆心 \(I\) 的轨迹。

### 1. 只看原题盲解尝试

**切入思路**：利用筝形 \(ABCD\) 的轴对称性与内切圆性质，结合三角形内角平分线定理将圆心 \(I\) 与动点 \(C\) 联系起来，说明 \(I\) 必在以线段 \(AB\) 上定分点 \(O\) 为圆心的定圆 \(\Gamma\) 上；再将四边形 \(ABCD\) 为非退化凸四边形的充要条件转化为 \(\triangle ABC\) 中 \(\angle BAC < 90^\circ\)、\(\angle BCA < 90^\circ\) 且 \(A, B, C\) 不共线，从而通过坐标验证与几何刻画确定圆心 \(I\) 在 \(\Gamma\) 上的精确弧段，并按 \(a=b\)、\(a<b\)、\(a>b\) 三种情况给出完整轨迹。

**推演步骤**：
- **分析几何结构与内切圆心位置**：由 \(AB = AD = a\) 及 \(CB = CD = b\) 可知 \(\triangle ABC \cong \triangle ADC\)。因为 \(ABCD\) 为非退化凸四边形，故 \(B, D\) 位于直线 \(AC\) 的两侧，\(D\) 为 \(B\) 关于直线 \(AC\) 的对称点，直线 \(AC\) 是四边形 \(ABCD\) 的对称轴，平分 \(\angle DAB\) 与 \(\angle DCB\)。由于圆 \(I\) 与凸四边形 \(ABCD\) 的四边都相切，圆心 \(I\) 必在四边形内部且位于四条内角平分线上，因此 \(I\) 在开线段 \(AC\) 上，且 \(BI\) 平分 \(\angle ABC\)。
- **求圆心 \(I\) 所在定圆 \(\Gamma\)**：在 \(\triangle ABC\) 中，\(BI\) 是 \(\angle ABC\) 的内角平分线，由角平分线定理得 \(\frac{AI}{IC} = \frac{AB}{BC} = \frac{a}{b}\)，即 \(\overrightarrow{AI} = \frac{a}{a+b}\overrightarrow{AC}\)。在线段 \(AB\) 上取定点 \(O\) 满足 \(\overrightarrow{AO} = \frac{a}{a+b}\overrightarrow{AB}\)（从而 \(AO = \frac{a^2}{a+b}\)，\(OB = \frac{ab}{a+b}\)），则 \(\overrightarrow{OI} = \overrightarrow{AI} - \overrightarrow{AO} = \frac{a}{a+b}\overrightarrow{BC}\)。因为 \(BC = b\)，所以 \(OI = \frac{ab}{a+b}\) 为定值，即 \(I\) 必在以 \(O\) 为圆心、\(R = \frac{ab}{a+b}\) 为半径且经过点 \(B\) 的圆 \(\Gamma\) 上。
- **刻画非退化凸四边形的充要条件**：反之，对 \(\Gamma\) 上任意一点 \(I\)，由 \(\overrightarrow{AC} = \frac{a+b}{a}\overrightarrow{AI}\) 确定点 \(C\)（自动满足 \(BC = b\)），并取 \(D\) 为 \(B\) 关于直线 \(AC\) 的对称点（自动满足 \(DA = a, CD = b\)）。当且仅当 \(A, B, C\) 不共线（即 \(I\) 不在直线 \(AB\) 上），且 \(BD\) 与直线 \(AC\) 的交点（即 \(B\) 在直线 \(AC\) 上的正投影 \(M\)）严格落在线段 \(AC\) 内部时，对角线 \(AC\) 与 \(BD\) 互相交于内点，\(ABCD\) 才是非退化凸四边形。在非退化 \(\triangle ABC\) 中，高线垂足 \(M\) 严格落在线段 \(AC\) 上等价于 \(\angle BAC < 90^\circ\) 且 \(\angle BCA < 90^\circ\)。此时由对称性及 \(I\) 在 \(\triangle ABC\) 角平分线 \(BI\) 上，\(I\) 到四边所在直线距离相等且垂足均落于四边内部，内切圆 \(I\) 必然存在。
- **精确求解轨迹范围（坐标验证）**：以 \(A\) 为原点、射线 \(AB\) 为 \(x\) 轴正方向建立直角坐标系，则 \(A(0,0)\)，\(B(a,0)\)，\(O\left(\frac{a^2}{a+b}, 0\right)\)，圆 \(\Gamma\) 的方程为 \(\left(x - \frac{a^2}{a+b}\right)^2 + y^2 = \frac{a^2 b^2}{(a+b)^2}\)，整理得 \(x^2 + y^2 = \frac{2a^2}{a+b}x + \frac{a^2(b^2 - a^2)}{(a+b)^2}\)。设 \(I(x,y)\)，则 \(C\left(\frac{a+b}{a}x, \frac{a+b}{a}y\right)\)。条件转化如下：（1）\(A, B, C\) 不共线等价于 \(y \neq 0\)；（2）\(\angle BAC < 90^\circ \iff \overrightarrow{AB} \cdot \overrightarrow{AC} > 0 \iff x > 0\)；（3）\(\angle BCA < 90^\circ \iff \overrightarrow{CA} \cdot \overrightarrow{CB} > 0 \iff x_C(x_C - a) + y_C^2 > 0\)，代入 \(C\) 的坐标与 \(\Gamma\) 的方程化简得 \((a+b)x + b^2 - a^2 > 0 \iff x > a - b\)。综上，\(I \in \Gamma\) 在轨迹中当且仅当 \(x > \max(0, a - b)\) 且 \(y \neq 0\)。
- **按 \(a, b\) 大小分类得出几何轨迹**：（1）若 \(a = b\)，则 \(O\left(\frac{a}{2},0\right)\)，\(R = \frac{a}{2}\)，\(\Gamma\) 是以 \(AB\) 为直径的圆，条件 \(x > 0\) 且 \(y \neq 0\) 仅除去 \(A, B\) 两点；（2）若 \(a < b\)，则 \(\max(0, a-b) = 0\)，过 \(A\) 作 \(AB\) 的垂线 \(l_A\)（即 \(x = 0\)），由 \(AO = \frac{a^2}{a+b} < R\) 知 \(l_A\) 与 \(\Gamma\) 交于两点 \(P_1, P_2\)，轨迹为 \(l_A\) 含 \(B\) 一侧的开优弧除去 \(B\)；（3）若 \(a > b\)，则 \(\max(0, a-b) = a - b\)，在 \(AB\) 上取 \(H(a-b, 0)\)（即 \(BH = b\)）并作垂线 \(l_H\)（即 \(x = a - b\)），因 \(\frac{a(a-b)}{a+b} < a - b < \frac{a^2}{a+b}\)，\(H\) 严格在 \(\Gamma\) 内部且在 \(O\) 的左侧，\(l_H\) 与 \(\Gamma\) 交于两点 \(Q_1, Q_2\)，轨迹为 \(l_H\) 含 \(B\) 一侧的开优弧除去 \(B\)。

**盲解结论**：在线段 \(AB\) 上取定点 \(O\) 使得 \(AO = \frac{a^2}{a+b}\)，\(OB = \frac{ab}{a+b}\)（即 \(AO : OB = a : b\)），并以 \(O\) 为圆心、\(R = OB = \frac{ab}{a+b}\) 为半径作圆 \(\Gamma\)（该圆经过点 \(B\)）。圆心 \(I\) 的轨迹按 \(a, b\) 的大小关系分为三种情况：

1. **当 \(a = b\) 时**：\(O\) 为 \(AB\) 的中点，圆心 \(I\) 的轨迹是以 \(AB\) 为直径的圆（除去 \(A, B\) 两点）。
2. **当 \(a < b\) 时**：过点 \(A\) 作 \(AB\) 的垂线 \(l_A\)，交圆 \(\Gamma\) 于两点 \(P_1, P_2\)（满足 \(AP_1 = AP_2 = \frac{a\sqrt{b^2 - a^2}}{a+b}\)）。圆心 \(I\) 的轨迹是圆 \(\Gamma\) 上位于直线 \(l_A\) 含点 \(B\) 一侧的开优弧 \(\widehat{P_1 B P_2}\) 除去点 \(B\)（即不含端点的两段圆弧 \(\widehat{P_1 B}\) 与 \(\widehat{P_2 B}\)）。
3. **当 \(a > b\) 时**：在线段 \(AB\) 上取点 \(H\) 使得 \(BH = b\)（即 \(AH = a - b\)），过点 \(H\) 作 \(AB\) 的垂线 \(l_H\)，交圆 \(\Gamma\) 于两点 \(Q_1, Q_2\)（满足 \(HQ_1 = HQ_2 = b\sqrt{\frac{a-b}{a+b}}\)）。圆心 \(I\) 的轨迹是圆 \(\Gamma\) 上位于直线 \(l_H\) 含点 \(B\) 一侧的开优弧 \(\widehat{Q_1 B Q_2}\) 除去点 \(B\)（即不含端点的两段圆弧 \(\widehat{Q_1 B}\) 与 \(\widehat{Q_2 B}\)）。

### 2. 对照答案复盘

Turn 1 的盲解结果完全正确，核心几何洞察与参考解答高度一致：均先由筝形 \(ABCD\) 的轴对称性推出内切圆心 \(I\) 在对角线 \(AC\) 上且满足 \(\frac{AI}{IC} = \frac{a}{b}\)，进而利用以 \(A\) 为位似中心、位似比为 \(\frac{a}{a+b}\) 的位似变换证明 \(I\) 位于定点 \(O\)（\(AO = \frac{a^2}{a+b}\)）为圆心、\(\frac{ab}{a+b}\) 为半径的定圆上，并将“非退化凸四边形”等价转化为 \(\triangle ABC\) 中 \(\angle BAC, \angle BCA\) 均为锐角（且 \(A,B,C\) 不共线）。两者的主要区别在于刻画圆弧范围的方式：参考解答在确定 \(\angle BAC, \angle BCA\) 为锐角后，利用正弦定理和 \(OI \parallel BC\) 直接以圆心角 \(\angle AOI \in (\arccos(\min(a,b)/\max(a,b)), \pi)\) 来表示两段开弧；Turn 1 则通过建立坐标系将两个锐角条件转化为 \(x > \max(0, a-b)\)，并用过 \(A\) 或 \(H\)（\(BH=b\)）的垂线截圆来给出几何描述，同时补充了轨迹充分性（逆向构造）及内切圆存在性的完整验证。两者所确定的轨迹完全相同。

### 3. 困难点与破局关键

- **从“内切圆心”到“定比位似”的视角转换**：题目同时涉及四个顶点和内切圆心 \(I\)，若直接用内切圆半径或三角坐标硬算会非常繁琐。需要敏锐地通过筝形的对称性，把 \(I\) 定位为 \(AC\) 与 \(\angle ABC\) 平分线的交点，从而借助角平分线定理得到定比 \(\frac{AI}{CI} = \frac{a}{b}\)，再构造位似把轨迹问题化归为定圆 \(C\) 的像。
- **凸四边形与非退化条件的精确充要转化**：学生往往只注意到 \(A, B, C\) 不能共线，却容易忽略“非退化凸四边形”还要求 \(\angle DAB < 180^\circ\) 与 \(\angle BCD < 180^\circ\)，这恰好对应于 \(\angle BAC < 90^\circ\) 与 \(\angle BCA < 90^\circ\)；并且在不同 \(a, b\) 大小关系下，这两个锐角条件谁构成有效边界需要分类厘清。

### 4. 问题拆解（教学引导）

- **识别对称结构，消元简化动点**：由固定长度 \(AB = DA = a\) 与 \(BC = CD = b\) 立即识别出四边形 \(ABCD\) 是以 \(AC\) 为对称轴的筝形（轴对称图形），从而先固定结构、消去自由点 \(D\)（\(D\) 必为 \(B\) 关于 \(AC\) 的对称点）。
- **关联内切圆心 \(I\) 与动点 \(C\)**：把未知的轨迹点 \(I\)（内切圆心）与更易刻画的动点 \(C\)（在以 \(B\) 为圆心、\(b\) 为半径的圆上运动）联系起来：由于 \(I\) 同时在对称轴 \(AC\) 和 \(\angle ABC\) 的角平分线上，直接用角平分线定理得到定比 \(\frac{AI}{IC} = \frac{a}{b}\)。
- **先求轨迹所在曲线，再截出有效范围**：先用定比位似求出 \(I\) 所在的完整圆 \(\omega\)，再回到题目“非退化凸四边形”的约束，把几何构型的边界条件转化为 \(\triangle ABC\) 的内角范围，进而确定圆 \(\omega\) 上真正有效的弧段。

### 5. 答案拆解（逻辑骨架）

- **利用轴对称与角平分线定理确定定比**（*动机*：寻找圆心 \(I\) 与唯一独立动点 \(C\) 之间的定量联系，为后续使用变换求轨迹铺路。）：由 \(AB = AD = a\) 和 \(BC = DC = b\) 知 \(ABCD\) 关于直线 \(AC\) 对称。内切圆心 \(I\) 在角平分线 \(AC\) 与 \(BI\) 的交点上，在 \(\triangle ABC\) 中由内角平分线定理得 \(\frac{AI}{CI} = \frac{AB}{BC} = \frac{a}{b}\)，即 \(\frac{AI}{AC} = \frac{a}{a+b}\)。
- **构造平行线与位似变换，锁定定圆 \(\omega\)**（*动机*：点 \(C\) 的轨迹是明显的定圆，利用“三角形一边上的定比平行截线”构造位似变换，直接将 \(C\) 的圆轨迹映为 \(I\) 的圆轨迹。）：过 \(I\) 作 \(OI \parallel BC\) 交 \(AB\) 于 \(O\)，则 \(\triangle AOI\) 与 \(\triangle ABC\) 关于点 \(A\) 位似，位似比为 \(\frac{a}{a+b}\)。因此 \(AO = \frac{a^2}{a+b}\) 为定点，\(OI = \frac{a}{a+b}BC = \frac{ab}{a+b}\) 为定值。由于 \(C\) 在圆 \((B, b)\) 上，故 \(I\) 必在圆 \(\omega(O, \frac{ab}{a+b})\) 上（该圆过点 \(B\)）。
- **将“非退化凸四边形”转化为锐角条件**（*动机*：必须检验“非退化凸四边形”这一限制会如何截断圆 \(\omega\)，不能遗漏凸性失效或退化的情形。）：因为 \(D\) 是 \(B\) 关于 \(AC\) 的对称点，\(AC \perp BD\) 且交点为 \(BD\) 中点 \(M\)（即 \(B\) 在 \(AC\) 上的射影）。\(ABCD\) 是非退化凸四边形当且仅当 \(A, B, C\) 不共线且 \(M\) 严格落在线段 \(AC\) 内部，也即 \(\angle BAC < 90^\circ\) 且 \(\angle BCA < 90^\circ\)（同时 \(A, B, C\) 不共线）。反之满足该条件时，对角线互相交于内点，内切圆也自然存在。
- **正弦定理结合 \(a, b\) 分类讨论，精确刻画弧段范围**（*动机*：将 \(\triangle ABC\) 中的角范围转化为圆 \(\omega\) 上的圆心角 \(\angle AOI\) 范围，从而完整刻画弧段，同时按 \(a, b\) 大小消除多解与越界问题。）：在 \(\triangle ABC\) 中由正弦定理 \(\frac{AB}{\sin\angle BCA} = \frac{BC}{\sin\angle BAC}\) 结合 \(OI \parallel BC\)（同位角/向量同向得 \(\angle AOI = \angle ABC\)）分三类讨论：（1）\(a > b\) 时，\(\angle BAC\) 必为锐角，限制来自 \(\angle BCA \in (0, \frac{\pi}{2})\)，此时 \(\sin\angle BAC = \frac{b}{a}\sin\angle BCA \in (0, \frac{b}{a})\)，临界 \(\angle BCA = \frac{\pi}{2}\) 对应 \(\angle ABC = \arccos\frac{b}{a}\)，故 \(\angle AOI \in (\arccos\frac{b}{a}, \pi)\)；（2）\(a = b\) 时，\(\omega\) 是以 \(AB\) 为直径的圆，\(\angle BAC, \angle BCA\) 恒为锐角，仅需排除 \(A, B\) 两点；（3）\(a < b\) 时，\(\angle BCA\) 必为锐角，限制来自 \(\angle BAC \in (0, \frac{\pi}{2})\)，此时 \(\sin\angle BCA = \frac{a}{b}\sin\angle BAC \in (0, \frac{a}{b})\)，临界 \(\angle BAC = \frac{\pi}{2}\) 对应 \(\angle ABC = \arccos\frac{a}{b}\)，故 \(\angle AOI \in (\arccos\frac{a}{b}, \pi)\)。对上述每种情况，图形关于 \(AB\) 轴对称，因此都对应圆 \(\omega\) 上关于 \(AB\) 对称的两段开弧（或除去 \(A, B\) 的整圆）。

### 6. 易错点分析

- **忽略凸性与非退化限制导致轨迹扩大**：常见错法——利用位似求出圆 \(\omega\) 后，直接认为圆心 \(I\) 的轨迹就是整个圆 \(\omega\)（或仅除去与直线 \(AB\) 的两个交点）。；错因——当 \(C\) 落在圆 \(\Omega\) 的另一侧时，虽然仍满足 \(DA=a, BC=CD=b\)，但可能出现 \(\angle BAD \ge 180^\circ\) 或 \(\angle BCD \ge 180^\circ\)，此时 \(ABCD\) 退化为三角形或变成凹四边形，不再符合“非退化的凸四边形”要求。；避坑策略——求轨迹题最后一步必须检查“逆命题（充分性）”与退化边界：逐一核对 \(A, B, C\) 共线以及 \(\angle BAD = 180^\circ\)、\(\angle BCD = 180^\circ\) 对应的临界位置，明确指出轨迹不含点 \(B\)（及 \(a=b\) 时的点 \(A\)）和弧的端点。
- **未分类讨论导致反三角函数越界或漏解**：常见错法——未按 \(a, b\) 大小关系分类讨论，误以为对所有 \(a, b\) 都可以用同一个角度公式（如统一写成 \(\arccos(b/a)\)）来刻画弧长范围。；错因——当 \(a < b\) 时 \(\frac{b}{a} > 1\)，\(\arccos(b/a)\) 无意义；实际上 \(a > b\) 时由 \(\angle BCA < 90^\circ\) 限制轨迹，\(a < b\) 时由 \(\angle BAC < 90^\circ\) 限制轨迹，二者起主导作用的约束不同。；避坑策略——对动点在圆周上的位置，先列出 \(\angle BAC < 90^\circ\) 与 \(\angle BCA < 90^\circ\) 两个不等式，再结合 \(a > b\)、\(a = b\)、\(a < b\) 三种大小关系分别判断究竟是哪一个角先达到 \(90^\circ\) 的临界值。
- **漏掉关于 \(AB\) 对称的另一半轨迹**：常见错法——只考虑 \(C\) 在线段 \(AB\) 的某一侧，最终只写出一段圆弧。；错因——题目给定平面上的线段 \(AB\)，动点 \(C, D\) 可以在平面内自由运动，将满足条件的图形关于直线 \(AB\) 翻折后依然满足全部条件，因此轨迹必关于直线 \(AB\) 对称，包含上下两段开弧。；避坑策略——在利用 \(\triangle ABC\) 求解动点轨迹时，时刻提醒自己 \(C, D\) 可以在直线 \(AB\) 两侧取点，关于 \(AB\) 轴对称的两支都要保留。

**教学小结**：处理含多个联动点与内切（外接）圆心的几何轨迹问题时，应先利用图形对称性与基本几何定理将所求点与核心动点通过定比（位似、旋转相似等几何变换）关联起来，确定轨迹所在的完整曲线后，再将题目的“非退化”与“凸性”限制精确转化为三角形内角或位置不等式，分情况截出真正有效的轨迹范围。

---

## 2024 CMO 试题与解答 · 1（`cmo-2024-both-days-combined-q1`）

- **学段**：高中 · **盲解结果**：盲解正确（不同有效解法）
- **教学标签**：训练:技巧进阶 / 归纳与递推 / 放缩与估值 / 极端原理 / 易错:边界与退化情形 / 易错:隐含假设与越界推广
- **知识专题**：取整函数 / 递归数列 / 周期数列

### 原题整理

1. 给定无理数 \(\alpha > 1\) 及正整数 \(L > \frac{\alpha^2}{\alpha - 1}\)，正整数数列 \(\{x_n\}\) 满足 \(x_1 > L\) 且对任意正整数 \(n\)，均有
\[
x_{n+1} = \begin{cases} \lfloor \alpha x_n \rfloor, & x_n \leqslant L \\ \lfloor \frac{x_n}{\alpha} \rfloor, & x_n > L \end{cases}
\]
（注：原题图片中分段式左侧印作 \(x_n = \dots\)，结合题意显然为 \(x_{n+1} = \dots\) 的印刷笔误。）
（1）证明：\(\{x_n\}\) 是最终周期的。
（2）证明：\(\{x_n\}\) 的最小正周期是一个与 \(x_1\) 无关的奇数。

### 1. 只看原题盲解尝试

**切入思路**：首先说明原题图片中递推式左侧印作 \(x_n\) 应为 \(x_{n+1}\) 的笔误。对第（1）问，利用当 \(x_n > L\) 时 \(x_{n+1} = \lfloor \frac{x_n}{\alpha} \rfloor < x_n\)，证明数列必在有限步内首次进入 \([1, L]\)；此后证明一旦 \(1 \le x_N \le L\)，对一切 \(n \ge N\) 均有 \(1 \le x_n \le \lfloor \alpha L \rfloor\)，由抽屉原理即得 \(\{x_n\}\) 最终周期。对第（2）问，令 \(M = \lfloor \frac{L+1}{\alpha} \rfloor\)。首先证明首次落入 \([1, L]\) 的项 \(x_N\) 满足 \(M \le x_N \le L\)，且由 \(L > \frac{\alpha^2}{\alpha - 1}\) 可推出 \(M > \frac{1}{\alpha - 1}\)，从而 \(M + 1 \le \lfloor \alpha M \rfloor \le L\)。接着利用 \(\alpha\) 的无理性证明核心引理：对任意整数 \(x \in [M+1, L]\)，有 \(\lfloor \alpha x \rfloor > L\) 且 \(\lfloor \frac{\lfloor \alpha x \rfloor}{\alpha} \rfloor = x - 1\)。由此任意 \(x_N \in [M, L]\) 必经过若干次两步一降 \(1\) 的过程到达 \(M\)；而从 \(M\) 出发，先跳至 \(M + k = \lfloor \alpha M \rfloor \in [M+1, L]\)（其中 \(k = \lfloor \alpha M \rfloor - M \ge 1\)），再经历 \(k\) 轮两步一降 \(1\) 回到 \(M\)。这给出了一个长度为 \(2k + 1\) 且元素两两互异的唯一极限环，故最小正周期为奇数 \(2(\lfloor \alpha M \rfloor - M) + 1\)，且仅与 \(\alpha, L\) 有关而与 \(x_1\) 无关。

**推演步骤**：
- 辨识原题图片中的条件与微小印刷笔误（将递推式左侧的 \(x_n\) 确认为 \(x_{n+1}\)）。
- 对第（1）问，验证每一步仍为正整数，并利用 \(x_n > L\) 时序列严格递减证明必存在首次满足 \(x_N \le L\) 的项 \(x_N\)。
- 用数学归纳法证明对一切 \(n \ge N\) 均有 \(1 \le x_n \le \lfloor \alpha L \rfloor\)，由抽屉原理与递推关系的确定性推出 \(\{x_n\}\) 最终周期。
- 对第（2）问，定义 \(M = \lfloor \frac{L+1}{\alpha} \rfloor\)，由 \(x_{N-1} \ge L + 1\) 得 \(M \le x_N \le L\)，并结合 \(L > \frac{\alpha^2}{\alpha - 1}\) 与 \(\alpha\) 的无理性证明 \(M + 1 \le \lfloor \alpha M \rfloor \le L\)。
- 利用 \(\alpha\) 为无理数证明：对任意整数 \(x \in [M+1, L]\)，都有 \(f(x) = \lfloor \alpha x \rfloor > L\) 且 \(f(f(x)) = \lfloor \frac{\lfloor \alpha x \rfloor}{\alpha} \rfloor = x - 1\)。
- 推出无论 \(x_1\) 如何选取，数列必在 \(x_N\) 之后经过 \(2(x_N - M)\) 步到达 \(M\)，随后进入长度 \(2k + 1\)（其中 \(k = \lfloor \alpha M \rfloor - M \ge 1\)）且 \(2k + 1\) 项两两互异的周期轨道，从而最小正周期为与 \(x_1\) 无关的奇数 \(2k + 1\)。
- 通过 Python 脚本对多种无理数 \(\alpha > 1\)、不同 \(L > \frac{\alpha^2}{\alpha - 1}\) 及不同初值 \(x_1 > L\) 进行数值验证，结果与公式 \(2(\lfloor \alpha M \rfloor - M) + 1\) 完全一致。

**盲解结论**：（1）**最终周期性证明**：
因为 \(\alpha > 1\)，\(L > \frac{\alpha^2}{\alpha - 1} = \alpha + 1 + \frac{1}{\alpha - 1} > \alpha\)，故对任意正整数 \(x\)：若 \(x \le L\)，则 \(\lfloor \alpha x \rfloor \ge \lfloor \alpha \rfloor \ge 1\)；若 \(x > L\)，则 \(\lfloor \frac{x}{\alpha} \rfloor \ge \lfloor \frac{L}{\alpha} \rfloor \ge 1\)。这与数列为正整数数列相一致。
当 \(x_n > L\) 时，由于 \(\alpha > 1\)，有 \(\frac{x_n}{\alpha} < x_n\)，从而 \(x_{n+1} = \lfloor \frac{x_n}{\alpha} \rfloor \le x_n - 1\)。因为 \(x_1 > L\) 且正整数严格递减不能无限持续保持大于 \(L\)，故必存在最小的正整数 \(N \ge 2\)，使得 \(x_N \le L\)（且 \(x_{N-1} > L\)）。
下面用数学归纳法证明：对一切 \(n \ge N\)，均有 \(1 \le x_n \le \lfloor \alpha L \rfloor\)。
- 当 \(n = N\) 时，\(1 \le x_N \le L \le \lfloor \alpha L \rfloor\) 成立；
- 假设 \(1 \le x_n \le \lfloor \alpha L \rfloor\)。若 \(x_n \le L\)，则 \(1 \le x_{n+1} = \lfloor \alpha x_n \rfloor \le \lfloor \alpha L \rfloor\)；若 \(L < x_n \le \lfloor \alpha L \rfloor\)，则 \(\frac{x_n}{\alpha} \le \frac{\alpha L}{\alpha} = L\)，从而 \(1 \le x_{n+1} = \lfloor \frac{x_n}{\alpha} \rfloor \le L \le \lfloor \alpha L \rfloor\)。

因此对所有 \(n \ge N\)，\(x_n\) 都取值于有限集 \(\{1, 2, \dots, \lfloor \alpha L \rfloor\}\)。由抽屉原理，存在 \(j > i \ge N\) 使得 \(x_i = x_j\)。因为递推关系中 \(x_{n+1}\) 由 \(x_n\) 唯一确定，归纳即得对一切 \(n \ge i\) 都有 \(x_{n+(j-i)} = x_n\)，故 \(\{x_n\}\) 是最终周期的。

（2）**最小正周期为与 \(x_1\) 无关的奇数**：
记迭代映射为 \(f(x) = \begin{cases} \lfloor \alpha x \rfloor, & x \le L, \\ \lfloor \frac{x}{\alpha} \rfloor, & x > L, \end{cases}\) 并令 \(M = \lfloor \frac{L+1}{\alpha} \rfloor\)。

**第一步：界定 \(x_N\) 与 \(M\) 的范围**。
由 \(N\) 的最小性可知 \(x_{N-1} \ge L + 1\)，于是
\[
x_N = \left\lfloor \frac{x_{N-1}}{\alpha} \right\rfloor \ge \left\lfloor \frac{L+1}{\alpha} \right\rfloor = M,
\]
故 \(M \le x_N \le L\)。又由 \(L > \frac{\alpha^2}{\alpha - 1}\) 可得
\[
M = \left\lfloor \frac{L+1}{\alpha} \right\rfloor > \frac{L+1}{\alpha} - 1 > \frac{L}{\alpha} - 1 > \frac{\alpha}{\alpha - 1} - 1 = \frac{1}{\alpha - 1}.
\]
由此 \((\alpha - 1)M > 1\)，即 \(\alpha M > M + 1\)，故 \(\lfloor \alpha M \rfloor \ge M + 1\)。另一方面，因为 \(\alpha\) 为无理数且 \(L + 1 \in \mathbb{Z}_{>0}\)，\(\frac{L+1}{\alpha}\) 不是整数，所以 \(M < \frac{L+1}{\alpha}\)，即 \(\alpha M < L + 1\)，从而 \(\lfloor \alpha M \rfloor \le L\)。综上，
\[
M + 1 \le \lfloor \alpha M \rfloor \le L.
\]

**第二步：建立区间 \([M+1, L]\) 上的两步降一引理**。
设整数 \(x\) 满足 \(M + 1 \le x \le L\)。由于 \(M = \lfloor \frac{L+1}{\alpha} \rfloor\) 且 \(\frac{L+1}{\alpha} \notin \mathbb{Z}\)，必有 \(x \ge M + 1 > \frac{L+1}{\alpha}\)，故 \(\alpha x > L + 1\)，从而
\[
f(x) = \lfloor \alpha x \rfloor \ge L + 1 > L.
\]
因为 \(x \ge 1\) 为整数且 \(\alpha\) 为无理数，\(\alpha x \notin \mathbb{Z}\)，所以 \(\alpha x - 1 < \lfloor \alpha x \rfloor < \alpha x\)。两边除以 \(\alpha > 1\)，结合 \(0 < \frac{1}{\alpha} < 1\)，得
\[
x - 1 < x - \frac{1}{\alpha} < \frac{\lfloor \alpha x \rfloor}{\alpha} < x.
\]
由于 \(x\) 为整数，上式说明 \(\frac{\lfloor \alpha x \rfloor}{\alpha}\) 严格介于相邻整数 \(x - 1\) 与 \(x\) 之间，因此
\[
f(f(x)) = \left\lfloor \frac{\lfloor \alpha x \rfloor}{\alpha} \right\rfloor = x - 1.
\]

**第三步：确定公共极限环并计算最小正周期**。
由 \(M \le x_N \le L\)，反复应用第二步的结论 \((x_N - M)\) 次（当 \(x_N = M\) 时应用 \(0\) 次），得
\[
x_{N + 2(x_N - M)} = M.
\]
令 \(k = \lfloor \alpha M \rfloor - M\)，由第一步知 \(k \ge 1\) 且 \(M + k = \lfloor \alpha M \rfloor \in [M+1, L]\)。现从 \(z_0 = M\) 出发追踪序列 \(z_{m+1} = f(z_m)\)：
- \(z_1 = f(M) = \lfloor \alpha M \rfloor = M + k \in [M+1, L]\)；
- 对 \(j = 1, 2, \dots, k\)，由于 \(z_{2j-1} = M + k - (j - 1) \in [M+1, L]\)，由第二步有 \(z_{2j} = f(z_{2j-1}) = \lfloor \alpha z_{2j-1} \rfloor > L\) 且 \(z_{2j+1} = f(z_{2j}) = z_{2j-1} - 1 = M + k - j\)。

当 \(j = k\) 时，\(z_{2k+1} = M = z_0\)。从而对一切 \(n \ge N_0 := N + 2(x_N - M)\)，数列 \(\{x_n\}\) 以 \(2k + 1\) 为周期循环取遍 \(z_0, z_1, \dots, z_{2k}\)。

最后验证 \(z_0, z_1, \dots, z_{2k}\) 两两互异：
- \(z_0 = M\)；
- \(z_1, z_3, \dots, z_{2k-1}\) 依次为 \(M+k, M+k-1, \dots, M+1\)，它们两两互异，且均属于 \([M+1, L]\)，严格大于 \(z_0\)；
- \(z_2, z_4, \dots, z_{2k}\) 均严格大于 \(L\)，故与前面所有 \(\le L\) 的项均不相同；且若对 \(1 \le i, j \le k\) 有 \(z_{2i} = z_{2j}\)，则 \(z_{2i+1} = f(z_{2i}) = f(z_{2j}) = z_{2j+1}\)，即 \(M + k - i = M + k - j\)，从而 \(i = j\)。

因此 \(z_0, z_1, \dots, z_{2k}\) 共 \(2k + 1\) 个数两两互异，故 \(\{x_n\}\) 的最小正周期恰为
\[
T = 2k + 1 = 2\left(\lfloor \alpha M \rfloor - M\right) + 1 = 2\left(\left\lfloor \alpha \left\lfloor \frac{L+1}{\alpha} \right\rfloor \right\rfloor - \left\lfloor \frac{L+1}{\alpha} \right\rfloor\right) + 1.
\]
显然 \(T\) 是一个奇数，且只依赖于 \(\alpha\) 与 \(L\)，与初项 \(x_1\) 无关。

**盲解时的疑虑/卡点**：原题图片中递推公式左侧印刷为 \(x_n = \begin{cases} \lfloor \alpha x_n \rfloor, & x_n \leqslant L \\ \lfloor \frac{x_n}{\alpha} \rfloor, & x_n > L \end{cases}\)，此处 \(x_n\) 显然是 \(x_{n+1}\) 的印刷笔误（若真为 \(x_n\)，则当 \(x_1 > L\) 时 \(x_1 = \lfloor x_1/\alpha \rfloor < x_1\) 矛盾）。数学推导本身已完全闭合且经过数值验证，无未解决的漏洞或边缘情形。

### 2. 对照答案复盘

盲解结果完全正确且严谨，采用了参考解答末尾提示的另一条经典路径（即通过证明区间 \([M+1, L]\) 上每两步数值减 \(1\)，直接确定了长度为 \(2(\lfloor \alpha M \rfloor - M) + 1\) 的唯一极限环）；参考解答则采用“有界归纳 + 极端原理（取不超过 \(L\) 的最大周期项 \(t\)）+ 二分集合 \(A, B\) 交替转移”的路线，两者本质相通，且盲解更显式地验明了条件 \(L > \frac{\alpha^2}{\alpha - 1}\) 对保证 \(\lfloor \alpha M \rfloor \ge M + 1\) 的作用（参考解答在此处略微简略）。

### 3. 困难点与破局关键

- **难点一：精确识别临界下界 \(M = \lfloor \frac{L+1}{\alpha} \rfloor\) 并用活条件 \(L > \frac{\alpha^2}{\alpha - 1}\)**：由 \(x_{N-1} \ge L + 1\) 得到下界 \(M = \lfloor \frac{L+1}{\alpha} \rfloor\) 是关键一步，但若仅停留在粗略估算，往往看不出与 \(\alpha, L\) 的精确关联。难点在于将 \(L > \frac{\alpha^2}{\alpha - 1}\) 转化为 \(M > \frac{1}{\alpha - 1}\)（即 \(\lfloor \alpha M \rfloor \ge M + 1\)），并利用 \(\alpha\) 的无理性辨明临界点 \(M\) 与 \(M + 1\) 在乘以 \(\alpha\) 后分别落在 \(L\) 的两侧。
- **难点二：刻画周期轨道结构以同时锁定“奇偶性”与“初值无关性”**：第（2）问既要证最小正周期是奇数，又要证与 \(x_1\) 无关。学生容易只用抽屉原理停留在周期存在性上，难以发现“状态 \(M\) 是所有轨道的必经汇合点”，也容易忽略如何利用 \(A, B\) 两个状态集合的交替转移（标答）或两步降 \(1\) 轨道（另一解法）来锁定周期奇偶性。

### 4. 问题拆解（教学引导）

- **步骤一：分析分段递推的“放大-缩小”动力学机制**：递推规则在阈值 \(L\) 两侧分别为“乘 \(\alpha\) 取整”（放大）和“除以 \(\alpha\) 取整”（缩小）。由于 \(x_1 > L\)，数列先不断缩小直至首次出现 \(\le L\) 的项；一旦进入 \([1, L]\)，放大后最多到达 \(\lfloor \alpha L \rfloor\)，之后又会被拉回 \([1, L]\)，这就是第（1）问有界性与最终周期性的直观来源。
- **步骤二：追踪首次跨过阈值 \(L\) 后的下界，并解码条件 \(L > \frac{\alpha^2}{\alpha - 1}\)**：从大于 \(L\) 首次跳回 \(\le L\) 的一步最值得关注：因为前一项至少是 \(L + 1\)，所以新项至少是 \(M = \lfloor \frac{L+1}{\alpha} \rfloor\)。同时检查条件 \(L > \frac{\alpha^2}{\alpha - 1}\)，变形得 \(\frac{L}{\alpha} - 1 > \frac{1}{\alpha - 1}\)，这恰好提示下界 \(M\) 满足 \((\alpha - 1)M > 1\)，即 \(\lfloor \alpha M \rfloor > M\)，排除了不动点的可能。
- **步骤三：从“奇数”与“与 \(x_1\) 无关”逆向猜测轨道结构**：既然最小正周期与 \(x_1\) 无关，几乎必然存在某个“瓶颈元素”对所有初值都在周期中出现，自然怀疑这个元素就是下界 \(M = \lfloor \frac{L+1}{\alpha} \rfloor\)；而周期为奇数，暗示着轨道在 \(L\) 以下与 \(L\) 以上几乎交替出现，只在到达 \(M\) 处发生一次“连续留在 \(\le L\) 区域”的跃迁。

### 5. 答案拆解（逻辑骨架）

- **步骤一：先降后界，归纳锁定不变有限集并证最终周期性**（*动机*：第（1）问需要证明有界性；进一步把下界直接缩紧到 \(\lfloor \frac{L+1}{\alpha} \rfloor\)，能同时为第（2）问铺路。）：由于 \(x_1 > L\) 且当 \(x_n > L\) 时 \(x_{n+1} = \lfloor \frac{x_n}{\alpha} \rfloor \le x_n - 1\)，数列必在有限步内首次落入 \([1, L]\)。去掉前面若干项后，不妨设首项 \(x_1\) 即为第一个不超过 \(L\) 的项（其前项 \(x_0 \ge L + 1\)）。于是 \(\lfloor \frac{L+1}{\alpha} \rfloor \le x_1 \le L < \alpha L\)。利用归纳法验证：若 \(\lfloor \frac{L+1}{\alpha} \rfloor \le x_k \le L\)，则 \(x_{k+1} = \lfloor \alpha x_k \rfloor\) 满足 \(\lfloor \frac{L+1}{\alpha} \rfloor \le x_k \le x_{k+1} \le \lfloor \alpha L \rfloor < \alpha L\)（这里用到 \(L > \frac{\alpha^2}{\alpha - 1}\) 保证下界处有 \(\lfloor \alpha x_k \rfloor > x_k\)）；若 \(L + 1 \le x_k < \alpha L\)，则 \(\lfloor \frac{L+1}{\alpha} \rfloor \le \lfloor \frac{x_k}{\alpha} \rfloor = x_{k+1} \le L < \alpha L\)。因区间 \([\lfloor \frac{L+1}{\alpha} \rfloor, \alpha L)\) 中整数有限，且后项由前项唯一确定，故 \(\{x_n\}\) 最终周期。
- **步骤二：截去非周期首部，依极大值 \(t\) 划分状态集 \(A\) 与 \(B\)**（*动机*：要证明最小正周期与 \(x_1\) 无关且为奇数，直接追踪每一项的数值较繁琐，参考解答改用极端原理取定“上边界 \(t\)”，将所有周期项划入两个互斥集合 \(A\)（不大于 \(L\)）与 \(B\)（大于 \(L\)）来分析转移规律。）：去掉前周期部分，不妨设 \(\{x_n\}\) 已经是纯周期数列。记 \(M = \lfloor \frac{L+1}{\alpha} \rfloor\)，并由极端原理取周期数列中不超过 \(L\) 的最大项为 \(t\)。定义 \(A = \{a \in \mathbb{N}^* \mid M \le a \le t\}\)，\(B = \{b \in \mathbb{N}^* \mid L + 1 \le b < \alpha t\}\)。同理归纳可知周期项全部落在 \(A \cup B\) 中（因为从 \(A\) 出发至多到 \(\lfloor \alpha t \rfloor < \alpha t\)，从 \(B\) 出发除以 \(\alpha\) 取整严格小于 \(t\)）。
- **步骤三：建立 \(A\)、\(B\) 之间的转移法则并锁定 \(M \to t\) 的唯一性**（*动机*：找出转移图中的“唯一非交替边”：只有从 \(M\) 到 \(t\) 是留在 \(A\) 内部的一步，其余时刻都在 \(A\) 与 \(B\) 之间严格来回跳跃。）：利用 \(\alpha\) 的无理性可得 \(\lfloor \alpha M \rfloor < L + 1\)（即 \(\lfloor \alpha M \rfloor \le L\)）且 \(\lfloor \alpha (M + 1) \rfloor \ge L + 1\)。由此：
（1）若 \(x_i \in A\) 且 \(x_i \neq M\)，则 \(x_i \ge M + 1\)，故 \(x_{i+1} = \lfloor \alpha x_i \rfloor \ge L + 1\)，又 \(x_i \le t \implies x_{i+1} < \alpha t\)，所以 \(x_{i+1} \in B\)；
（2）若 \(x_i \in B\)，则 \(L + 1 \le x_i < \alpha t \implies x_{i+1} = \lfloor \frac{x_i}{\alpha} \rfloor < t\)，故 \(x_{i+1} \in A \setminus \{t\}\)；
（3）既然 \(t\) 在周期中出现，而上述两类转移都不可能到达 \(t\)（需注意由 \(L > \frac{\alpha^2}{\alpha - 1}\) 知 \(M > \frac{1}{\alpha - 1}\)，故 \(\lfloor \alpha M \rfloor \ge M + 1\)，从而 \(t \ge \lfloor \alpha M \rfloor > M\)），因此 \(t\) 的前一项必为 \(M\)，即当 \(x_i = M\) 时 \(x_{i+1} = t \in A\)。
- **步骤四：通过相邻极大项 \(t\) 之间的交替步数证明最小正周期为奇数且与 \(x_1\) 无关**（*动机*：用相邻两次 \(t\) 之间的状态交替计数奇偶性，并用必经点 \(M\) 说明周期与初值无关。）：在纯周期数列中取相邻两次出现 \(t\) 的下标 \(p < q\)（即 \(x_p = x_q = t\) 且在 \(p, q\) 之间不再出现 \(t\)）。因为 \(t\) 在周期中只从 \(M\) 跳来，从 \(x_p = t \in A \setminus \{M\}\) 出发，必有 \(x_{p+1} \in B, x_{p+2} \in A, x_{p+3} \in B, \dots\) 严格交替；直到回到 \(x_q = t\) 的前一项必为 \(x_{q-1} = M \in A\)。于是下标差 \((q - 1) - p\) 为偶数，故最小正周期 \(T = q - p\) 为奇数（注：相邻两次 \(t\) 的间距恰为一个最小正周期，因整个轨道被 \(t\) 到下一次 \(t\) 唯一决定）。同时，由于 \(M = \lfloor \frac{L+1}{\alpha} \rfloor\) 必然在周期中出现（即 \(x_{q-1} = M\)），而后续所有项均由 \(M\) 唯一确定，因此整个周期轨道以及最小正周期 \(T\) 都只与 \(\alpha, L\) 有关，与初项 \(x_1\) 完全无关。

（补充对比思路：也可不用最大项 \(t\)，直接证明对一切 \(x \in [M+1, L]\) 有 \(f(x) > L\) 且 \(f(f(x)) = x - 1\)，从而无论 \(x_1\) 为何值必降到 \(M\)，且 \(M \to M + k \to \dots \to M\) 直接给出最小正周期的显式表达式 \(2(\lfloor \alpha M \rfloor - M) + 1\)。）

### 6. 易错点分析

- **忽视无理性导致取整恒等式出错**：常见错法——忽略 \(\alpha\) 为无理数及 \(\alpha > 1\) 的条件，直接误以为 \(\lfloor \frac{\lfloor \alpha x \rfloor}{\alpha} \rfloor = x\) 或对任意 \(\alpha\) 都等于 \(x - 1\)。；错因——若 \(\alpha\) 为整数或有理数使得 \(\alpha x \in \mathbb{Z}\)，则 \(\lfloor \alpha x \rfloor = \alpha x\)，从而 \(\lfloor \frac{\lfloor \alpha x \rfloor}{\alpha} \rfloor = x\) 而非 \(x - 1\)，整个“两步降 \(1\)”或状态转移结构将彻底改变。；避坑策略——严格写明：对整数 \(x \ge 1\) 与无理数 \(\alpha > 1\)，\(\alpha x \notin \mathbb{Z}\)，故 \(\alpha x - 1 < \lfloor \alpha x \rfloor < \alpha x\)，两边除以 \(\alpha > 1\) 得 \(x - 1 < x - \frac{1}{\alpha} < \frac{\lfloor \alpha x \rfloor}{\alpha} < x\)，从而必有 \(\lfloor \frac{\lfloor \alpha x \rfloor}{\alpha} \rfloor = x - 1\)。
- **未验证最小正周期不可能退化为 1（忽略下界条件）**：常见错法——漏证 \(\lfloor \alpha M \rfloor > M\)（其中 \(M = \lfloor \frac{L+1}{\alpha} \rfloor\)），导致可能出现不动点 \(M \mapsto M\)。；错因——若没有 \(L > \frac{\alpha^2}{\alpha - 1}\)，当 \(\alpha \in (1, 2)\) 且 \(M\) 较小时完全可能出现 \(\lfloor \alpha M \rfloor = M\)，此时参考解答中“除 \(M\) 外 \(A\) 中其余元素都跳入 \(B\)”及 \(t > M\)、或“隔项减 \(1\) 回到 \(M\) 后不再停留”都将失效，最小正周期可能变成 \(1\) 甚至陷入不同的不动点。；避坑策略——紧盯 \(L > \frac{\alpha^2}{\alpha - 1}\)，由此推出 \(M = \lfloor \frac{L+1}{\alpha} \rfloor > \frac{L+1}{\alpha} - 1 > \frac{L}{\alpha} - 1 > \frac{1}{\alpha - 1}\)，进而得到 \(\alpha M > M + 1\)，严格保证 \(\lfloor \alpha M \rfloor \ge M + 1\)。
- **混淆“存在奇数周期”与“最小正周期为奇数”**：常见错法——只证明数列有某个奇数周期（如某两个相等项之间的步数为奇数），就直接断言“最小正周期为奇数”。；错因——一个最小正周期为 \(T\) 的数列，其任意正整数倍 \(mT\) 都是周期（例如当 \(T = 3\) 时 \(6\) 是偶数周期，当 \(T = 2\) 时不存在奇数周期；更重要的是，若只证得某两相同项间距为奇数，还不能直接排除是最小正周期的奇数倍，不过奇数之因数必为奇数，这一点也需说清：若最小正周期 \(T\) 整除某个奇数 \(q - p\)，则 \(T\) 必为奇数；但若要证“与 \(x_1\) 无关”，仍需说明进入同一极限环）。；避坑策略——在标答法中，先利用周期性取 \(x_p = x_q = t\) 为相邻两次出现最大项 \(t\) 的位置，从而保证开区间 \((p, q)\) 内不再出现 \(t\)，才能断定 \(x_{p+1}, \dots, x_{q-1}\) 严格在 \(B, A\) 间交替且必在 \(x_{q-1} = M\) 结束；在直接算周期法中，则需显式验证周期内 \(2k+1\) 项两两互异。

**教学小结**：处理分段取整递推数列时，一要紧盯阈值两侧的单调与跨界估算（特别注意无理性对严格不等式的保证），二要善于从临界状态（如 \(\lfloor \frac{L+1}{\alpha} \rfloor\)）或极端状态（如周期极大值 \(t\)）入手将复杂数值轨迹转化为清晰的状态机交替转移。

---

## 2024 CMO 试题与解答 · 2（`cmo-2024-both-days-combined-q2`）

- **学段**：高中 · **盲解结果**：盲解完全正确
- **教学标签**：训练:技巧进阶 / 辅助线与几何变换 / 局部-整体转化 / 易错:边界与退化情形 / 易错:符号与方向 / 易错:隐含假设与越界推广
- **知识专题**：三角形的心与鸡爪定理 / 圆内接四边形与直径 / 三线共点与位似

### 原题整理

给定 \(\triangle ABC\)，点 \(I\) 是 \(\triangle ABC\) 的内心，点 \(L\)、\(M\)、\(N\) 分别是 \(AI\)、\(AC\)、\(CI\) 的中点，线段 \(AM\) 上的一点 \(D\) 满足 \(BC = BD\)，\(\triangle ABD\) 的内切圆分别与 \(AD\)、\(BD\) 切于点 \(E\)、\(F\)，已知点 \(J\) 为 \(\triangle AIC\) 的外心，\(\omega\) 为 \(\triangle JMD\) 的外接圆，直线 \(MN\) 再次交 \(\omega\) 于点 \(P\)，直线 \(JL\) 再次交 \(\omega\) 于点 \(Q\)，证明：直线 \(PQ\)、\(LN\)、\(EF\) 三线共点。

### 1. 只看原题盲解尝试

**切入思路**：先定位三条直线的公共点：取线段 \(ID\) 的中点 \(X\)。由于 \(L\)、\(N\) 分别是 \(AI\)、\(CI\) 的中点，且 \(D\) 在 \(AC\) 上，\(X\) 显然在直线 \(LN\) 上。接着证明 \(X\) 也在直线 \(EF\) 与直线 \(PQ\) 上：
1. 证明 \(X \in EF\)：利用 \(BC=BD\) 得 \(\triangle BCD\) 为等腰三角形，从而 \(\angle DEF = \frac{C}{2}\)。设 \(\triangle ABC\) 的内切圆与 \(AC\) 切于 \(E_0\)，计算 \(X\) 在 \(AC\) 上的投影 \(X'\) 到 \(E\) 的有向距离，发现 \(EX' = \frac{E_0 C}{2}\)，结合 \(XX' = \frac{r}{2}\) 即可由正切值相等及同侧方向证明 \(X \in EF\)。
2. 证明 \(X \in PQ\)：由 \(J\) 为 \(\triangle AIC\) 外心知 \(JM \perp AC\)、\(JL \perp AI\)、\(MN \parallel AI\)，故 \(JD\) 为 \(\omega\) 的直径。先验证 \(P, Q, J, M\) 四点互异（即使 \(D \in JL\) 导致 \(Q=D\) 亦然），再用有向角导角证明 \(PQ \parallel AB\)；另一方面，由 \(JD\) 为直径知 \(Q\) 是 \(D\) 在 \(JL\) 上的正投影，利用以 \(AI\) 方向及垂直方向为基的向量分解，直接算出 \(\overrightarrow{QX}\) 与 \(\overrightarrow{AB}\) 同向，即 \(QX \parallel AB\)，从而 \(P, Q, X\) 共线。

**推演步骤**：
- 确定非退化条件：\(D \neq A, M\)（故 \(0 < AD < \frac{AC}{2}\)）；由 \(BC=BD\) 得 \(\angle BDC = C < 90^\circ\)，\(\angle ADB = 180^\circ - C\)。由 \(J\) 为 \(\triangle AIC\) 外心及 \(\angle AIC > 90^\circ\)，得 \(J\) 与 \(I\) 在 \(AC\) 异侧，且 \(JM \perp AC\)、\(JL \perp AI\)、\(MN \parallel AI\)、\(LN \parallel AC\)。
- 取 \(ID\) 的中点 \(X\)。利用中位线或以 \(I\) 为位似中心、位似比为 \(\frac{1}{2}\) 的位似变换，直接得出 \(X \in LN\)。
- 证明 \(X \in EF\)：设 \(\triangle ABC\) 内切圆切 \(AC\) 于 \(E_0\)，\(X\) 在 \(AC\) 上的投影为 \(X'\)（即 \(E_0 D\) 中点）。计算有向距离得 \(EX' = AX' - AE = \frac{a+b-c}{4} = \frac{E_0 C}{2} > 0\)，且 \(XX' = \frac{r}{2}\)，从而 \(\tan\angle XEX' = \frac{r}{E_0 C} = \tan\frac{C}{2}\)。又由 \(\angle EDF = 180^\circ - C\) 及 \(DE=DF\) 得 \(\angle DEF = \frac{C}{2}\)，且 \(F, X\) 在 \(AC\) 同侧、\(\overrightarrow{ED}\) 与 \(\overrightarrow{AC}\) 同向，故 \(X \in EF\)。
- 验证圆 \(\omega\) 上各点的位置关系：由 \(\angle JMD = 90^\circ\) 知 \(JD\) 为 \(\omega\) 直径；通过内积与投影说明 \(MN\) 不切 \(\omega\) 于 \(M\)、\(JL\) 不切 \(\omega\) 于 \(J\)，从而 \(P \notin \{J, M, D\}\)、\(Q \neq J, M\)（注意当 \(D \in JL\) 时允许 \(Q = D\)），且 \(Q\) 必为 \(D\) 在 \(JL\) 上的正投影；再比较到 \(AI\) 的距离得出 \(Q \notin MN\)，故 \(P \neq Q\)。
- 证明 \(PQ \parallel AB\)：在 \(\omega\) 上对互异四点 \(P, Q, J, M\) 使用有向角（模 \(180^\circ\)），由 \(\measuredangle(PQ, JL) = \measuredangle(MN, JM)\) 并结合 \(JL \perp AI\)、\(JM \perp AC\)、\(\angle BAI = \angle IAC\) 推出 \(\measuredangle(PQ, AC) = \measuredangle(AB, AC) \pmod{180^\circ}\)，即 \(PQ \parallel AB\)。
- 证明 \(QX \parallel AB\)：以 \(\overrightarrow{AI}\) 方向及指向 \(C\) 一侧的法方向为正交基，写出 \(\overrightarrow{AD}\)、\(\overrightarrow{AQ}\)（\(D\) 在 \(JL\) 上投影）和 \(\overrightarrow{AX}\)（\(ID\) 中点），相减得 \(\overrightarrow{QX} = \frac{AD}{2}(\cos\frac{A}{2}\,\mathbf{u} - \sin\frac{A}{2}\,\mathbf{v})\)，恰沿 \(\overrightarrow{AB}\) 方向，故 \(QX \parallel AB\)，从而 \(X \in PQ\)。综合三步即证 \(PQ, LN, EF\) 共点于 \(X\)。

**盲解结论**：取线段 \(ID\) 的中点 \(X\)，以下证明直线 \(PQ\)、\(LN\)、\(EF\) 均经过点 \(X\)，从而三线共点。

**一、基本性质与非退化说明**

记 \(\triangle ABC\) 的三边长分别为 \(a = BC\)、\(b = AC\)、\(c = AB\)，半周长 \(s = \frac{a+b+c}{2}\)，内切圆半径为 \(r\)。
由 \(\triangle ABD\) 存在内切圆知 \(D \neq A\)；由 \(\omega\) 是 \(\triangle JMD\) 的外接圆知 \(D \neq M\)。因此 \(D\) 严格在线段 \(AM\) 内部，即 \(0 < AD < \frac{b}{2}\)。
因为 \(D\) 在线段 \(AC\) 上且 \(BD = BC\)（\(D \neq C\)），在等腰 \(\triangle BCD\) 中有 \(\angle BDC = \angle BCD = C\)（故 \(C < 90^\circ\)），从而 \(\angle ADB = 180^\circ - C\)。

因为 \(J\) 是 \(\triangle AIC\) 的外心，所以 \(JA = JI = JC\)。又 \(\angle AIC = 90^\circ + \frac{B}{2} > 90^\circ\)，故 \(J\) 与 \(I\)（以及 \(B\)）在直线 \(AC\) 的异侧。
由 \(L\)、\(M\)、\(N\) 分别是 \(AI\)、\(AC\)、\(CI\) 的中点，立得：
- \(JM \perp AC\)（因为 \(JA = JC\)）；
- \(JL \perp AI\)（因为 \(JA = JI\)）；
- \(MN \parallel AI\)，\(LN \parallel AC\)。

**二、证明 \(X\) 在直线 \(LN\) 上**

因为 \(L\)、\(N\)、\(X\) 分别是线段 \(IA\)、\(IC\)、\(ID\) 的中点，且 \(A\)、\(D\)、\(C\) 共线，在以 \(I\) 为位似中心、位似比为 \(\frac{1}{2}\) 的位似变换下，直线 \(AC\) 映为直线 \(LN\)，点 \(D\) 映为点 \(X\)，故 \(X\) 在直线 \(LN\) 上。

**三、证明 \(X\) 在直线 \(EF\) 上**

设 \(\triangle ABC\) 的内切圆与边 \(AC\) 切于点 \(E_0\)，则 \(E_0\) 在线段 \(AC\) 上，\(IE_0 \perp AC\)，\(IE_0 = r\)，\(AE_0 = s - a = \frac{b+c-a}{2}\)，且 \(E_0 C = s - c = \frac{a+b-c}{2} > 0\)。在 \(\mathrm{Rt}\triangle IE_0 C\) 中，\(\angle ICE_0 = \frac{C}{2}\)，故
\[
\tan\frac{C}{2} = \frac{IE_0}{E_0 C} = \frac{r}{E_0 C}.
\]

设 \(X\) 在直线 \(AC\) 上的正投影为 \(X'\)。因为 \(X\) 是 \(ID\) 的中点且 \(D \in AC\)，所以 \(X'\) 是线段 \(E_0 D\) 的中点，且 \(X\) 与 \(I\)（及 \(B\)）在直线 \(AC\) 的同侧，满足 \(XX' = \frac{1}{2}IE_0 = \frac{r}{2}\)。

在 \(\triangle ABD\) 中，内切圆与 \(AD\)、\(BD\) 分别切于 \(E\)、\(F\)，故 \(E\) 严格在线段 \(AD\) 内部，\(F\) 严格在线段 \(BD\) 内部（在 \(AC\) 的 \(B\) 同侧），且
\[
AE = \frac{AD + AB - BD}{2} = \frac{AD + c - a}{2}.
\]
沿射线 \(\overrightarrow{AC}\) 方向度量从 \(A\) 出发的有向距离：
\[
AX' - AE = \frac{AE_0 + AD}{2} - AE = \frac{\frac{b+c-a}{2} + AD - (AD + c - a)}{2} = \frac{a+b-c}{4} = \frac{E_0 C}{2} > 0.
\]
因此 \(X'\) 位于点 \(E\) 沿 \(\overrightarrow{AC}\) 方向的正前方，且 \(EX' = \frac{E_0 C}{2}\)。在 \(\mathrm{Rt}\triangle EX'X\) 中，
\[
\tan\angle XEX' = \frac{XX'}{EX'} = \frac{r/2}{E_0 C/2} = \frac{r}{E_0 C} = \tan\frac{C}{2},
\]
故 \(\angle XEX' = \frac{C}{2}\)。

另一方面，在 \(\triangle ABD\) 中，\(DE = DF\) 且 \(\angle EDF = \angle ADB = 180^\circ - C\)，所以
\[
\angle DEF = \frac{180^\circ - (180^\circ - C)}{2} = \frac{C}{2}.
\]
由于 \(E\) 在线段 \(AD\) 内部，射线 \(\overrightarrow{ED}\) 与 \(\overrightarrow{AC}\) 同向；又 \(F\) 与 \(X\) 均在直线 \(AC\) 的 \(B\) 同侧，且 \(\angle DEF = \angle XEX' = \frac{C}{2}\)，故射线 \(\overrightarrow{EF}\) 与射线 \(\overrightarrow{EX}\) 重合，即点 \(X\) 在直线 \(EF\) 上。

**四、证明 \(X\) 在直线 \(PQ\) 上**

1. **\(JD\) 为 \(\omega\) 的直径及 \(P, Q, J, M\) 四点互异**
   因为 \(JM \perp AC\) 且 \(D \in AM\)（\(D \neq M\)），所以 \(\angle JMD = 90^\circ\)，\(JD\) 是 \(\omega\) 的直径。
   - **证明 \(P \notin \{J, M, D\}\)**：因为 \(MN \parallel AI\) 且 \(AI \nparallel AC\)，直线 \(MN\) 与 \(AC\) 仅交于 \(M\)，所以 \(D \notin MN\)，故 \(P \neq D\)；又 \(JM \perp AC\) 而 \(AI \nparallel AC\)，所以 \(J \notin MN\)，故 \(P \neq J\)。若 \(P = M\)，则 \(MN\) 与 \(\omega\) 相切于 \(M\)，从而 \(MN \perp MO\)（其中 \(O\) 为 \(JD\) 中点，即 \(\omega\) 的圆心）。但 \(\overrightarrow{MO} = \frac{1}{2}(\overrightarrow{MJ} + \overrightarrow{MD})\)，\(\overrightarrow{MN} = \frac{1}{2}\overrightarrow{AI}\)。由于 \(J\) 与 \(I\) 在 \(AC\) 异侧，且 \(\angle IAC = \frac{A}{2} < 90^\circ\)，有 \(\overrightarrow{MJ} \cdot \overrightarrow{AI} < 0\)；又 \(D\) 在线段 \(AM\) 上，\(\overrightarrow{MD}\) 与 \(\overrightarrow{AC}\) 反向而 \(\overrightarrow{AI}\) 在 \(\overrightarrow{AC}\) 上的投影为正，故 \(\overrightarrow{MD} \cdot \overrightarrow{AI} < 0\)。从而 \(\overrightarrow{MO} \cdot \overrightarrow{MN} < 0\)，矛盾，因此 \(P \neq M\)。
   - **证明 \(Q \neq J, M\) 且 \(Q\) 是 \(D\) 在 \(JL\) 上的正投影**：若 \(Q = M\)，则 \(M \in JL\)，由 \(JL \perp AI\) 与 \(JM \perp AC\) 得 \(AI \parallel AC\)，矛盾。若 \(Q = J\)，则 \(JL\) 与 \(\omega\) 相切于 \(J\)，于是 \(JL \perp JD\)，结合 \(JL \perp AI\) 得 \(JD \parallel AI\)；但 \(\overrightarrow{JD}\) 在 \(AC\) 上的投影为 \(\overrightarrow{MD}\)（与 \(\overrightarrow{AC}\) 反向），而 \(\overrightarrow{AI}\) 在 \(AC\) 上的投影与 \(\overrightarrow{AC}\) 同向，矛盾。因此 \(Q \neq J\)。又 \(JD\) 是 \(\omega\) 的直径，故若 \(D \in JL\) 则 \(Q = D\)，若 \(D \notin JL\) 则 \(\angle JQD = 90^\circ\)；无论哪种情况，均有 \(DQ \perp JL\)，即 \(Q\) 是 \(D\) 在直线 \(JL\) 上的正投影。
   - **证明 \(P \neq Q\)**：因为 \(Q\) 是 \(D\) 在 \(JL\) 上的正投影且 \(JL \perp AI\)，点 \(Q\) 到直线 \(AI\) 的距离等于 \(D\) 到直线 \(AI\) 的距离，即 \(AD\sin\frac{A}{2}\)。而 \(MN \parallel AI\)，直线 \(MN\) 上任意一点到 \(AI\) 的距离等于 \(M\) 到 \(AI\) 的距离，即 \(AM\sin\frac{A}{2}\)。因为 \(AD < AM\)，所以 \(Q \notin MN\)，从而 \(Q \neq P\)。

2. **证明 \(PQ \parallel AB\)**
   因为 \(P, Q, J, M\) 是 \(\omega\) 上四个互异的点，由有向角（模 \(180^\circ\)）的圆周角定理：
   \[
   \measuredangle(PQ, JL) = \measuredangle(PQ, QJ) = \measuredangle(PM, MJ) = \measuredangle(MN, JM) = \measuredangle(AI, JM).
   \]
   结合 \(JL \perp AI\)（\(\measuredangle(JL, AI) = 90^\circ\)）及 \(JM \perp AC\)（\(\measuredangle(AC, JM) = 90^\circ\)），得
   \[
   \begin{aligned}
   \measuredangle(PQ, AC) &= \measuredangle(PQ, JL) + \measuredangle(JL, AI) + \measuredangle(AI, AC) \\
   &= \measuredangle(AI, AC) + \measuredangle(AC, JM) + 90^\circ + \measuredangle(AI, AC) \\
   &= 2\measuredangle(AI, AC) + 180^\circ = \measuredangle(AB, AC) \pmod{180^\circ},
   \end{aligned}
   \]
   其中最后一步用到 \(AI\) 平分 \(\angle BAC\)。因此 \(PQ \parallel AB\)。

3. **证明 \(QX \parallel AB\)**
   设 \(\mathbf{u}\) 为沿 \(\overrightarrow{AI}\) 方向的单位向量，\(\mathbf{v}\) 为垂直于 \(\mathbf{u}\) 且指向直线 \(AI\) 含 \(C\) 一侧半平面的单位向量（则 \(B\) 在 \(-\mathbf{v}\) 一侧）。因为 \(\angle IAC = \frac{A}{2}\) 且 \(D\) 在射线 \(\overrightarrow{AC}\) 上（记 \(d = AD > 0\)），有
   \[
   \overrightarrow{AD} = d\cos\frac{A}{2}\,\mathbf{u} + d\sin\frac{A}{2}\,\mathbf{v}.
   \]
   由于 \(L\) 是 \(AI\) 的中点且 \(JL \perp AI\)，\(D\) 在 \(JL\) 上的正投影 \(Q\) 满足
   \[
   \overrightarrow{AQ} = \frac{1}{2}\overrightarrow{AI} + d\sin\frac{A}{2}\,\mathbf{v}.
   \]
   又 \(X\) 是 \(ID\) 的中点，故
   \[
   \overrightarrow{AX} = \frac{1}{2}\left(\overrightarrow{AI} + \overrightarrow{AD}\right) = \frac{1}{2}\overrightarrow{AI} + \frac{d}{2}\cos\frac{A}{2}\,\mathbf{u} + \frac{d}{2}\sin\frac{A}{2}\,\mathbf{v}.
   \]
   两式相减得
   \[
   \overrightarrow{QX} = \overrightarrow{AX} - \overrightarrow{AQ} = \frac{d}{2}\left(\cos\frac{A}{2}\,\mathbf{u} - \sin\frac{A}{2}\,\mathbf{v}\right).
   \]
   因为 \(AI\) 是 \(\angle BAC\) 的内角平分线且 \(B, C\) 在 \(AI\) 异侧，沿 \(\overrightarrow{AB}\) 方向的单位向量正是 \(\cos\frac{A}{2}\,\mathbf{u} - \sin\frac{A}{2}\,\mathbf{v}\)。又 \(d > 0\)，故 \(\overrightarrow{QX} \neq \mathbf{0}\) 且 \(QX \parallel AB\)。

   由 \(PQ \parallel AB\) 与 \(QX \parallel AB\) 可知 \(P\)、\(Q\)、\(X\) 三点共线，即 \(X\) 在直线 \(PQ\) 上。

综上所述，点 \(X\) 同时在直线 \(PQ\)、\(LN\)、\(EF\) 上，因此直线 \(PQ\)、\(LN\)、\(EF\) 三线共点（交于 \(ID\) 的中点 \(X\)）。

### 2. 对照答案复盘

盲解思路与参考解答完全一致，均抓住核心交点为线段 \(ID\) 的中点（参考解答中记作线段 \(LN\) 上满足 \(LK = \frac{1}{2}AD\) 的点 \(K\)，盲解记作 \(X\)），先证该点在 \(LN\) 上，再分别证其在 \(EF\) 与 \(PQ\) 上。细节上，盲解进一步补齐了参考解答未讨论的退化情形（如 \(D \in JL\) 时 \(Q = D\)、\(C = 2A\) 时 \(PQ\) 与 \(EF\) 重合），并用有向角（模 \(180^\circ\)）与正交基向量替换了对等腰梯形 \(DQMP\) 和 \(KECN\) 图形顺序的依赖，使证明对所有满足条件的三角形均严格成立。

### 3. 困难点与破局关键

- **将“二圆交点”转化为“方向+投影”的双重刻画**：圆 \(\omega\) 的定义涉及 \(J, M, D\)，而要说明 \(PQ\) 过某固定点，需同时提取圆上的角度信息（\(PQ \parallel AB\)）与点的位置信息（\(Q\) 为 \(D\) 在 \(JL\) 上的投影），再通过解 \(\triangle LKQ\)（或向量分解）建立 \(KQ \parallel AB\)，两步结合才得到 \(K, P, Q\) 共线。
- **识别交点 \(K\) 为 \(ID\) 中点并完成长度相消**：从条件 \(BC=BD\) 出发既能得到 \(\angle DEF = \frac{C}{2}\)，又能算得 \(AE\) 与 \(AD\) 的关系；只有把 \(K\) 在 \(AC\) 上的投影 \(K'\) 与 \(\triangle ABC\) 内切圆切点 \(I'\) 联系起来，才能看到 \(EK' = \frac{a+b-c}{4} = \frac{1}{2}CI'\) 这一常数相消。

### 4. 问题拆解（教学引导）

- **拆解外心与中点条件，捕捉直角与直径**：由 \(I\) 是内心、\(J\) 是 \(\triangle AIC\) 外心及 \(L, M, N\) 为中点，立即识别出经典构型：\(JM \perp AC\)、\(JL\) 为 \(AI\) 中垂线、\(MN \parallel AI\) 且 \(LN \parallel AC\)。由 \(JM \perp AC\) 立刻看出 \(JD\) 是圆 \(\omega\) 的直径。
- **利用中位线性质锁定候选交点 \(K\)**：由于 \(PQ\)、\(LN\)、\(EF\) 三线共点且 \(LN \parallel AC\) 位置最简单，先思考交点在 \(LN\) 上的位置。注意到 \(D \in AC\) 而 \(LN\) 是 \(\triangle AIC\) 的中位线，线段 \(ID\) 的中点 \(K\) 天然落在 \(LN\) 上（满足 \(LK = \frac{1}{2}AD\)），于是可将三线共点拆解为“证明 \(K \in PQ\)”与“证明 \(K \in EF\)”两个独立目标。
- **将 \(BC=BD\) 与直径条件转化为角度和投影关系**：由 \(BC=BD\) 知 \(\triangle BCD\) 等腰且 \(\angle BDC = C\)，进而 \(\angle DEF = \frac{C}{2}\)，这把 \(EF\) 的方向与 \(\angle C\)（即直线 \(CI\) 的倾斜角）直接挂钩；另一方面，由 \(JD\) 为直径知 \(DQ \perp JL\)，把 \(Q\) 转化为 \(D\) 的正投影，从而可从纯方向与长度角度分别攻克两个共线目标。

### 5. 答案拆解（逻辑骨架）

- **重新刻画目标共点 \(K\)**（*动机*：把“三线共点”转化为“特定点落在另外两条直线上”，避免直接求 \(PQ \cap EF\) 带来的复杂表达。）：在线段 \(LN\) 上取点 \(K\) 使 \(LK = \frac{1}{2}AD\)（即 \(ID\) 的中点）。因为 \(L, N\) 为 \(IA, IC\) 中点且 \(D \in AC\)，以 \(I\) 为中心、\(\frac{1}{2}\) 为位似比的位似变换把 \(A, D, C\) 映为 \(L, K, N\)，故 \(K\) 必在直线 \(LN\) 上，只需证明 \(K, P, Q\) 共线与 \(K, E, F\) 共线。
- **利用圆 \(\omega\) 的直径与平行弦确定 \(PQ \parallel AB\)**（*动机*：先确定直线 \(PQ\) 的方向，只需再证明 \(KQ\) 具有相同方向即可推出共线。）：由 \(J\) 为 \(\triangle AIC\) 外心知 \(JM \perp AC\)、\(JL \perp AI\)；因 \(D \in AM\)，有 \(\angle JMD = 90^\circ\)，故 \(DJ\) 为 \(\omega\) 直径，从而 \(DQ \perp LJ\)（\(Q\) 为 \(D\) 在 \(LJ\) 上投影），进而 \(DQ \parallel AI \parallel PM\)。于是圆内接四边形 \(DQMP\) 为等腰梯形（一般情形下；或用有向角），结合 \(PM \parallel AI\) 得 \(PQ\) 与 \(AC\) 成角 \(2\angle IAC = \angle BAC\)，即 \(PQ \parallel AB\)。
- **证明 \(KQ \parallel AB\) 完成 \(K, P, Q\) 共线**（*动机*：在已得 \(PQ \parallel AB\) 的前提下，只需验证 \(KQ\) 的斜率或夹角等于 \(\angle A\)。）：在 \(\triangle LKQ\) 中，\(LK = \frac{1}{2}AD\)，由 \(Q\) 是 \(D\) 在 \(LJ\) 上的投影及 \(LJ \perp AI\) 得 \(LQ = AD\sin\frac{A}{2}\)，且 \(\angle KLQ = 90^\circ - \frac{A}{2}\)。于是 \(LK\cos\angle KLQ = \frac{1}{2}AD\sin\frac{A}{2} = \frac{1}{2}LQ\)，说明 \(K\) 在 \(LQ\) 的中垂线上，故 \(\angle LKQ = 180^\circ - 2(90^\circ - \frac{A}{2}) = A\)。又 \(LK \parallel AC\)，从而 \(KQ \parallel AB\)，结合 \(PQ \parallel AB\) 即得 \(K, P, Q\) 共线。
- **投影算长度证明 \(K, E, F\) 共线**（*动机*：\(EF\) 的方向角已固定为 \(\frac{C}{2}\)，因此只需证明 \(KE\) 与 \(AC\) 夹角也为 \(\frac{C}{2}\)，这等价于比较 \(K\) 到 \(E\) 的水平投影与到 \(C\) 的距离。）：作 \(I, L, K, N\) 在 \(AC\) 上的正投影 \(I', L', K', N'\)，利用切线长公式 \(AE = \frac{AD+AB-BD}{2}\) 与 \(AI' = \frac{AB+AC-BC}{2}\)，算出 \(EK' = \frac{1}{2}AI' + \frac{1}{2}AD - AE = \frac{AC+BC-AB}{4} = \frac{1}{2}CI' = CN'\)。因为 \(KN \parallel AC\) 且 \(K, N\) 到 \(AC\) 距离均为 \(I\) 到 \(AC\) 距离的一半，所以 \(KECN\) 为等腰梯形（或直接在 \(\mathrm{Rt}\triangle EK'K\) 中算 \(\tan\angle KEK' = \frac{r}{s-c} = \tan\frac{C}{2}\)），得 \(\angle KED = \angle ICD = \frac{C}{2}\)；又 \(\triangle BCD\) 中 \(BC=BD\) 故 \(\angle BDC = C\)、\(\angle FED = \frac{C}{2}\)，因此 \(K, E, F\) 共线。

### 6. 易错点分析

- **忽略 \(Q = D\) 的退化情形导致等腰梯形失效**：常见错法——默认 \(P, Q, D, M\) 总是构成非退化的等腰梯形 \(DQMP\)，忽略了当 \(D\) 恰落在 \(AI\) 的中垂线 \(JL\) 上时会出现 \(Q = D\) 的情形。；错因——当 \(D \in JL\)（例如 \(a=4, b=5\) 且 \(c \in (4.5, 5)\) 的某些三角形）时，\(JD\) 与 \(JL\) 重合，从而 \(Q = D\)，此时四边形 \(DQMP\) 退化为三角形，直接引用等腰梯形 \(DQMP\) 的底角性质会导致论证不完整。；避坑策略——在证明四点共圆导角或使用等腰梯形前，先检验各点是否重合；更稳妥的做法是采用有向角（模 \(180^\circ\)）与向量方法，直接对 \(Q=D\) 与 \(Q \neq D\) 给出统一论证。
- **依赖草图顺序导致有向线段与梯形构型出错**：常见错法——直接把 \(KECN\) 当作标准等腰梯形并用纯角加减推导 \(\angle KED = \angle ICD\)，未验证点 \(E\)、\(D\)、\(I'\)、\(K'\) 在 \(AC\) 上的先后顺序。；错因——随着 \(AD\) 长度变化，点 \(E\) 可能位于 \(I'\)（即内切圆切点）的左侧或右侧，若不校验 \(EK'\) 的方向（即 \(AK' - AE > 0\)），草图上的梯形方向可能发生翻转或自交。；避坑策略——使用从 \(A\) 出发沿射线 \(\overrightarrow{AC}\) 的有向坐标（或直接计算 \(\tan\angle XEX'\) 并比较 \(E_0\)、\(X'\) 与 \(A\) 的位置差 \(AX' - AE > 0\)），不依赖 \(E\)、\(X'\)、\(E_0\) 的左右排列顺序。
- **忽视 \(PQ\) 与 \(EF\) 可能重合的情形**：常见错法——认为“三线共点”必须满足三条直线两两相交于同一点，在构造时强行设 \(PQ \cap EF\)，未注意两者可能重合。；错因——当 \(\triangle ABC\) 满足 \(C = 2A\) 且 \(A < 30^\circ\) 时，\(PQ\) 与 \(EF\) 均过 \(ID\) 中点且均与 \(AC\) 成角 \(A\)，此时 \(PQ\) 与 \(EF\) 重合；若依赖“交点存在唯一”，论证会在这一情形失效。；避坑策略——对“三线共点”问题，最稳健的策略是构造唯一候选交点 \(X\) 并分别验证 \(X \in PQ\)、\(X \in LN\)、\(X \in EF\)，不要假定三条直线必须两两不同。

**教学小结**：面对“三条直线共点”的平面几何题，首先应寻找其中一条直线（如中位线 \(LN\)）上由另一几何对象（如 \(ID\) 中点）自然诱导的特殊点作为候选交点，再把共点问题拆解为“方向平行”与“投影算长”两个局部子命题逐一击破。

---

## 2024 CMO 试题与解答 · 3（`cmo-2024-both-days-combined-q3`）

- **学段**：高中 · **盲解结果**：盲解正确（不同有效解法）
- **教学标签**：训练:压轴攻坚 / 放缩与估值 / 概率方法与算两次 / 极端原理 / 易错:边界与退化情形 / 易错:计数重复与漏算 / 易错:隐含假设与越界推广
- **知识专题**：数论与组合 / 分式部分 / 极小集合与最值

### 原题整理

给定正整数 \(a_1 > a_2 > \dots > a_n > 1\)，记 \(M = \mathrm{lcm}(a_1, a_2, \dots, a_n)\)，对有限非空正整数集 \(X\)，记
\[
f(X) = \min_{1 \le i \le n} \sum_{x \in X} \left\{\frac{x}{a_i}\right\},
\]
称 \(X\) 为“极小的”，如果对 \(X\) 的任意真子集 \(Y\)，均有 \(f(Y) < f(X)\)。设 \(X\) 是极小的且 \(f(X) \ge \frac{2}{a_n}\)，证明：\(|X| \le f(X)M\)。

### 1. 只看原题盲解尝试

**切入思路**：利用“极小性”的等价刻画与迭代整除链分解来界定集合 \(X\) 的大小。首先选取使分式部分之和达到最小值 \(f(X)\) 的下标 \(i_0\)，记 \(L_1 = a_{i_0}\)，将 \(X\) 中不被 \(L_1\) 整除的元素直接用 \(S_{i_0}(X) = f(X)\) 界定为不超过 \(L_1 f(X)\)。对于剩余被 \(L_1\) 整除的子集 \(Z_1\)，利用极小性不断选取能覆盖 \(Z_t\) 中元素的指标 \(j_t\) 并将模数扩大为 \(L_{t+1} = \mathrm{lcm}(L_t, a_{j_t})\)，利用 \(\delta_{j_t} < 1 - \frac{1}{b_t}\)（其中 \(b_t = L_{t+1}/L_t \ge 2\)）精确控制每一步被筛去的元素个数，最后结合 \(\sum b_t \le \prod b_t \le \frac{M}{L_1}\) 与 \(f(X) \ge \frac{2}{a_n} \ge \frac{2}{L_1}\) 以及 \(M f(X) \in \mathbb{Z}\) 完成严格放缩。

**推演步骤**：
- 记 \(S_i(X) = \sum_{x \in X} \left\{\frac{x}{a_i}\right\}\)，\(f = f(X) = \min_{1 \le i \le n} S_i(X)\)，且对每个 \(i \in \{1, \dots, n\}\) 记 \(\delta_i = S_i(X) - f \ge 0\)。选取 \(i_0 \in \{1, \dots, n\}\) 使得 \(S_{i_0}(X) = f\)。由于 \(S_{i_0}(X)\) 是 \(\frac{1}{a_{i_0}}\) 的整数倍且 \(a_{i_0} \mid M\)，故 \(M f\) 为正整数。
- 令 \(L_1 = a_{i_0}\)，并记 \(Z_1 = \{ x \in X : L_1 \mid x \}\)。对任意 \(x \in X \setminus Z_1\)，有 \(a_{i_0} \nmid x\)，因此 \(\left\{\frac{x}{a_{i_0}}\right\} \ge \frac{1}{a_{i_0}}\)。于是 \(f = S_{i_0}(X) \ge \frac{|X \setminus Z_1|}{a_{i_0}}\)，即 \(|X \setminus Z_1| \le L_1 f\)。若 \(Z_1 = \emptyset\)，则 \(|X| = |X \setminus Z_1| \le L_1 f \le M f\)，结论成立。
- 若 \(Z_1 \ne \emptyset\)，构造递降子集列 \(Z_1 \supset Z_2 \supset \dots \supset Z_m = \emptyset\) 及严格递增整除链 \(L_1 \mid L_2 \mid \dots \mid L_m \mid M\)。对当前非空的 \(Z_t\)（其中 \(Z_t = \{ x \in X : L_t \mid x \}\)），任取 \(x_t \in Z_t\)。由 \(X\) 的极小性，\(f(X \setminus \{x_t\}) < f\)，故存在 \(j_t \in \{1, \dots, n\}\) 使得 \(S_{j_t}(X \setminus \{x_t\}) < f\)，即 \(\left\{\frac{x_t}{a_{j_t}}\right\} > S_{j_t}(X) - f = \delta_{j_t} \ge 0\)。特别地，\(a_{j_t} \nmid x_t\)，结合 \(L_t \mid x_t\) 可知 \(a_{j_t} \nmid L_t\)。
- 令 \(L_{t+1} = \mathrm{lcm}(L_t, a_{j_t})\)，\(b_t = \frac{L_{t+1}}{L_t} = \frac{a_{j_t}}{\gcd(a_{j_t}, L_t)} \ge 2\)（为整数），并令 \(Z_{t+1} = \{ x \in Z_t : a_{j_t} \mid x \} = \{ x \in X : L_{t+1} \mid x \}\)。由于 \(L_t < L_{t+1} \mid M\)，该过程必在有限步 \(m \ge 2\) 后终止，且有 \(Z_m = \emptyset\)（若 \(L_t = M\)，则 \(Z_t\) 中元素被所有 \(a_j\) 整除，与极小性矛盾）。
- 在每一步 \(t \in \{1, \dots, m-1\}\) 中，因为 \(L_t \mid x_t\) 且 \(a_{j_t} \nmid x_t\)，故 \(\gcd(a_{j_t}, L_t) \mid x_t\)，从而 \(\left\{\frac{x_t}{a_{j_t}}\right\}\) 是 \(\frac{1}{b_t}\) 的正整数倍且小于 \(1\)，因此 \(\delta_{j_t} < \left\{\frac{x_t}{a_{j_t}}\right\} \le 1 - \frac{1}{b_t}\)，即 \(S_{j_t}(X) < f + 1 - \frac{1}{b_t}\)。另一方面，对任意 \(x \in Z_t \setminus Z_{t+1}\)，有 \(L_t \mid x\) 且 \(a_{j_t} \nmid x\)，故 \(\left\{\frac{x}{a_{j_t}}\right\} \ge \frac{1}{b_t}\)。求和得 \(\frac{|Z_t \setminus Z_{t+1}|}{b_t} \le S_{j_t}(X) < f + 1 - \frac{1}{b_t}\)，即 \(|Z_t \setminus Z_{t+1}| < b_t f + b_t - 1\)。
- 记 \(P_0 = \frac{M}{L_1} \ge \frac{L_m}{L_1} = \prod_{t=1}^{m-1} b_t\)。对整数 \(b_1, \dots, b_{m-1} \ge 2\)，易证 \(\sum_{t=1}^{m-1} b_t \le \prod_{t=1}^{m-1} b_t \le P_0\)（利用 \(A, B \ge 2 \implies AB \ge A + B\) 归纳）。将各步估计相加，得 \(|X| = |X \setminus Z_1| + \sum_{t=1}^{m-1} |Z_t \setminus Z_{t+1}| < L_1 f + \sum_{t=1}^{m-1} (b_t f + b_t - 1) \le (L_1 + P_0) f + P_0 - 1\)。
- 由于 \(L_1 = a_{i_0} \ge a_n \ge 2\) 且 \(P_0 \ge 2\)，有 \(P_0 L_1 - L_1 - P_0 = (P_0 - 1)(L_1 - 1) - 1 \ge 0\)。结合 \(f \ge \frac{2}{a_n} \ge \frac{2}{L_1}\)，可得 \((M f + 1) - \big((L_1 + P_0) f + P_0 - 1\big) = (P_0 L_1 - L_1 - P_0) f - (P_0 - 2) \ge (P_0 L_1 - L_1 - P_0) \frac{2}{L_1} - (P_0 - 2) = P_0 \left(1 - \frac{2}{L_1}\right) \ge 0\)。因此 \(|X| < M f + 1\)。又因为 \(|X|\) 与 \(M f\) 均为整数，故 \(|X| \le M f = f(X) M\)。

**盲解结论**：证明完毕，结论 \(|X| \le f(X)M\) 成立。

### 2. 对照答案复盘

Turn 1 盲解完全正确且无逻辑漏洞，采用的是与参考解答不同的另一种有效方法（`different_valid_method`）。Turn 1 从极小性的等价刻画 \(X = \bigcup_{i=1}^n X_i\) 出发，选取使 \(S_{i_0}(X) = f(X)\) 的模数 \(L_1 = a_{i_0}\)，对能被 \(L_1\) 整除的剩余元素迭代构造整除链 \(L_1 \mid L_2 \mid \dots \mid L_m \mid M\)，利用 \(\delta_{j_t} < 1 - \frac{1}{b_t}\) 与 \(\sum b_t \le \prod b_t \le \frac{M}{L_1}\)、\(f(X) \ge \frac{2}{L_1}\) 及 \(M f(X) \in \mathbb{Z}\) 直接完成证明，无需对 \(n=2\) 单独讨论，也无需删去冗余的 \(a_i\)。参考解答则采用“消去冗余 \(a_i\) + 算两次”的思路：先删去不能产生新极小减元子集 \(X_i\) 的 \(a_i\)，剔除 \(n-1\) 个代表元 \(P\) 得到 \(X'\)，再对 \(\sum_{i=1}^n \sum_{x \in X'} \left\{\frac{x}{a_i}\right\}\) 进行双向估计（上界用 \(n f(X) - \frac{n-1}{M}\)，下界利用 \((x,M) \ge 2t\) 得出每项和至少为 \(\frac{2(n-1)}{M}\)），从而迫使 \(n=2\) 后再收尾。两种方法均严谨完整。

### 3. 困难点与破局关键

- **如何处理多个 \(a_i\) 之间的重叠与非独立性**：题目中的“极小性”是一个关于所有真子集的条件，直接将其等价转化为每个 \(x \in X\) 都存在某个 \(i\) 使得 \(S_i(X \setminus \{x\}) < f(X)\)，只是第一步；更大的难点在于多个 \(a_i\) 之间存在复杂的公因数关系（\(\sum a_i\) 甚至可以远大于 \(M\)），无法简单地把每个 \(i\) 对应的“关键元素”个数直接相加来得到 \(f(X)M\)。
- **找到能同时利用 \(M = \mathrm{lcm}(a_1, \dots, a_n)\) 与 \(f(X) \ge \frac{2}{a_n}\) 的放缩桥梁**：参考解答中将“每个 \(i \ne i_0\) 对应一个不同的 \((|X|-1)\)-子集 \(X_i\)”与“删去不满足条件的 \(a_i\)”结合，使得被剔除的集合 \(P\) 恰好有 \(n-1\) 个元素；如果不做这一步，\(x_i\) 可能重合，无法保证 \(|X'| = |X| - n + 1\)。而盲解中则通过整除链 \(L_t \mid L_{t+1}\) 强制每次扩大的倍数 \(b_t \ge 2\) 满足和不超过积，从而绕开了 \(\sum a_i > M\) 的障碍。

### 4. 问题拆解（教学引导）

- **解读目标不等式与整性条件**：明确目标不等式 \(|X| \le f(X)M\) 的等价形式：对至少一个（乃至所有）指标 \(i\)，有 \(\frac{|X|}{M} \le \sum_{x \in X} \left\{\frac{x}{a_i}\right\}\)。同时注意到 \(f(X)\) 必由某个 \(i_0\) 取到，故 \(M f(X)\) 恒为正整数。
- **刻画极小性与检验特殊情形**：由 \(f\) 的单调性，\(X\) 是极小的等价于：对每个 \(x \in X\)，存在 \(i\) 使得 \(S_i(X \setminus \{x\}) < f(X)\)，即 \(\left\{\frac{x}{a_i}\right\} > S_i(X) - f(X)\)。特别地，若 \(a_1 = M\) 且 \(S_1(X) = f(X)\)，则不存在 \(a_1 \mid x\)，立得 \(|X| \le f(X) M\)。
- **挖掘 \(f(X) \ge \frac{2}{a_n}\) 与 \(M > a_1\) 的数值信息**：条件 \(f(X) \ge \frac{2}{a_n}\) 意味着对任意 \(i\) 都有 \(a_i f(X) \ge 2\)；当 \(M > a_1\) 时，有 \(a_i \le \frac{M}{i+1}\)，从而 \(f(X) \ge \frac{2(n+1)}{M}\)，这是后续比较线性项与乘积项的关键。

### 5. 答案拆解（逻辑骨架）

- **第一步：消去冗余的 \(a_i\) 并构造代表元集合 \(P\)**（*动机*：为了后续对所有 \(a_i\) 求和时能够统一剔除一组代表元，先消去不能提供新“关键元素”的冗余模数 \(a_i\)。）：设 \(i_0\) 使得 \(S_{i_0}(X) = f(X)\)，令 \(X_{i_0} = X\)。依次考察 \(i \ne i_0\)：若存在不同于已取集合的 \(Y \subset X\)（\(|Y| = |X| - 1\)）使得 \(S_i(Y) = f(Y)\)，则记 \(X_i = Y\)；否则删去 \(a_i\)。删去这样的 \(a_i\) 不会改变 \(f(X)\) 与任意 \((|X|-1)\)-子集的 \(f(Y)\)，从而不破坏 \(X\) 的极小性，且新的公倍数 \(M' \le M\)。于是可设对所有 \(i \ne i_0\) 都有互不相同的 \(X_i = X \setminus \{x_i\}\)，记 \(P = \{x_i : i \ne i_0\}\)，则 \(|P| = n - 1\)。
- **第二步：按 \(M = a_1\) 与 \(M > a_1\) 分类处理**（*动机*：将 \(M = a_1\) 的平凡情形分离出来，从而在 \(M > a_1\) 时获得更强的分母上界 \(a_i \le \frac{M}{i+1}\)。）：若 \(M = a_1\)，则任意 \(x \in X\) 均不被 \(a_1\) 整除（否则去掉 \(x\) 后 \(f\) 不变，与极小性矛盾），故 \(\left\{\frac{x}{a_1}\right\} \ge \frac{1}{M}\)，直接求和得 \(f(X) \ge \frac{|X|}{M}\)。若 \(M > a_1\)，则 \(\frac{M}{a_1} \ge 2\)，由 \(a_1 > a_2 > \dots > a_n\) 递推得 \(\frac{M}{a_i} \ge i + 1\)。
- **第三步：利用极小性建立双和的上界**（*动机*：通过剔除 \(P\)，保证每个 \(i \ne i_0\) 在 \(X'\) 上的和严格小于 \(f(X)\)（至少差 \(\frac{1}{M}\)）。）：记 \(X' = X \setminus P\)，则 \(|X'| = |X| - n + 1\)。由于 \(X' \subset X_i\) 且对 \(i \ne i_0\) 有 \(f(X_i) \le f(X) - \frac{1}{M}\)（利用 \(M f\) 的整性与极小性），故有上界
\[
\sum_{i=1}^n \sum_{x \in X'} \left\{\frac{x}{a_i}\right\} \le \sum_{i=1}^n f(X_i) \le n f(X) - \frac{n-1}{M}.
\]
- **第四步：交换求和次序并建立内层和的统一下界**（*动机*：对单个 \(x \in X'\) 而言，若许多 \(a_i\) 整除 \(x\)，则 \((x, M)\) 必然很大，从而迫使剩余非零分式部分的分子很大。这是整个证明最核心的数论估值技巧。）：交换求和次序，对固定的 \(x \in X'\) 估计 \(\sum_{i=1}^n \left\{\frac{x}{a_i}\right\}\)。若其中有 \(t \ge 1\) 项为 \(0\)，则这 \(t\) 个 \(a_i\) 均整除 \((x, M)\)，故 \((x, M) \ge 2t\)；其余 \(n - t\) 个非零项的分子均为 \((x, M)\) 的正整数倍，故每项至少为 \(\frac{2t}{M}\)，总和至少为 \(\frac{2t(n-t)}{M} \ge \frac{2(n-1)}{M}\)。若 \(t = 0\)，则利用 \(\frac{M}{a_i} \ge i + 1\) 直接得总和至少为 \(\sum_{i=1}^n \frac{i+1}{M} \ge \frac{2(n-1)}{M}\)。
- **第五步：合并上下界，排除 \(n \ge 3\) 并处理 \(n = 2\)**（*动机*：通过上下界对撞消去 \(|X|\)，将问题压缩到极端的 \(n=2\) 情形并最终导出矛盾。）：结合上下界并反设 \(|X| \ge f(X)M\)（实际严格大于，但参考解答以 \(\ge\) 推出 \(n=2\)），代入 \(f(X) \ge \frac{2}{a_n} \ge \frac{2(n+1)}{M}\)，化简得 \(\frac{2(n+1)}{M} \le f(X) \le \frac{(n-1)(2n-3)}{(n-2)M}\)（\(n \ge 3\)），矛盾，故只剩 \(n = 2\)。当 \(n = 2\) 时，利用 \(2f(X) - \frac{1}{M}\) 与下界 \(\frac{3}{M}(|X|-1)\) 对比得出必有 \(a_1 = \frac{M}{2}, a_2 = 2\) 且至少两个 \(x\) 为奇数（由 \(f(X) \ge \frac{2}{a_2} = 1\)），从而再收紧下界导出矛盾。

### 6. 易错点分析

- **删去冗余模数时忽略极小性的保持**：常见错法——在删去多余的 \(a_i\) 时，只检查 \(f(X)\) 不变而忽略了 \(X\) 的极小性是否被破坏（即是否存在某个真子集 \(Y\) 在删去 \(a_i\) 后 \(f(Y)\) 变大到 \(\ge f(X)\)）。；错因——删去一个 \(a_i\) 不会减小 \(f(X)\)，但有可能使某个真子集 \(Y\) 的最小值变大；必须验证对所有 \(|Y|=|X|-1\) 的子集，要么 \(f(Y)\) 本就由其他 \(a_j\) 达到，要么 \(Y\) 已被选作某个 \(X_j\)，从而 \(f(Y) < f(X)\) 仍成立。；避坑策略——严格区分“去掉 \(a_i\) 不改变 \(f(X)\)”与“去掉 \(a_i\) 不改变 \(X\) 的极小性”，说明为何所有 \(|Y|=|X|-1\) 的子集的 \(f(Y)\) 也不变，或改用保留全部 \(a_i\) 的整除链分解法。
- **对分式部分和的下界估计过松**：常见错法——对单个 \(x \in X'\) 估计 \(\sum_{i=1}^n \left\{\frac{x}{a_i}\right\}\) 时，直接用 \(\frac{1}{a_i} \ge \frac{1}{M}\) 放缩，忽略了 \(t\) 个零项带来的 \((x, M)\) 公因子放大效应。；错因——若仅用 \(\left\{\frac{x}{a_i}\right\} \ge \frac{1}{M}\) 对非零项求和，只能得到 \(\frac{n-t}{M}\)，当 \(t\) 较大时无法与上界 \(n f(X) - \frac{n-1}{M}\) 抗衡。；避坑策略——对 \(t=0\) 与 \(t \ge 1\) 分别讨论：\(t=0\) 时利用 \(a_i \le \frac{M}{i+1}\)；\(t \ge 1\) 时利用 \((x,M) \ge 2t\) 得到下界 \(\frac{2t(n-t)}{M} \ge \frac{2(n-1)}{M}\)。
- **忽略 \(M f(X)\) 的整性及 \(n=2\) 的边界情况**：常见错法——忘记利用 \(M f(X)\) 是整数这一性质，或在 \(f(X) \ge \frac{2}{a_n}\) 的放缩中忽略 \(n=2\) 或 \(a_1 = M\) 等边界情形。；错因——若不利用 \(M f(X) \in \mathbb{Z}\)，许多严格小于 \(M f(X) + 1\) 的上界无法收口到 \(\le M f(X)\)；而在参考解答中，\(n \ge 3\) 时可直接推出矛盾，\(n=2\) 则是边界情形需单独检验。；避坑策略——在不等式两端出现常数误差（如 \(+1\) 或 \(-\frac{n-1}{M}\)）时，先确认 \(M f(X) \in \mathbb{Z}\)，再利用严格不等号 \(< M f(X) + 1\) 推出 \(\le M f(X)\)。

**教学小结**：面对涉及最小公倍数 \(M = \mathrm{lcm}(a_1, \dots, a_n)\) 与“极小性”的数论组合最值问题时，既可以通过“删去冗余模数 + 交换求和次序（算两次）”并借助 \((x, M)\) 放大分式部分下界来破局，也可以通过“构造整除链 \(L_1 \mid L_2 \mid \dots \mid L_m \mid M\)”将原本重叠的模数转化为乘积不超限的逐步筛除。

---

## 2024 CMO 试题与解答 · 4（`cmo-2024-both-days-combined-q4`）

- **学段**：高中 · **盲解结果**：盲解正确（不同有效解法）
- **教学标签**：训练:压轴攻坚 / 构造与反例 / 辅助线与几何变换 / 反证与分类讨论 / 易错:边界与退化情形 / 易错:隐含假设与越界推广 / 易错:符号与方向
- **知识专题**：组合几何 / 抽屉原理与区域剖分 / 平环面距离最值

### 原题整理

对于 \(\mathbb{R}^2\) 中任意两点 \((x_1, y_1), (x_2, y_2)\)，我们定义该两点之间的小数距离为 \[\sqrt{\|x_1 - x_2\|^2 + \|y_1 - y_2\|^2}\] 其中 \(\|x\|\) 表示实数 \(x\) 与最近的整数的距离。求最大的实数 \(r\)，使得平面上存在四个点，满足两两之间的小数距离均不小于 \(r\)。

### 1. 只看原题盲解尝试

**切入思路**：将平面上的小数距离等价转化为二维平环面 \(\mathbb{T}^2 = \mathbb{R}^2 / \mathbb{Z}^2\) 上的度量。首先通过显式构造四个点 \((0,0), (a, \frac{1}{2}), (\frac{1}{2}, a), (\frac{1}{2}+a, \frac{1}{2}+a)\)（其中 \(a = 1 - \frac{\sqrt{3}}{2}\)，对应平面周期密铺中的扭棱正方形密铺），说明可以达到 \(r = \sqrt{2-\sqrt{3}} = \frac{\sqrt{6}-\sqrt{2}}{2}\)。随后采用反证法证明上界：假设存在四点满足两两距离均不小于 \(r > \frac{\sqrt{6}-\sqrt{2}}{2}\)，通过平移与对称性将四点坐标归约为环面上的标准序，按横纵坐标的相对排列顺序分为三种本质不同的情形（\(24\) 归约为 \(3\) 种置换），分别利用区间和、绝对值不等式以及代数放缩导出矛盾。

**推演步骤**：
- **构造下界（证明 \(r \ge \frac{\sqrt{6}-\sqrt{2}}{2}\)）：** 令 \(a = 1 - \frac{\sqrt{3}}{2}\in (0,\frac{1}{2})\)，在平面上取四个点：
\[P_1 = (0,0),\quad P_2 = \left(a, \frac{1}{2}\right),\quad P_3 = \left(\frac{1}{2}, a\right),\quad P_4 = \left(\frac{1}{2}+a, \frac{1}{2}+a\right).\]
计算两两之间小数距离的平方：
- \(d(P_1, P_2)^2 = d(P_1, P_3)^2 = d(P_2, P_4)^2 = d(P_3, P_4)^2 = \|a\|^2 + \left\|\frac{1}{2}\right\|^2 = a^2 + \frac{1}{4} = \left(1 - \frac{\sqrt{3}}{2}\right)^2 + \frac{1}{4} = 2 - \sqrt{3}\)；
- \(d(P_1, P_4)^2 = d(P_2, P_3)^2 = 2\left\|\frac{1}{2} - a\right\|^2 = 2\left(\frac{\sqrt{3}-1}{2}\right)^2 = 2 - \sqrt{3}\)。
注意 \(\sqrt{2-\sqrt{3}} = \frac{\sqrt{6}-\sqrt{2}}{2}\)，因此这四个点两两之间的小数距离均等于 \(\frac{\sqrt{6}-\sqrt{2}}{2}\)。
- **证明上界——基本性质与归约：** 设存在四个点 \(P_1, P_2, P_3, P_4\) 满足两两之间的小数距离均不小于 \(r\)。注意到对任意实数 \(t\) 有 \(\|t\| \in [0, \frac{1}{2}]\)，且对 \(t \in [0,1]\) 有 \(\|t\| = \min(t, 1-t) = \frac{1}{2} - \left|t - \frac{1}{2}\right|\)，故恒有 \(r \le \sqrt{\left(\frac{1}{2}\right)^2 + \left(\frac{1}{2}\right)^2} = \frac{1}{\sqrt{2}}\)。

反证：假设 \(r > \frac{\sqrt{6}-\sqrt{2}}{2}\)。因为 \(\left(\frac{\sqrt{6}-\sqrt{2}}{2}\right)^2 = 2-\sqrt{3} > \frac{1}{4}\)，故 \(r > \frac{1}{2}\)。令 \(\delta = \sqrt{r^2 - \frac{1}{4}}\)，则 \(\delta \in \left(1-\frac{\sqrt{3}}{2}, \frac{1}{2}\right]\)，且 \(M := \frac{1}{2} - \delta \in \left[0, \frac{\sqrt{3}-1}{2}\right)\)。

由于 \(\|t\|\) 仅依赖于 \(t \bmod 1\)，将各点横、纵坐标分别取小数部分并作适当平移（不改变两两之间的 \(\|x_i-x_j\|\) 与 \(\|y_i-y_j\|\)），可设 \(P_i = (x_i, y_i) \in [0, 1)^2\)。若存在两点横坐标相等，则它们的小数距离为 \(\|y_i-y_j\| \le \frac{1}{2} < r\)，矛盾；同理纵坐标也两两互异。重新编号并平移，使 \(0 = x_1 < x_2 < x_3 < x_4 < 1\) 且 \(y_1 = 0\)，\(y_2, y_3, y_4 \in (0, 1)\) 互异。

**引理：** 若两点 \((x,y)\) 与 \((x',y')\) 满足 \(\|x-x'\|^2 + \|y-y'\|^2 \ge r^2\)，记 \(u = \|x-x'\|\)，\(v = \|y-y'\|\)，则 \(u \ge \delta\)，\(v \ge \delta\)，且 \(u + v \ge \frac{1}{2} + \delta\)。
*证明：* 由 \(v \le \frac{1}{2}\) 得 \(u^2 \ge r^2 - \frac{1}{4} = \delta^2\)，故 \(u \ge \delta\)；同理 \(v \ge \delta\)。又 \((\frac{1}{2}-u)(\frac{1}{2}-v) \ge 0\)，展开得 \(2uv \ge u+v-\frac{1}{2}\)，从而 \((u+v)^2 = u^2+v^2+2uv \ge \frac{1}{4}+\delta^2+u+v-\frac{1}{2}\)，即 \((u+v-\frac{1}{2})^2 \ge \delta^2\)。因 \(u+v \ge \sqrt{u^2+v^2} \ge r > \frac{1}{2}\)，故 \(u+v \ge \frac{1}{2}+\delta\)。
- **按 \(y_2, y_3, y_4\) 的大小顺序分类讨论：** \((y_2, y_3, y_4)\) 的大小排列共有 \(6\) 种情况。利用变换 \(y \mapsto 1-y \pmod 1\)（保持 \(x_i\) 序与 \(y_1=0\) 不变）可将 \(y_1 < y_4 < y_3 < y_2\) 化为 \(y_1 < y_2 < y_3 < y_4\)，将 \(y_1 < y_3 < y_4 < y_2\) 化为 \(y_1 < y_2 < y_4 < y_3\)；利用变换 \(x \mapsto 1-x \pmod 1\) 并重排标号 \((P_1, P_4, P_3, P_2)\) 可将 \(y_1 < y_4 < y_2 < y_3\) 化为 \(y_1 < y_2 < y_4 < y_3\)。因此只需考虑以下三种本质不同的情形：

**情形 1：\(y_1 < y_2 < y_3 < y_4\)。**
记 \(g_1 = x_2-x_1, g_2 = x_3-x_2, g_3 = x_4-x_3, g_4 = 1-x_4\)，以及 \(h_1 = y_2-y_1, h_2 = y_3-y_2, h_3 = y_4-y_3, h_4 = 1-y_4\)。它们均为正数且 \(\sum_{i=1}^4 g_i = \sum_{i=1}^4 h_i = 1\)。对 \((P_1, P_2), (P_2, P_3), (P_3, P_4), (P_4, P_1)\) 分别有 \(r \le \sqrt{\|g_i\|^2 + \|h_i\|^2} \le g_i + h_i\)（\(i=1,2,3,4\)）。四式相加得 \(4r \le \sum_{i=1}^4 (g_i+h_i) = 2\)，故 \(r \le \frac{1}{2}\)，与 \(r > \frac{1}{2}\) 矛盾。

**情形 2：\(y_1 < y_2 < y_4 < y_3\)。**
记 \(g_1 = x_2-x_1, g_2 = x_3-x_2, g_3 = x_4-x_3, g_4 = 1-x_4\)，以及 \(h_1 = y_2-y_1, h_2 = y_4-y_2, h_3 = y_3-y_4, h_4 = 1-y_3\)。它们均为正数且 \(\sum_{i=1}^4 g_i = \sum_{i=1}^4 h_i = 1\)。对点对 \((P_1, P_2), (P_3, P_4), (P_1, P_3), (P_2, P_3), (P_2, P_4)\) 分别应用引理（并注意到 \(\|t\| \le t\) 与 \(\|1-t\| = \|t\| \le t\)）：
- 由 \((P_1, P_2)\) 得 \(g_1 + h_1 \ge \frac{1}{2} + \delta\)；
- 由 \((P_3, P_4)\) 得 \(g_3 + h_3 \ge \frac{1}{2} + \delta\)；
- 由 \((P_1, P_3)\) 得 \(g_4 + h_4 \ge \frac{1}{2} + \delta\)；
- 由 \((P_2, P_3)\) 得 \(g_2 \ge \delta\)；
- 由 \((P_2, P_4)\) 得 \(h_2 \ge \delta\)。
五式相加得 \(2 = \sum_{i=1}^4 (g_i + h_i) \ge \frac{3}{2} + 5\delta\)，即 \(\delta \le \frac{1}{10}\)。然而 \(\delta > 1 - \frac{\sqrt{3}}{2} > \frac{1}{10}\)（因 \(\frac{9}{10} > \frac{\sqrt{3}}{2} \iff 3.24 > 3\)），矛盾。
- **情形 3：\(y_1 < y_3 < y_2 < y_4\)。**
记 \(g_1 = x_2-x_1, g_2 = x_3-x_2, g_3 = x_4-x_3, g_4 = 1-x_4 > 0\)（和为 \(1\)），以及 \(h_1 = y_3-y_1, h_2 = y_2-y_3, h_3 = y_4-y_2, h_4 = 1-y_4 > 0\)（和为 \(1\)）。此时各点坐标为 \(P_1=(0,0)\)，\(P_2=(g_1, h_1+h_2)\)，\(P_3=(g_1+g_2, h_1)\)，\(P_4=(1-g_4, 1-h_4)\)。

令 \(t_1 = g_1+g_2-\frac{1}{2}\)，\(t_3 = g_2+g_3-\frac{1}{2}\)，\(s_1 = h_1+h_2-\frac{1}{2}\)，\(s_3 = h_2+h_3-\frac{1}{2}\)，它们均在 \((-\frac{1}{2}, \frac{1}{2})\) 内。利用 \(\sum g_i = \sum h_i = 1\) 可直接写出：
\[g_2 = \frac{1}{2}+t_1-g_1 = \frac{1}{2}+t_3-g_3,\qquad g_4 = \frac{1}{2}-t_1-g_3 = \frac{1}{2}-t_3-g_1,\]
\[h_2 = \frac{1}{2}+s_1-h_1 = \frac{1}{2}+s_3-h_3,\qquad h_4 = \frac{1}{2}-s_1-h_3 = \frac{1}{2}-s_3-h_1.\]
设 \(u(x) = \sqrt{\delta^2 + x - x^2}\)（\(x \in [0, \frac{1}{2}]\)），易见 \(u(x)\) 在 \([0, \frac{1}{2}]\) 上严格递增且 \(u(0) = \delta\)。考察点对 \((P_1, P_2), (P_3, P_4), (P_1, P_3), (P_2, P_4)\)：
- 由 \((P_1, P_2)\) 得 \(g_1^2 \ge \|g_1\|^2 \ge r^2 - \|h_1+h_2\|^2 = \frac{1}{4} + \delta^2 - \left(\frac{1}{2} - |s_1|\right)^2 = \delta^2 + |s_1| - |s_1|^2\)，故 \(g_1 \ge u(|s_1|) \ge \delta\)；
- 同理由 \((P_3, P_4)\) 得 \(g_3 \ge u(|s_3|) \ge \delta\)；由 \((P_1, P_3)\) 得 \(h_1 \ge u(|t_1|) \ge \delta\)；由 \((P_2, P_4)\) 得 \(h_3 \ge u(|t_3|) \ge \delta\)。

现在看 \(t_1, t_3, s_1, s_3\) 的符号：
1. 若 \(t_1, t_3\) 至少有一个 \(\le 0\) 且 \(s_1, s_3\) 至少有一个 \(\le 0\)，则由上面表达式得 \(0 < g_2 \le \frac{1}{2} - \delta = M\) 且 \(0 < h_2 \le M\)。于是对 \((P_2, P_3)\) 有 \(r^2 \le \|g_2\|^2 + \|h_2\|^2 \le g_2^2 + h_2^2 \le 2M^2\)。但 \(r^2 - 2M^2 = \frac{1}{4} + \delta^2 - 2\left(\frac{1}{2} - \delta\right)^2 = \frac{3}{4} - (1-\delta)^2 > 0\)（因 \(0 < 1-\delta < \frac{\sqrt{3}}{2}\)），矛盾！
2. 若 \(t_1, t_3\) 至少有一个 \(\ge 0\) 且 \(s_1, s_3\) 至少有一个 \(\ge 0\)，则同理 \(0 < g_4 \le M\) 且 \(0 < h_4 \le M\)，对 \((P_1, P_4)\) 得 \(r^2 \le g_4^2 + h_4^2 \le 2M^2 < r^2\)，矛盾！

因此只剩下 \(t_1, t_3\) 同号且 \(s_1, s_3\) 与之异号。由对称性（必要时交换 \(x, y\) 坐标），不妨设 \(t_1 > 0, t_3 > 0\) 且 \(s_1 < 0, s_3 < 0\)。令 \(m = \min(t_1, t_3, |s_1|, |s_3|) \in (0, \frac{1}{2})\)。检验 \(m\) 的四种取法：
- 若 \(m = t_1\)，取 \((a, b) = (g_2, h_2)\)，则 \(a = \frac{1}{2} + t_1 - g_1 \le M + m\)，\(b = \frac{1}{2} - |s_1| - h_1 \le \frac{1}{2} - m - u(m)\)；
- 若 \(m = t_3\)，取 \((a, b) = (g_2, h_2)\)，则 \(a = \frac{1}{2} + t_3 - g_3 \le M + m\)，\(b = \frac{1}{2} - |s_3| - h_3 \le \frac{1}{2} - m - u(m)\)；
- 若 \(m = |s_1|\)，取 \((a, b) = (h_4, g_4)\)，则 \(a = \frac{1}{2} + |s_1| - h_3 \le M + m\)，\(b = \frac{1}{2} - t_3 - g_1 \le \frac{1}{2} - m - u(m)\)；
- 若 \(m = |s_3|\)，取 \((a, b) = (h_4, g_4)\)，则 \(a = \frac{1}{2} + |s_3| - h_1 \le M + m\)，\(b = \frac{1}{2} - t_1 - g_3 \le \frac{1}{2} - m - u(m)\)。

于是在所有四种取法中，均存在正数 \(a, b\) 满足 \(a^2 + b^2 \ge r^2\)，\(0 < a \le M + m\)，且 \(0 < b \le \frac{1}{2} - m - u(m)\)。
- **完成情形 3 的最后放缩：**
首先由 \(b > 0\) 得 \(m + u(m) < \frac{1}{2}\)。若 \(m \ge \delta\)，因 \(m < \frac{1}{2}\) 且 \(u\) 在 \([0, \frac{1}{2}]\) 递增，有 \(m + u(m) \ge \delta + u(\delta) = \delta + \sqrt{\delta}\)。但 \(\delta > 1 - \frac{\sqrt{3}}{2} = \left(\frac{\sqrt{3}-1}{2}\right)^2\)，故 \(\delta + \sqrt{\delta} > \left(1 - \frac{\sqrt{3}}{2}\right) + \frac{\sqrt{3}-1}{2} = \frac{1}{2}\)，矛盾！因此必有 \(0 < m < \delta\)（这也排除了 \(\delta = \frac{1}{2}\) 时 \(M=0\) 导致矛盾以外的情形，实际上 \(\delta = \frac{1}{2}\) 时 \(u(m) \ge \frac{1}{2}\) 直接与 \(m+u(m)<\frac{1}{2}\) 矛盾）。

当 \(0 < m < \delta\) 时，利用恒等式
\[(\delta^2 + m - m^2) - \left(\delta + \left(\frac{1}{\sqrt{\delta}} - 1\right)m\right)^2 = m(2\delta - 2\sqrt{\delta} + 1)\left(1 - \frac{m}{\delta}\right) > 0\]
（因 \(2\delta - 2\sqrt{\delta} + 1 = (\sqrt{\delta}-1)^2 + \delta > 0\)），可得 \(u(m) > \delta + \left(\frac{1}{\sqrt{\delta}} - 1\right)m\)。代入 \(b\) 的上界得
\[0 < b < \frac{1}{2} - \delta - \frac{m}{\sqrt{\delta}} = M - \frac{m}{\sqrt{\delta}},\]
从而 \(0 < m < M\sqrt{\delta}\) 且 \(r^2 \le a^2 + b^2 < (M + m)^2 + \left(M - \frac{m}{\sqrt{\delta}}\right)^2\)。

将 \(q(m) = (M + m)^2 + \left(M - \frac{m}{\sqrt{\delta}}\right)^2\) 视为关于 \(m \in [0, M\sqrt{\delta}]\) 的二次函数，其二次项系数 \(1 + \frac{1}{\delta} > 0\)，故最大值必在端点处取得：
- \(q(0) = 2M^2 < r^2\)（已证）；
- \(q(M\sqrt{\delta}) = M^2(1 + \sqrt{\delta})^2\)。记 \(x = \sqrt{\delta} > \frac{\sqrt{3}-1}{2}\)，则 \(x^2 + x - \frac{1}{2} > 0\)，于是
\[0 \le M(1+x) = \left(\frac{1}{2} - x^2\right)(1+x) = \frac{1}{2} - x\left(x^2 + x - \frac{1}{2}\right) < \frac{1}{2},\]
故 \(q(M\sqrt{\delta}) < \frac{1}{4} < r^2\)。
综上必有 \(r^2 < \max(q(0), q(M\sqrt{\delta})) < r^2\)，矛盾！

因此假设不成立，最大的实数 \(r\) 为 \(\frac{\sqrt{6}-\sqrt{2}}{2}\)。

**盲解结论**：\(\frac{\sqrt{6}-\sqrt{2}}{2}\)（即 \(\sqrt{2-\sqrt{3}}\)）

### 2. 对照答案复盘

Turn 1 盲解所得最终答案 \(\frac{\sqrt{6}-\sqrt{2}}{2}\)（即 \(\sqrt{2-\sqrt{3}}\)）及极值构型与参考答案完全一致；上界证明采用了与参考答案不同的有效方法。参考答案在单位正方形内以角点与交点为圆心作半径为 \(d\) 的辅助圆，将剩余星形区域巧妙剖分为直径均不超过 \(d\) 的三个子区域，再借由 \(90^\circ\) 旋转对称性与边界排除导出“四个互不重合区域各含 \(B,C,D\) 中一点”的几何矛盾，构思极为精妙直观；盲解则通过平环面坐标归约，将横纵坐标的相对次序经反射对称压缩为三种置换情形，前两种用间距和迅速否定，第三种借助区间偏离量与二次函数端点最值给出纯代数的严谨证明。两种方法殊途同归，参考答案胜在几何直观与篇幅凝练，盲解的代数分解则避免了复杂的圆弧几何作图构思。

### 3. 困难点与破局关键

- **构造突破 \(\frac{1}{2}\) 门槛的极值点集构型**：在不知道答案的情况下，容易被 \((0,0),(\frac{1}{2},0),(0,\frac{1}{2}),(\frac{1}{2},\frac{1}{2})\) 给出 \(r=\frac{1}{2}\) 的表面对称性迷惑；要突破 \(\frac{1}{2}\)，必须意识到当两个点某维坐标相同时距离至多为 \(\frac{1}{2}\)，从而尝试通过错位让尽量多点对在两维上同时产生贡献（对应扭棱正方形密铺中的正三角形边长 \(d = \frac{\sqrt{6}-\sqrt{2}}{2}\)）。
- **如何利用“恰好各占一区”与旋转对称性制造 \(4>3\) 的矛盾**：仅将剩余星形区域 \(R_d\) 切分成 \(3\) 块直径 \(\le d\) 的区域，只能说明 \(3\) 个点 \(B,C,D\) 恰好每块占 \(1\) 个，还不足以产生矛盾；参考答案最核心的跃迁在于发现“排除边界 \(JK, KL\) 后，绿色三角形 \(\triangle FKJ\) 与蓝色三角形 \(\triangle GKL\) 必各含一点”，再利用正方形的旋转对称性同时得到另外两角的三角形 \(\triangle HLI, \triangle EIJ\) 也各含一点，从而制造出“\(4\) 个不交区域容纳 \(3\) 个点”的抽屉矛盾。

### 4. 问题拆解（教学引导）

- **识别平移不变性与周期本质**：小数距离 \(\sqrt{\|x_1-x_2\|^2 + \|y_1-y_2\|^2}\) 只与坐标的小数部分及平移后的相对位置有关，本质上等价于边长为 \(1\) 的平环面 \(\mathbb{R}^2/\mathbb{Z}^2\) 上的欧氏距离。由此立刻得到平移不变性：总可把其中一个点 \(A\) 移至 \((0,0)\)，把其余三点 \(B,C,D\) 平移进单位正方形 \([0,1)^2\) 中。
- **将小数距离转化为单位正方形内的几何限制区域**：若把单位正方形 \(AXYZ\)（\(A(0,0), X(1,0), Y(1,1), Z(0,1)\)）视作铺开的平面基本域，则任意点 \(P\in [0,1]^2\) 到 \(A\) 的小数距离就是 \(P\) 到四个顶点 \(A,X,Y,Z\) 几何距离的最小值。因此“\(B,C,D\) 与 \(A\) 小数距离大于 \(d\)”等价于它们位于正方形内被四个半径为 \(d\) 的角圆挖去后剩下的中心星形区域。
- **通过平衡等距条件猜测极值构型**：若四点有两两相同的横（或纵）坐标，距离必不超过 \(\frac{1}{2}\)。于是为了最大化 \(r\)，应令 \(B,C\) 分别靠近下、左边界中点（对应角圆交点 \(E,H\)），\(D\) 位于中心偏右上（靠近 \(\odot Y\) 圆弧），使尽可能多的点对同时达到等距，解出 \(\frac{1}{4}+a^2 = 2\left(\frac{1}{2}-a\right)^2\) 即得极值 \(d = \frac{\sqrt{6}-\sqrt{2}}{2}\)。

### 5. 答案拆解（逻辑骨架）

- **第一步：构造极值四点组并验证等距性**（*动机*：先给出紧致的下界构型，并利用极值构型的几何特征反过来指导上界证明中的辅助圆作法。）：令 \(a = 1 - \frac{\sqrt{3}}{2}\)，取 \(A(0,0)\)，\(B\left(a, \frac{1}{2}\right)\)，\(C\left(\frac{1}{2}, a\right)\)，\(D\left(\frac{1}{2}+a, \frac{1}{2}+a\right)\)，逐一验算 \(6\) 对点的小数距离平方均为 \(a^2+\frac{1}{4} = 2\left(\frac{1}{2}-a\right)^2 = 2-\sqrt{3}\)，从而证明 \(r_{\max} \ge \frac{\sqrt{6}-\sqrt{2}}{2}\)。这一构型实际上是平面上正三角形与正方形交替密铺（扭棱正方形密铺）在周期为 \(1\) 下的四个代表顶点。
- **第二步：单位正方形归约与角圆挖空**（*动机*：把无穷平面上的周期距离问题完全等价地压缩到有界单位正方形内的标准欧氏几何区域中。）：设 \(d = \frac{\sqrt{6}-\sqrt{2}}{2}\)，反设存在四点两两小数距离均大于 \(d\)。利用整数平移不变性，将 \(A\) 置于原点 \((0,0)\)，\(B,C,D\) 移入单位正方形 \(AXYZ\)（\(X(1,0),Y(1,1),Z(0,1)\)）内，则 \(B,C,D\) 均位于以 \(A,X,Y,Z\) 为圆心、\(d\) 为半径的四个开圆之外。由于 \(d\) 恰好满足角圆交点 \(E,F,G,H\) 与角点构成正三角形（\(\triangle AEH, \triangle XEF, \triangle YFG, \triangle ZGH\) 边长均为 \(d\)），被挖去四个圆后剩下的中心区域是一个四重对称的曲边星形。
- **第三步：借由次级辅助圆完成直径不超 \(d\) 的三区域剖分**（*动机*：围绕极值点 \(I,J,K,L\) 构造直径不超过 \(d\) 的覆盖剖分，使每块区域最多只能容纳 \(B,C,D\) 中的一个点。）：以星形四个尖点 \(E,F,G,H\) 为圆心、\(d\) 为半径再作四个圆，它们两两交于 \(I,J,K,L\)；由构型计算可知 \(I,J,K,L\) 恰好也落在原本的四个角圆 \(\odot A, \odot X, \odot Y, \odot Z\) 上（即极值构型中第 \(4\) 个点的位置）。利用这些圆弧将中心星形区域划分为三部分：曲边三角形 \(\triangle FKJ\)、\(\triangle GKL\) 以及六边形（曲边多边形）\(EJKLHI\)。由于三块区域的各边弦长均为 \(\frac{\sqrt{6}-\sqrt{2}}{2}d < d\)，且相关圆弧向内凹或半径受控，容易验证每一块区域内部任意两点的几何距离都不超过 \(d\)（进而小数距离也不超过 \(d\)）。
- **第四步：边界排除与旋转对称性导出抽屉矛盾**（*动机*：打破 \(3\) 个区域对应 \(3\) 个点的僵局，利用对称性把“局部必有一点”复制到正方形的四个角上，通过抽屉原理 \(4 > 3\) 一举击穿。）：因为 \(B,C,D\) 两两小数距离大于 \(d\)，上述三块区域每块至多包含 \(B,C,D\) 中的一个点；又因一共恰好有 \(3\) 个点，故三块区域必各含 \(1\) 个点。特别地，没有任何点能落在区域之间的公共边 \(JK, KL\) 上（否则该点同时计入两块区域，剩下至多 \(1\) 个区域却要容纳余下 \(2\) 个点，矛盾）。因此去掉边界 \(JK, KL\) 后的 \(\triangle FKJ\) 与 \(\triangle GKL\) 必各含一点。由正方形绕中心旋转 \(90^\circ\) 的对称性，去掉边界 \(LI, IJ\) 后的 \(\triangle HLI\) 与 \(\triangle EIJ\) 也必各含一点。这样就得到了四个互不相交的三角形区域，每个区域内至少有一个点，但总点数只有 \(3\) 个（\(B,C,D\)），从而导出矛盾，完成证明。

### 6. 易错点分析

- **混淆欧氏距离与小数距离的边界绕回效应**：常见错法——误以为欧氏距离大就代表小数距离大，或忽略横纵坐标差大于 \(\frac{1}{2}\) 时的“绕回”效应。；错因——小数距离定义在模 \(1\) 的周期空间（平环面）上，总有 \(d_{\text{小数}}(P,Q) \le |PQ|\)。因此在同一小区域内“欧氏直径 \(\le d\)”可以推出“小数距离 \(\le d\)”，但反过来若把点放得过远（例如在单位正方形内部距离超过 \(\frac{1}{2}\)），它们在周期意义下反而更近。；避坑策略——先利用“将一点置于原点并把其余点平移入 \([0,1)^2\)”把小数距离化为标准几何距离的最小值 \(\min(|PA|,|PX|,|PY|,|PZ|)\)，或者在代数证明中始终区分 \(\|t\|\) 与 \(t\)，特别注意当 \(t > \frac{1}{2}\) 时 \(\|t\| = 1 - t < t\)。
- **被网格直觉误导而错失真正极值构型**：常见错法——先入为主认为最优构型是正交网格 \((0,0),(\frac{1}{2},0),(0,\frac{1}{2}),(\frac{1}{2},\frac{1}{2})\)，从而误猜答案为 \(\frac{1}{2}\)。；错因——正交网格虽然对称，但相邻点之间有一个坐标差为 \(0\)，导致距离受限于 \(\|x\| \le \frac{1}{2}\)。若将部分点沿坐标方向微调错位（构成类似“扭棱正方形”的正三角形与正方形拼接），可以让两个坐标差同时非零，从而突破 \(\frac{1}{2}\) 达到 \(\frac{\sqrt{6}-\sqrt{2}}{2} \approx 0.5176\)。；避坑策略——看到“两两距离”与可连续调节的坐标时，应主动尝试打破正交网格对称性，例如先固定 \(A(0,0)\)，再观察 \(\odot A, \odot X, \odot Y, \odot Z\) 在单位正方形内挖去后的剩余星形区域的顶点（如 \(E,F,G,H\)）与对称轴上的点，顺藤摸瓜找到全等边长为 \(d\) 的极限构型。
- **区域划分论证中忽略边界归属导致抽屉原理失效**：常见错法——分割区域后直接套用抽屉原理，未排除点恰好落在区域公共边界 \(JK, KL\) 上的情形。；错因——若点 \(B\) 恰好落在 \(\triangle FKJ\) 与多边形 \(EJKLHI\) 的公共边 \(JK\) 上，则 \(B\) 同时属于这两个区域，不能仅凭“每个区域至多含一点”就断定三个区域各有一点并进一步对称推广出四个不交区域。；避坑策略——在划分区域应用抽屉原理前，必须单独排查公共边界线段（如 \(JK, KL\)）是否可能落入点，并用“排除公共边界的开/半开区域”严格写出“四个区域互不重合且各含至少一个点”，确保逻辑无漏洞。

**教学小结**：面对平环面（小数距离或周期边界）上的极值点集问题，核心思路是利用平移不变性将一点固定为参考原点、其余点收入基本单位区域，再结合极值构型的对称节点去构造“直径不超过目标阈值”的覆盖剖分（几何法）或紧致不等式链（代数法）。

---

## 2024 CMO 试题与解答 · 5（`cmo-2024-both-days-combined-q5`）

- **学段**：高中 · **盲解结果**：盲解完全正确
- **教学标签**：训练:技巧进阶 / 构造与反例 / 奇偶与同余 / 放缩与估值 / 易错:隐含假设与越界推广 / 易错:计数重复与漏算 / 易错:边界与退化情形
- **知识专题**：二次剩余与原根 / 功能图构造 / 抽屉原理与估值

### 原题整理

设 \(p\) 为素数，\(f\) 为 \(\{0, 1, \cdots, p-1\}\) 到自身的一个双射，满足当 \(p \mid a^2 - b\) 时，\(|f(a) - f(b)| \leqslant 2024\)。
求证：有无穷多个素数 \(p\) 使得 \(f\) 存在，也有无穷多个素数 \(p\) 使得 \(f\) 不存在。

### 1. 只看原题盲解尝试

**切入思路**：将条件转化为有向（或无向）功能图 \(G_p\) 上的带宽问题：令 \(g(a) = a^2 \bmod p\)（\(a \in \{0, 1, \dots, p-1\}\)），则题目条件等价于寻找双射 \(f\)，使得每条边 \((a, g(a))\) 两端函数值之差不超过 \(2024\)。
1. **存在性（无穷多个素数）**：考虑所有满足 \(p \equiv 3 \pmod 4\) 的素数（由欧几里得式反证法易知有无穷多个）。此时 \(-1\) 是模 \(p\) 的二次非剩余，于是 \(g\) 限制在二次剩余集 \(Q\) 上是一个双射，把 \(Q\) 分解为若干个不相交的有向圈；每个二次非剩余 \(u \in N\) 恰好只指向 \(Q\) 中的一个元素，而 \(0\) 为孤立点。这样 \(G_p\) 的每个非平凡连通分支都是“一个圈上每个点外挂一个度为 \(1\) 的叶子”。通过将圈“对折”编号并把叶子紧挨对应的圈顶点放置，可构造出双射 \(f\) 使得对任意 \(a\) 都有 \(|f(a) - f(g(a))| \leqslant 4 \leqslant 2024\)。
2. **不存在性（无穷多个素数）**：考虑所有满足 \(2^{16} \mid p - 1\) 的素数（利用 \((2q_1 \cdots q_s)^{2^{15}} + 1\) 的素因子可初等证明其有无穷多个）。对这样的素数 \(p\)，模 \(p\) 的乘法群中存在 \(2^{16} = 65536\) 个元素满足 \(x^{2^{16}} \equiv 1 \pmod p\)。对其中每个 \(x\)，在 \(g\) 的作用下至多 \(16\) 步即到达 \(1\)，由三角不等式得 \(|f(x) - f(1)| \leqslant 16 \times 2024 = 32384\)。然而闭区间 \([f(1) - 32384,\, f(1) + 32384]\) 内仅有 \(64769\) 个整数，少于 \(65536\) 个，与 \(f\) 为单射矛盾。

**推演步骤**：
- **第一部分：证明有无穷多个素数 \(p\) 使得 \(f\) 存在。**

首先证明有无穷多个形如 \(4k+3\) 的素数。反设只有有限个满足 \(p \equiv 3 \pmod 4\) 的素数 \(p_1, p_2, \dots, p_r\)（至少有 \(3\)，故 \(r \geqslant 1\)）。考虑正整数 \(M = 4p_1 p_2 \cdots p_r - 1 \geqslant 11\)。由于 \(M\) 为奇数且 \(M \equiv 3 \pmod 4\)，其素因子不能全模 \(4\) 余 \(1\)，必存在素因子 \(q \equiv 3 \pmod 4\)。但 \(q \nmid 4p_1 p_2 \cdots p_r\)，故 \(q \notin \{p_1, \dots, p_r\}\)，矛盾。因此满足 \(p \equiv 3 \pmod 4\) 的素数有无穷多个。
- 对任意素数 \(p \equiv 3 \pmod 4\)，定义映射 \(g : \{0, 1, \dots, p-1\} \to \{0, 1, \dots, p-1\}\) 为 \(g(a) = a^2 \bmod p\)。对 \(a, b \in \{0, 1, \dots, p-1\}\)，\(p \mid a^2 - b\) 当且仅当 \(b = g(a)\)。

显然 \(g(0) = 0\)。令 \(Q = \{g(x) : 1 \leqslant x \leqslant p-1\}\) 为模 \(p\) 的二次剩余集，\(N = \{1, \dots, p-1\} \setminus Q\) 为二次非剩余集。
由于 \(p \equiv 3 \pmod 4\)，\(\frac{p-1}{2}\) 为奇数，故 \(-1 \in N\)：否则若存在 \(u\) 使 \(u^2 \equiv -1 \pmod p\)，由费马小定理得 \(1 \equiv u^{p-1} = (u^2)^{\frac{p-1}{2}} \equiv (-1)^{\frac{p-1}{2}} = -1 \pmod p\)，与 \(p \geqslant 3\) 矛盾。

进一步，\(g|_Q : Q \to Q\) 是双射：若 \(x_1, x_2 \in Q\) 满足 \(g(x_1) = g(x_2)\)，则 \(p \mid (x_1 - x_2)(x_1 + x_2)\)。若 \(x_1 + x_2 = p\)，设 \(x_1 \equiv u^2,\, x_2 \equiv v^2 \pmod p\)，则 \((uv^{-1})^2 \equiv x_1 x_2^{-1} \equiv -1 \pmod p\)，矛盾。故必有 \(x_1 = x_2\)。由于 \(Q\) 为有限集，\(g|_Q\) 为双射。

对每个 \(y \in Q\)，同余方程 \(x^2 \equiv y \pmod p\) 在 \(\{1, \dots, p-1\}\) 中恰有两个解 \(x_0\) 与 \(p - x_0\)。因 \(g|_Q\) 是 \(Q\) 上的双射，恰有一解在 \(Q\) 中，另一解必在 \(N\) 中。由此映射 \(x \mapsto p - x\) 建立 \(Q\) 与 \(N\) 之间的一一对应，故 \(|Q| = |N| = \frac{p-1}{2}\)。
- 将置换 \(g|_Q\) 分解为若干个不相交的轮换 \(C_1, C_2, \dots, C_m\)。对其中任意一个长度为 \(L \geqslant 1\) 的轮换 \(C = (v_0, v_1, \dots, v_{L-1})\)（满足 \(g(v_j) = v_{j+1 \bmod L}\)），令 \(u_j = p - v_{j-1 \bmod L} \in N\)（\(0 \leqslant j \leqslant L-1\)），则
\[g(u_j) = g(v_{j-1 \bmod L}) = v_j.\]
记 \(K_C = \{v_0, \dots, v_{L-1}, u_0, \dots, u_{L-1}\}\)，其大小为 \(2L\)，且 \(\{0\}, K_{C_1}, \dots, K_{C_m}\) 构成 \(\{0, 1, \dots, p-1\}\) 的一个划分。

在每个 \(K_C\) 上构造双射 \(h_C : K_C \to \{0, 1, \dots, 2L-1\}\)：先定义 \(\{0, 1, \dots, L-1\}\) 上的置换 \(r\) 如下：
\[r(j) = \begin{cases} 0, & j = 0, \\ 2j - 1, & 1 \leqslant j \leqslant \lfloor L/2 \rfloor, \\ 2(L - j), & \lfloor L/2 \rfloor + 1 \leqslant j \leqslant L - 1. \end{cases}\]
（当 \(L=1\) 时仅 \(r(0)=0\)；当 \(L=2\) 时 \(r(0)=0, r(1)=1\)。）
逐段验证相邻两项之差 \(|r(j) - r(j+1 \bmod L)|\)：
- \(L=1\) 时为 \(0\)；\(L=2\) 时为 \(1\)；
- \(L \geqslant 3\) 时：\(j=0\) 处为 \(|0 - 1| = 1\)；\(1 \leqslant j \leqslant \lfloor L/2 \rfloor - 1\) 处为 \(|(2j-1)-(2j+1)| = 2\)；\(j = \lfloor L/2 \rfloor\) 处不论 \(L\) 奇偶均有 \(|r(\lfloor L/2 \rfloor) - r(\lfloor L/2 \rfloor + 1)| = 1\)；\(\lfloor L/2 \rfloor + 1 \leqslant j \leqslant L-2\) 处为 \(2\)；\(j = L-1\) 处为 \(|2 - 0| = 2\)。
故对任意 \(L \geqslant 1\) 与任意 \(0 \leqslant j \leqslant L-1\)，均有 \(|r(j) - r(j+1 \bmod L)| \leqslant 2\)。

现令 \(h_C(v_j) = 2r(j)\)，\(h_C(u_j) = 2r(j) + 1\)，则 \(h_C\) 为双射，且：
\[|h_C(v_j) - h_C(g(v_j))| = 2|r(j) - r(j+1 \bmod L)| \leqslant 4, \quad |h_C(u_j) - h_C(g(u_j))| = 1.\]
最后设轮换 \(C_1, \dots, C_m\) 的长度分别为 \(L_1, \dots, L_m\)，令 \(S_{i-1} = 1 + \sum_{t=1}^{i-1} 2L_t\)（\(S_0 = 1\)），定义：
\[f(0) = 0, \qquad f(x) = S_{i-1} + h_{C_i}(x) \quad (x \in K_{C_i},\; 1 \leqslant i \leqslant m).\]
由于 \(\sum_{i=1}^m 2L_i = p - 1\)，\(f\) 是 \(\{0, 1, \dots, p-1\}\) 到自身的双射。且对任意 \(a \in \{0, 1, \dots, p-1\}\)，\(a\) 与 \(g(a)\) 同属 \(\{0\}\) 或同一个 \(K_{C_i}\)，故 \(|f(a) - f(g(a))| \leqslant 4 \leqslant 2024\)。这就证明了存在无穷多个素数 \(p\) 使 \(f\) 存在。
- **第二部分：证明有无穷多个素数 \(p\) 使得 \(f\) 不存在。**

先证满足 \(2^{16} \mid p - 1\) 的素数 \(p\) 有无穷多个。反设只有有限个这样的素数 \(q_1, \dots, q_s\)（若无则取空积为 \(1\)）。令 \(A = 2q_1 \cdots q_s\)，考虑正整数 \(N = A^{2^{15}} + 1 > 1\)。因 \(N\) 为奇数，取 \(N\) 的任一素因子 \(p\)，则 \(p\) 为奇素数且 \(p \nmid A\)。由 \(A^{2^{15}} \equiv -1 \pmod p\) 平方得 \(A^{2^{16}} \equiv 1 \pmod p\)。设 \(d\) 为 \(A\) 模 \(p\) 的阶，则 \(d \mid 2^{16}\)。若 \(d \mid 2^{15}\)，则 \(1 \equiv A^{2^{15}} \equiv -1 \pmod p\)，与 \(p\) 为奇素数矛盾。故 \(d = 2^{16}\)。由费马小定理 \(d \mid p - 1\)，即 \(2^{16} \mid p - 1\)，但 \(p \notin \{q_1, \dots, q_s\}\)，矛盾。因此满足 \(2^{16} \mid p - 1\) 的素数 \(p\) 有无穷多个。
- 对任意满足 \(2^{16} \mid p - 1\) 的素数 \(p\)，取模 \(p\) 的原根 \(\gamma\)，并令
\[H = \left\{ \gamma^{k \cdot \frac{p-1}{2^{16}}} \bmod p \;\middle|\; k = 0, 1, \dots, 2^{16} - 1 \right\} \subseteq \{1, \dots, p-1\}.\]
易知 \(H\) 中元素两两不同，故 \(|H| = 2^{16} = 65536\)，且对每个 \(x \in H\) 均有 \(x^{2^{16}} \equiv 1 \pmod p\)。

假设存在满足题设的双射 \(f\)。对每个 \(x \in H\)，构造序列 \(a_0, a_1, \dots, a_{16} \in \{0, 1, \dots, p-1\}\)，其中 \(a_0 = x\)，\(a_{i+1} = a_i^2 \bmod p\)（\(0 \leqslant i \leqslant 15\)）。由归纳法得 \(a_{16} \equiv x^{2^{16}} \equiv 1 \pmod p\)，又 \(p > 2^{16} > 1\)，故 \(a_{16} = 1\)。

由 \(p \mid a_i^2 - a_{i+1}\) 及题设条件，有 \(|f(a_i) - f(a_{i+1})| \leqslant 2024\)（\(0 \leqslant i \leqslant 15\)）。根据三角不等式：
\[|f(x) - f(1)| = |f(a_0) - f(a_{16})| \leqslant \sum_{i=0}^{15} |f(a_i) - f(a_{i+1})| \leqslant 16 \times 2024 = 32384.\]
这意味着对所有 \(x \in H\)，\(f(x)\) 均落在整数区间 \([f(1) - 32384,\, f(1) + 32384]\) 内。但该区间至多包含
\[2 \times 32384 + 1 = 64769\]
个整数，而 \(|H| = 65536 > 64769\)，这与 \(f\) 是单射矛盾。因此对所有满足 \(2^{16} \mid p - 1\) 的无穷多个素数 \(p\)，均不存在满足题设的双射 \(f\)。

**盲解结论**：证明完成：
1. **存在满足条件的 \(f\) 的素数有无穷多个**：所有满足 \(p \equiv 3 \pmod 4\) 的素数 \(p\)（共有无穷多个）均存在满足题设的双射 \(f\)（事实上可使 \(|f(a) - f(b)| \leqslant 4 \leqslant 2024\)）。
2. **不存在满足条件的 \(f\) 的素数有无穷多个**：所有满足 \(2^{16} \mid p - 1\) 的素数 \(p\)（共有无穷多个）均不存在满足题设的双射 \(f\)。

### 2. 对照答案复盘

第一轮自主解答结果完全正确（outcome: correct），核心思路与官方参考解答高度一致：
1. **存在性部分**：两者均将条件转化为模 \(p\) 平方映射的功能图，利用 \(p \equiv 3 \pmod 4\) 时 \(-1\) 为二次非剩余的性质，证明每个非零连通分支都是“有向圈 + 每个圈顶点外挂一个叶子”，再将圈“对折”交错排布（把叶子紧挨对应的圈顶点），使相邻点差值不超过 \(4 \leqslant 2024\)。自主解答还补充了分段解析式对所有圈长 \(L \geqslant 1\) 的严格验证以及无穷多个 \(p \equiv 3 \pmod 4\) 的初等证明。
2. **不存在性部分**：两者本质相同，均利用 \(2^n\) 个满足 \(x^{2^n} \equiv 1 \pmod p\) 的元素在 \(n\) 步平方后到达 \(1\)，结合三角不等式与 \(2^n > 4048n + 1\) 导出矛盾。差异仅在于取数细节：参考解答取费马数 \(2^{2^n}+1\) 的素因子（使 \(\operatorname{ord}_p(2) = 2^{n+1}\)）并以 \(2^{2^i}\) 的子集乘积直接给出 \(2^n\) 个互异元素（连原根存在性都无需引用）；自主解答则直接固定最小阈值 \(n = 16\)（\(2^{16}=65536 > 64769\)），用 \(A^{2^{15}}+1\) 初等证明有无穷多个素数满足 \(2^{16} \mid p - 1\)，再借助模 \(p\) 原根构造集合 \(H\)。两种方法均严密无误。

### 3. 困难点与破局关键

- **将抽象同余双射转化为功能图结构并用 \(v_2(p-1)\) 分离两类素数**：常数 \(2024\) 看似极大，实则提示了“极小阶数构造（差 \(\leqslant 4\)）”与“指数膨胀反证（\(2^n > 4048n+1\)）”。突破口在于想到通过控制 \(p-1\) 的 \(2\)-adic 赋值 \(v_2(p-1)\) 来分别控制功能图的局部宽度与深度。
- **长圈的“对折”编号以实现常数带宽**：即使看出了每个连通分支是“长 \(k\) 的圈外挂 \(k\) 个叶子”，直接沿圈顺时针编号会使首尾两端差值达到 \(2k-1\)（随 \(p\) 增大而无界）。需要采用“从一端双路折叠交错排列”的技巧，把长圈拉直成带宽为 \(O(1)\) 的线性排布。

### 4. 问题拆解（教学引导）

- **条件图论化：识别功能图与带宽模型**：对每个 \(a \in \{0, 1, \dots, p-1\}\)，满足 \(p \mid a^2 - b\) 的 \(b\) 是唯一的，即 \(b = a^2 \bmod p\)。这自然诱导了一个以 \(\{0, \dots, p-1\}\) 为顶点集、以 \(a \to a^2 \bmod p\) 为有向边的功能图 \(G_p\)。题目要求将顶点重排为 \(0, 1, \dots, p-1\) 的一个排列（双射 \(f\)），使所有相邻顶点的标号之差不超过固定常数 \(2024\)（即图 \(G_p\) 的带宽 \(\leqslant 2024\)）。
- **规模直觉：对比“指数爆炸”与“有界带宽”**：注意到 \(2024\) 是常数而 \(p\) 趋于无穷。若 \(G_p\) 中某点到很多其他点的距离都很短（例如树形分叉很多、直径小而点数多），则三角不等式会迫使标号跨度极大，从而 \(f\) 不存在；反之，若每个连通分支的树深很浅，主要结构是单圈或路径，就有可能通过折叠排列将带宽压在常数以内。
- **数论抓手：锁定 \(p - 1\) 中因子 \(2\) 的幂次**：由于映射是 \(x \mapsto x^2 \bmod p\)，模 \(p\) 乘法群 \(\mathbb{F}_p^\times\)（\(p-1\) 阶循环群）的 \(2\)-Sylow 子群阶数 \(2^{v_2(p-1)}\) 直接决定了“多对一汇入 \(1\)”的二叉树深度：当 \(v_2(p-1) = 1\)（即 \(p \equiv 3 \pmod 4\)）时，二次剩余与非剩余恰好平分且二次映射在二次剩余上为双射，树深仅为 \(1\)；当 \(v_2(p-1)\) 充分大（如 \(p \mid 2^{2^n}+1\) 或 \(2^{16} \mid p-1\)）时，至多 \(n\) 步就能将 \(2^n\) 个元素全部映射到 \(1\)，从而打破常数上界。

### 5. 答案拆解（逻辑骨架）

- **步骤 1：建立功能图模型**（*动机*：将代数整除关系转换为直观的图论标号（带宽）问题，便于利用图形态（圈 vs 树）进行分析。）：把 \(a^2 \equiv b \pmod p\) 视作从 \(a\) 指向 \(b\) 的有向边。\(0\) 是孤立点（仅有自环），其余 \(p-1\) 个点构成若干连通分支。题目即要求给顶点赋予 \(0, 1, \dots, p-1\) 的双射标号，使每条边两端标号差 \(\leqslant 2024\)。
- **步骤 2：存在性方向——解析 \(p \equiv 3 \pmod 4\) 时的连通分支结构**（*动机*：利用 \(p \equiv 3 \pmod 4\) 使二次映射退化为“带刺的圈”，消除深层分叉结构。）：取无穷多个满足 \(p \equiv 3 \pmod 4\) 的素数。此时 \(-1\) 是模 \(p\) 的二次非剩余，故 \(x\) 与 \(p-x\) 中恰有一个二次剩余。由此 \(x \mapsto x^2 \bmod p\) 限制在 \(\frac{p-1}{2}\) 个二次剩余上是入度与出度均为 \(1\) 的双射（分解为若干不相交的有向圈），而每个二次非剩余唯一指向圈上一点且入度为 \(0\)。因此除 \(0\) 外，每个连通分支均为“一个 \(k\) 元圈 + 圈外 \(k\) 个度为 \(1\) 的悬垂点”。
- **步骤 3：存在性方向——对折构造完成局部到整体赋值**（*动机*：通过“对折”消除首尾回绕的大跨度，并将悬垂点穿插进对应圈点旁以保持局部性。）：对每个含 \(2k\) 个点的分支，把连续 \(2k\) 个整数 \(a, a+1, \dots, a+2k-1\) 按“从外向内对折”的方式排成：\(a, a+2, \dots, a+2k-2, a+2k-1, a+2k-3, \dots, a+3, a+1\)。将圈上第 \(i\) 个点（顺时针）放到该序列第 \(2i-1\) 位，其对应的圈外点放到第 \(2i\) 位。这样每条悬垂边两端相邻（差不超过 \(2\)），圈上相邻两点在折叠序列中至多相隔 \(2\) 个圈点（差不超过 \(4\)），远小于 \(2024\)。再把 \(v_0\) 赋为 \(0\)，将 \(1, \dots, p-1\) 分段分给各分支即可。
- **步骤 4：不存在性方向——利用高阶 \(2\) 次幂素因子导出指数爆炸矛盾**（*动机*：构造出指数级规模的顶点集合，使其在常数步（\(n\) 步）平方迭代内全部汇聚于 \(1\)，用三角不等式与抽屉原理击穿 \(2024\) 的限制。）：利用费马数 \(2^{2^n}+1\) 两两互素的性质，对充分大的 \(n\) 取其素因子 \(p\)（满足 \(p \nmid 2^{2^i}+1,\; 0 \leqslant i \leqslant n-1\)），则 \(\operatorname{ord}_p(2) = 2^{n+1}\)。令 \(a_i \equiv 2^{2^i} \pmod p\)（\(1 \leqslant i \leqslant n\)），考察 \(a_1, \dots, a_n\) 中任意若干项之积共 \(2^n\) 个数 \(x_1, \dots, x_{2^n}\)。因指数对应二进制不重不漏且均小于 \(2^{n+1}\)，这 \(2^n\) 个数模 \(p\) 互不同余，且都满足 \(x_k^{2^n} \equiv 1 \pmod p\)。若 \(f\) 存在，反复平方 \(n\) 次后 \(x_k\) 到达 \(1\)，由三角不等式得 \(|f(x_k) - f(1)| \leqslant 2024n\)，于是 \(2^n\) 个互异整数落在仅有 \(4048n + 1\) 个整数的区间内；当 \(n\) 充分大（如 \(n \geqslant 16\)）时 \(2^n > 4048n + 1\)，矛盾。

### 6. 易错点分析

- **误求充要条件导致卡壳**：常见错法——试图刻画使 \(f\) 存在的充要条件，对任意 \(p-1 = 2^k m\) 的混合结构强行分析，导致陷入图带宽判定（NP-hard 级别）的复杂讨论。；错因——一般素数下 \(x \mapsto x^2 \bmod p\) 的功能图由深度为 \(k\) 的二叉树与若干圈复合而成，确定精确带宽阈值 \(2024\) 的充要条件极为困难且完全不必要。；避坑策略——明确题目只要求证明“存在”与“不存在”的素数各无穷多个，果断放弃寻找一般判据，分别在最极端的特殊素数族（\(v_2(p-1)=1\) 与 \(v_2(p-1)\) 充分大）中构造即可。
- **忽视 \(p \equiv 3 \pmod 4\) 与退化圈长 \(L=1\)**：常见错法——忽略 \(p \equiv 3 \pmod 4\) 这一前提，误以为对所有奇素数 \(x \mapsto x^2 \bmod p\) 都是二次剩余集上的双射；或忽略 \(L=1\) 的自环（如 \(1^2 \equiv 1\)）导致索引越界。；错因——若 \(p \equiv 1 \pmod 4\)，则 \(-1\) 是二次剩余，\(a\) 与 \(-a\) 可以同为二次剩余且平方相等，此时 \(x \mapsto x^2\) 在 \(Q\) 上不再是双射，圈上会挂出深度更大的二叉树而非单个叶子。；避坑策略——写出双射时必须显式验证：\(g|_Q\) 在 \(p \equiv 3 \pmod 4\) 下是单射（依赖 \(-1\) 为二次非剩余），并对 \(L=1\)（如 \(1 \mapsto 1\)）和 \(L=2\) 的小圈以及孤立点 \(0\) 单独核对差值界。
- **漏证同余互异性或素数无穷性**：常见错法——在不存在性证明中，构造出若干满足 \(x^{2^n} \equiv 1 \pmod p\) 的数后未严格证明它们模 \(p\) 两两互异，或仅用“对充分大 \(p\)”而未证明存在无穷多个满足 \(2^n \mid p-1\) 的素数。；错因——若未能保证 \(2^n\) 个元素模 \(p\) 互不同余，则无法应用 \(f\) 的单射性得到 \(|f(H)| = 2^n\) 与区间整数个数 \(4048n+1\) 的矛盾。；避坑策略——构造集合 \(H\) 后，必须从“模 \(p\) 阶为 \(2^{n+1}\)（参考解答）”或“原根幂次与 \(2^{16} \mid p-1\)（自主解答）”严格证明 \(H\) 中元素两两模 \(p\) 不同余，且 \(p > 2^n\) 保证 \(1\) 的唯一性。

**教学小结**：面对“要求在无穷多素数上成立或不成立”的数论组合题，不要急于求一般充要条件，而应将整除映射图论化，并抓住 \(p-1\) 的关键素因子（此处为 \(v_2(p-1)\)）构造结构最简单的极端素数族：一边用“对折排列”把单圈带宽压到常数，一边用“\(n\) 步汇于 \(1\) 的指数级点集”配合三角不等式与抽屉原理制造矛盾。

---

## 2024 CMO 试题与解答 · 6（`cmo-2024-both-days-combined-q6`）

- **学段**：高中 · **盲解结果**：盲解正确（不同有效解法）
- **教学标签**：训练:压轴攻坚 / 放缩与估值 / 构造与反例 / 反证与分类讨论 / 易错:计算精度与等价替换 / 易错:边界与退化情形 / 易错:符号与方向
- **知识专题**：代数不等式 / 多项式构造 / 无理数逼近

### 原题整理

已知 \(x_1, x_2, \ldots, x_n\) 为实数，且 \(\sum_{i=1}^n x_i = n\)，\(\sum_{i=1}^n x_i^2 = 2n\)，\(\sum_{i=1}^n x_i^3 = 3n\)。
(1) 求最大的常数 \(C\)，使得对所有 \(n \geqslant 4\)，均有 \(\max\{x_1, x_2, \ldots, x_n\} - \min\{x_1, x_2, \ldots, x_n\} \geqslant C\)。
(2) 证明存在常数 \(\lambda > 0\)，使得对所有 \(n \geqslant 4\)，均有 \(\max\{x_1, x_2, \ldots, x_n\} - \min\{x_1, x_2, \ldots, x_n\} \geqslant C + \lambda n^{-\frac{3}{2}}\)，其中 \(C\) 为第 (1) 问所求值。

### 1. 只看原题盲解尝试

**切入思路**：首先令 \(y_i = x_i - 1\) 将条件中心化为 \(\sum_{i=1}^n y_i = 0\)、\(\sum_{i=1}^n y_i^2 = n\)、\(\sum_{i=1}^n y_i^3 = -n\)，设 \(u = \max y_i > 0\)、\(v = -\min y_i > 0\)，目标极差为 \(R = u + v\)。

第（1）问：利用 \(y_i \in [-v, u]\) 构造三个非负和式 \(S_1 = \frac{1}{n}\sum (u-y_i)(y_i+v) = uv - 1 \geqslant 0\)、\(S_2 = \frac{1}{n}\sum (u-y_i)(y_i+v)^2 = u(v^2+1)-2v+1 \geqslant 0\)、\(S_3 = \frac{1}{n}\sum (u-y_i)^2(y_i+v) = v(u^2+1)-2u-1 \geqslant 0\)。分 \(u \geqslant u_0\) 与 \(0 < u < u_0\)（其中 \(u_0 = \frac{\sqrt{5}-1}{2}\)，\(v_0 = \frac{\sqrt{5}+1}{2}\)）两类，结合单调函数 \(g(u)=u+\frac{2u+1}{u^2+1}\) 与 \(k(v)=v+\frac{2v-1}{v^2+1}\) 证明对一切 \(n \geqslant 4\) 均有 \(u+v \geqslant \sqrt{5}\)。再对任意 \(n \geqslant 4\) 取 \(k = \lceil n p_0 \rceil\)（其中 \(p_0 = \frac{5+\sqrt{5}}{10}\)），通过只取三个值的结构及介值定理构造出满足所有条件的实数列，使得当 \(n \to \infty\) 时极差趋近于 \(\sqrt{5}\)，从而确定最大常数 \(C = \sqrt{5}\)。

第（2）问：设 \(\delta = u + v - \sqrt{5}\)。当 \(\delta > 0.03\) 时由 \(n \geqslant 4\) 显然有 \(\delta > \frac{1}{35} n^{-3/2}\)。当 \(\delta \leqslant 0.03\) 时，由 \(g'(u), k'(v)\) 的下界得到 \(|\alpha| = |u-u_0|\) 与 \(|\beta| = |v-v_0|\) 均为 \(O(\delta)\)，进而 \(S_1 = O(\delta)\)。将指标按与 \(\frac{u-v}{2}\) 的大小关系分成靠近 \(u\) 的集合 \(A\)（设 \(|A|=k\)）和靠近 \(-v\) 的集合 \(B\)，记偏差矩 \(E_j = \frac{1}{n}\sum_{i \in A}(u-y_i)^j\)，\(H_j = \frac{1}{n}\sum_{i \in B}(y_i+v)^j\)，则 \(E_1 + H_1 = O(\delta)\) 且 \(E_2 + H_2 \leqslant n(E_1 + H_1)^2 = O(n \delta^2)\)。将 \(S_2, S_3\) 用 \(E_j, H_j\) 展开并代入 \(\sum y_i = 0\) 中，发现一阶线性项 \(p_0 \alpha - E_1\) 与 \((1-p_0)\beta - H_1\) 相互抵消，从而得到 \(\left|\frac{k}{n} - p_0\right| \leqslant 6\delta^2 + \frac{3}{5}(E_2 + H_2) \leqslant 24 n \delta^2\)。另一方面，因 \(p_0 = \frac{5+\sqrt{5}}{10}\) 是二次无理数，对任意整数 \(k\) 均有 \(\left|\frac{k}{n} - p_0\right| \geqslant \frac{1}{50n^2}\)。联立即得 \(\delta \geqslant \frac{1}{35} n^{-3/2}\)。

**推演步骤**：
- 步骤 1（平移化简）：令 \(y_i = x_i - 1\)（\(i = 1, 2, \ldots, n\)），则有
\[
\sum_{i=1}^n y_i = \sum_{i=1}^n x_i - n = 0,
\]
\[
\sum_{i=1}^n y_i^2 = \sum_{i=1}^n x_i^2 - 2\sum_{i=1}^n x_i + n = 2n - 2n + n = n,
\]
\[
\sum_{i=1}^n y_i^3 = \sum_{i=1}^n x_i^3 - 3\sum_{i=1}^n x_i^2 + 3\sum_{i=1}^n x_i - n = 3n - 6n + 3n - n = -n.
\]
记 \(u = \max_{1 \leqslant i \leqslant n} y_i\)，\(v = -\min_{1 \leqslant i \leqslant n} y_i\)。由于 \(\sum_{i=1}^n y_i = 0\) 且 \(\sum_{i=1}^n y_i^2 = n > 0\)，\(y_i\) 不全为 \(0\)，故 \(u > 0\)，\(v > 0\)，且对每个 \(i\) 都有 \(-v \leqslant y_i \leqslant u\)。待求极差即为 \(R = \max\{x_i\} - \min\{x_i\} = u + v\)。
- 步骤 2（证明第 (1) 问下界 \(R \geqslant \sqrt{5}\)）：由 \(-v \leqslant y_i \leqslant u\) 构造以下三个非负均值：
\[
S_1 = \frac{1}{n}\sum_{i=1}^n (u - y_i)(y_i + v) = \frac{1}{n}\sum_{i=1}^n \left(-y_i^2 + (u - v)y_i + uv\right) = uv - 1 \geqslant 0,
\]
\[
S_2 = \frac{1}{n}\sum_{i=1}^n (u - y_i)(y_i + v)^2 = \frac{1}{n}\sum_{i=1}^n \left(-y_i^3 + (u - 2v)y_i^2 + (2uv - v^2)y_i + uv^2\right) = u(v^2 + 1) - 2v + 1 \geqslant 0,
\]
\[
S_3 = \frac{1}{n}\sum_{i=1}^n (u - y_i)^2(y_i + v) = \frac{1}{n}\sum_{i=1}^n \left(y_i^3 + (v - 2u)y_i^2 + (u^2 - 2uv)y_i + u^2v\right) = v(u^2 + 1) - 2u - 1 \geqslant 0.
\]
记 \(u_0 = \frac{\sqrt{5} - 1}{2}\)，\(v_0 = \frac{\sqrt{5} + 1}{2}\)，注意 \(u_0 v_0 = 1\)，\(v_0 - u_0 = 1\)，\(u_0 + v_0 = \sqrt{5}\)，\(u_0^2 = 1 - u_0\)，\(v_0^2 = 1 + v_0\)。
- 情形 1：若 \(u \geqslant u_0\)，由 \(S_3 \geqslant 0\) 得 \(v \geqslant \frac{2u + 1}{u^2 + 1}\)，故 \(u + v \geqslant g(u) := u + \frac{2u + 1}{u^2 + 1}\)。计算导数：
\[
g'(u) = 1 + \frac{2(u^2 + 1) - 2u(2u + 1)}{(u^2 + 1)^2} = \frac{u^4 - 2u + 3}{(u^2 + 1)^2} = \frac{(u^2 - 1)^2 + 2\left(u - \frac{1}{2}\right)^2 + \frac{3}{2}}{(u^2 + 1)^2} > 0,
\]
故 \(g(u)\) 在 \((0, +\infty)\) 上严格递增，从而 \(u + v \geqslant g(u) \geqslant g(u_0) = u_0 + \frac{2u_0 + 1}{u_0^2 + 1} = u_0 + v_0 = \sqrt{5}\)。
- 情形 2：若 \(0 < u < u_0\)，由 \(S_1 \geqslant 0\) 得 \(v \geqslant \frac{1}{u} > \frac{1}{u_0} = v_0 > \frac{1}{2}\)。再由 \(S_2 \geqslant 0\) 得 \(u \geqslant \frac{2v - 1}{v^2 + 1}\)，故 \(u + v \geqslant k(v) := v + \frac{2v - 1}{v^2 + 1}\)。计算导数：
\[
k'(v) = 1 + \frac{2(v^2 + 1) - 2v(2v - 1)}{(v^2 + 1)^2} = \frac{v^4 + 2v + 3}{(v^2 + 1)^2} > 0 \quad (v > 0),
\]
故 \(k(v)\) 在 \((0, +\infty)\) 上严格递增，从而 \(u + v \geqslant k(v) > k(v_0) = v_0 + \frac{2v_0 - 1}{v_0^2 + 1} = v_0 + u_0 = \sqrt{5}\)。

综上，对所有 \(n \geqslant 4\) 均有 \(\max\{x_i\} - \min\{x_i\} \geqslant \sqrt{5}\)。
- 步骤 3（构造极小序列，确定第 (1) 问最大值 \(C = \sqrt{5}\)）：记 \(p_0 = \frac{v_0}{\sqrt{5}} = \frac{5 + \sqrt{5}}{10} \in (0.72, 0.73)\)。对任意整数 \(n \geqslant 4\)，取 \(k = \lceil n p_0 \rceil\)。因 \(p_0\) 为无理数，有 \(k - 1 < n p_0 < k\)，且由 \(n \geqslant 4\) 可得 \(n p_0 > 2.88 \implies k \geqslant 3\)，\(n(1 - p_0) > 1.08 \implies n - k \geqslant 1\)。
对 \(s \in \left[s_0, 1\right]\)（其中 \(s_0 = -\frac{k - 1}{n - k + 1}\)），定义 \(r(s) = \frac{k - 1 + s}{n - k} > 0\)（满足 \(-r(s) \leqslant s \leqslant 1\)）。考虑由 \(k - 1\) 个 \(1\)、\(1\) 个 \(s\) 和 \(n - k\) 个 \(-r(s)\) 组成的数列，其和为 \(0\)。记
\[
Q(s) = \frac{k - 1 + s^2 + (n - k)r(s)^2}{n} > 0, \qquad C_3(s) = \frac{k - 1 + s^3 - (n - k)r(s)^3}{n}, \qquad F(s) = \frac{C_3(s)}{Q(s)^{3/2}}.
\]
令 \(h(t) = \frac{1 - 2t}{\sqrt{t(1 - t)}} = \sqrt{\frac{1 - t}{t}} - \sqrt{\frac{t}{1 - t}}\)，它在 \((0, 1)\) 上严格递减，且 \(h(p_0) = \sqrt{\frac{u_0}{v_0}} - \sqrt{\frac{v_0}{u_0}} = \frac{u_0 - v_0}{\sqrt{u_0 v_0}} = -1\)。直接计算端值：取 \(p = \frac{k}{n} > p_0\) 与 \(p' = \frac{k - 1}{n} < p_0\)，有
\[
F(1) = h(p) < -1 < h(p') = F(s_0).
\]
由介值定理，存在 \(s \in (s_0, 1)\) 使得 \(F(s) = -1\)。对该 \(s\) 令 \(u = Q(s)^{-1/2}\)，将上述数列各元素乘以 \(u\) 再加 \(1\) 得到 \(x_1, \ldots, x_n\)，则 \(\sum x_i = n\)，\(\sum x_i^2 = 2n\)，\(\sum x_i^3 = 3n\)，且极差为 \(\frac{1 + r(s)}{\sqrt{Q(s)}}\)。
当 \(n \to \infty\) 时，\(p = \frac{k}{n} \to p_0\)，由于 \(s \in (-r(s), 1)\) 有界，故 \(r(s) \to \frac{p_0}{1 - p_0} = \frac{v_0}{u_0}\)，\(Q(s) \to p_0 + (1 - p_0)\frac{v_0^2}{u_0^2} = \frac{1}{u_0^2}\)，于是极差 \(\frac{1 + r(s)}{\sqrt{Q(s)}} \to u_0 + v_0 = \sqrt{5}\)。因此最大常数 \(C = \sqrt{5}\)。
- 步骤 4（第 (2) 问：大偏差情形与小偏差下的局部线性估计）：记 \(\delta = R - \sqrt{5} \geqslant 0\)，令 \(\alpha = u - u_0\)，\(\beta = v - v_0\)，则 \(\alpha + \beta = \delta\)。
若 \(\delta > 0.03\)，因 \(n \geqslant 4\) 时 \(n^{-3/2} \leqslant \frac{1}{8}\)，显然有 \(\delta > 0.03 \geqslant 0.24 n^{-3/2} > \frac{1}{35} n^{-3/2}\)。
以下假设 \(0 \leqslant \delta \leqslant 0.03\)（故 \(R = \sqrt{5} + \delta \in (2.23, 2.27)\)）：
- 若 \(u \geqslant u_0\)，因 \(g(1) = 2.5 > \sqrt{5} + 0.03 \geqslant g(u)\) 且 \(g\) 严格递增，故 \(u \in [u_0, 1)\)。在 \([u_0, 1)\) 上 \(g'(u) \geqslant \frac{3/2}{(1 + 1)^2} = \frac{3}{8}\)，于是 \(\delta \geqslant g(u) - g(u_0) \geqslant \frac{3}{8}\alpha\)，得 \(0 \leqslant \alpha \leqslant \frac{8}{3}\delta\)，且 \(|\beta| = |\delta - \alpha| \leqslant \frac{8}{3}\delta\)。
- 若 \(0 < u < u_0\)，则 \(v > v_0\)。因 \(k(2) = 2.6 > \sqrt{5} + 0.03 \geqslant k(v)\) 且 \(k\) 严格递增，故 \(v \in (v_0, 2)\)。在 \((v_0, 2)\) 上 \(v > \frac{3}{2}\)，\(k'(v) = \frac{v^4 + 2v + 3}{(v^2 + 1)^2} > \frac{(3/2)^4 + 6}{5^2} > \frac{11}{25} > \frac{3}{8}\)，于是 \(\delta \geqslant k(v) - k(v_0) \geqslant \frac{3}{8}\beta\)，得 \(0 < \beta \leqslant \frac{8}{3}\delta\)，且 \(|\alpha| = |\delta - \beta| \leqslant \frac{8}{3}\delta\)。

由此，\(u < 0.70 < 1\)，\(v < 1.70 < 2\)，且
\[
S_1 = uv - 1 = v_0 \alpha + u_0 \beta + \alpha \beta \leqslant (v_0 + u_0)\frac{8}{3}\delta + \frac{64}{9}\delta^2 = \frac{8\sqrt{5}}{3}\delta + \frac{64}{9}\delta^2 < 6.2\delta.
\]
- 步骤 5（第 (2) 问：聚类分解与一阶对消）：将下标集 \(\{1, 2, \ldots, n\}\) 分为 \(A = \{i : y_i \geqslant \frac{u - v}{2}\}\)（设 \(|A| = k\)）与 \(B = \{i : y_i < \frac{u - v}{2}\}\)（则 \(|B| = n - k\)）。对 \(i \in A\) 令 \(\epsilon_i = u - y_i \in \left[0, \frac{R}{2}\right]\)；对 \(i \in B\) 令 \(\eta_i = y_i + v \in \left[0, \frac{R}{2}\right)\)。由于对 \(i \in A\) 有 \(y_i + v \geqslant \frac{R}{2}\)，对 \(i \in B\) 有 \(u - y_i > \frac{R}{2}\)，记 \(E_j = \frac{1}{n}\sum_{i \in A} \epsilon_i^j\)，\(H_j = \frac{1}{n}\sum_{i \in B} \eta_i^j\)（\(j = 1, 2, 3\)），则
\[
\frac{\sqrt{5}}{2}(E_1 + H_1) \leqslant \frac{R}{2}(E_1 + H_1) \leqslant S_1 < 6.2\delta \implies E_1 + H_1 < \frac{12.4}{\sqrt{5}}\delta < 6\delta.
\]
又由 \(\epsilon_i, \eta_i \geqslant 0\)，有
\[
E_2 + H_2 = \frac{1}{n}\left(\sum_{i \in A}\epsilon_i^2 + \sum_{i \in B}\eta_i^2\right) \leqslant \frac{1}{n}\left(\left(\sum_{i \in A}\epsilon_i\right)^2 + \left(\sum_{i \in B}\eta_i\right)^2\right) = n(E_1^2 + H_1^2) \leqslant n(E_1 + H_1)^2 \leqslant 36 n \delta^2.
\]
将 \(S_2, S_3\) 按 \(A, B\) 展开：对 \(i \in A\)，\((u - y_i)(y_i + v)^2 = \epsilon_i(R - \epsilon_i)^2\)，\((u - y_i)^2(y_i + v) = \epsilon_i^2(R - \epsilon_i)\)；对 \(i \in B\)，\((u - y_i)(y_i + v)^2 = (R - \eta_i)\eta_i^2\)，\((u - y_i)^2(y_i + v) = (R - \eta_i)^2\eta_i\)。于是
\[
S_2 = R^2 E_1 - 2R E_2 + E_3 + R H_2 - H_3, \qquad S_3 = R^2 H_1 - 2R H_2 + H_3 + R E_2 - E_3.
\]
另一方面，利用 \(u_0(v_0^2+1)-2v_0+1=0\)、\(v_0(u_0^2+1)-2u_0-1=0\)、\(2u_0 v_0 - 2 = 0\) 及 \(v_0^2 + 1 = \sqrt{5} v_0 = 5 p_0\)、\(u_0^2 + 1 = \sqrt{5} u_0 = 5(1 - p_0)\)，直接展开 \(S_2, S_3\) 得
\[
S_2 = 5 p_0 \alpha + 2 v_0 \alpha \beta + u \beta^2, \qquad S_3 = 5(1 - p_0)\beta + 2 u_0 \alpha \beta + v \alpha^2.
\]
令 \(p = \frac{k}{n}\)，\(\epsilon = p - p_0\)。由 \(\frac{1}{n}\sum_{i=1}^n y_i = p u - (1 - p)v - E_1 + H_1 = 0\) 及 \(p_0 u_0 - (1 - p_0)v_0 = 0\)，整理得
\[
\epsilon R + (p_0 \alpha - E_1) - ((1 - p_0)\beta - H_1) = 0 \implies R|\epsilon| \leqslant |E_1 - p_0 \alpha| + |H_1 - (1 - p_0)\beta|.
\]
注意到 \(R^2 - 5 = 2\sqrt{5}\delta + \delta^2\)，代入 \(R^2 E_1 = S_2 + 2R E_2 - E_3 - R H_2 + H_3\)，有
\[
R^2(E_1 - p_0 \alpha) = 2v_0 \alpha \beta + u \beta^2 - p_0(2\sqrt{5}\delta + \delta^2)\alpha + (2R E_2 - E_3) - (R H_2 - H_3).
\]
类似地，
\[
R^2(H_1 - (1 - p_0)\beta) = 2u_0 \alpha \beta + v \alpha^2 - (1 - p_0)(2\sqrt{5}\delta + \delta^2)\beta + (2R H_2 - H_3) - (R E_2 - E_3).
\]
由于 \(0 \leqslant \epsilon_i, \eta_i \leqslant \frac{R}{2}\)，有 \(0 \leqslant E_3 \leqslant \frac{R}{2} E_2\) 与 \(0 \leqslant H_3 \leqslant \frac{R}{2} H_2\)，因此 \(0 \leqslant 2R E_2 - E_3 \leqslant 2R E_2\)，\(0 \leqslant R H_2 - H_3 \leqslant R H_2\)，两组绝对值之和中的 \(E, H\) 项不超过 \(3R(E_2 + H_2)\)。对其余含 \(\alpha, \beta, \delta\) 的项，结合 \(|\alpha|, |\beta| \leqslant \frac{8}{3}\delta\)、\(u + v < 2.4\)、\(\delta \leqslant 0.03\)，有
\[
\left(2(v_0 + u_0) + u + v\right)\left(\frac{8}{3}\delta\right)^2 + (2\sqrt{5} + \delta)\frac{8}{3}\delta^2 < \left(7 \cdot \frac{64}{9} + 4.53 \cdot \frac{8}{3}\right)\delta^2 < 63\delta^2.
\]
故 \(R^2\left(|E_1 - p_0 \alpha| + |H_1 - (1 - p_0)\beta|\right) \leqslant 63\delta^2 + 3R(E_2 + H_2)\)。两边除以 \(R^3\)（利用 \(R \geqslant \sqrt{5}\)，\(R^2 \geqslant 5\)，\(R^3 \geqslant 5\sqrt{5} > 11\)）并结合 \(n \geqslant 4\) 得
\[
|\epsilon| \leqslant \frac{63}{R^3}\delta^2 + \frac{3}{R^2}(E_2 + H_2) \leqslant 6\delta^2 + \frac{3}{5} \cdot 36 n \delta^2 = (6 + 21.6 n)\delta^2 \leqslant 24 n \delta^2.
\]
- 步骤 6（第 (2) 问：二次无理数丢番图逼近下界）：记整数 \(m = 10k - 5n\)，则
\[
|\epsilon| = \left|\frac{k}{n} - \frac{5 + \sqrt{5}}{10}\right| = \frac{|m - n\sqrt{5}|}{10n}.
\]
若 \(|m - n\sqrt{5}| \geqslant 1\)，则 \(|\epsilon| \geqslant \frac{1}{10n} > \frac{1}{50n^2}\)。若 \(|m - n\sqrt{5}| < 1\)，因 \(\sqrt{5}\) 为无理数且 \(n \geqslant 4\)，整数 \(|m^2 - 5n^2| \geqslant 1\)，而 \(|m + n\sqrt{5}| \leqslant 2n\sqrt{5} + 1 < 5n\)（因 \(2\sqrt{5} < 4.48\) 且 \(n \geqslant 4\)），故
\[
|\epsilon| = \frac{|m^2 - 5n^2|}{10n |m + n\sqrt{5}|} \geqslant \frac{1}{10n \cdot 5n} = \frac{1}{50n^2}.
\]
联立步骤 5 的上界得 \(\frac{1}{50n^2} \leqslant 24 n \delta^2\)，即 \(\delta^2 \geqslant \frac{1}{1200 n^3}\)，从而
\[
\delta \geqslant \frac{1}{20\sqrt{3}} n^{-\frac{3}{2}} > \frac{1}{35} n^{-\frac{3}{2}}.
\]
因此取 \(\lambda = \frac{1}{35} > 0\)，对所有 \(n \geqslant 4\) 结论成立。

**盲解结论**：(1) 最大的常数 \(C = \sqrt{5}\)。
(2) 可取常数 \(\lambda = \frac{1}{35} > 0\)（具体证明见推导步骤），使得对所有 \(n \geqslant 4\) 均有 \(\max\{x_1, x_2, \ldots, x_n\} - \min\{x_1, x_2, \ldots, x_n\} \geqslant \sqrt{5} + \lambda n^{-\frac{3}{2}}\)。

**盲解时的疑虑/卡点**：无未解决的不确定性：第 (1) 问的上下界推导、第 (1) 问中对每个 n>=4 的可构造性及渐近极限、以及第 (2) 问对所有 n>=4 的常数估算均已逐项验证无误。

### 2. 对照答案复盘

独立盲解（Turn 1）与参考解答均完整求出了第（1）问的最大常数 \(C = \sqrt{5}\) 并严格证明了第（2）问的 \(\lambda n^{-\frac{3}{2}}\) 量化下界，核心数学本质高度一致，但在具体实现路径上属于不同的有效方法（`different_valid_method`）：
1. 第（1）问下界：盲解通过构造三个非负矩表达式 \(S_1, S_2, S_3\)，对 \(u \geqslant u_0\) 与 \(0 < u < u_0\) 分类并结合导数证明 \(g(u), k(v)\) 的单调性；参考解答更为精炼，直接由 \(AB \geqslant 1\) 配合单一三次恒等式 \(\sum (y_i + t)\left(y_i - \frac{1}{t}\right)^2 = 0\) 反证得出 \(B \geqslant t\)，避开了求导与分类。
2. 第（1）问构造：盲解对任意 \(n \geqslant 4\) 取 \(k = \lceil n p_0 \rceil\)，利用三值结构与连续函数介值定理一次性完成了“对所有 \(n \geqslant 4\) 的存在性”与“极限趋近 \(\sqrt{5}\)”的构造；参考解答则巧妙利用四点有理配对（\(\pm\) 互为倒数的有理数对自动满足 \(\sum y_i = 0\) 与 \(\sum y_i^2 = n\)），通过线性组合同时满足三次和条件，代数上更为初等。
3. 第（2）问量化下界：两者都捕捉到了相同的底层机制——所有 \(y_i\) 必须向两点 \(-t, \frac{1}{t}\) 聚集、一阶偏离必须相互抵消、以及无理数 \(p_0\) 的丢番图逼近下界 \(\Omega(n^{-2})\)。盲解通过展开 \(S_2, S_3\) 消去 \(\sum y_i = 0\) 中的一阶偏离量 \(E_1, H_1\)，得到显式常数 \(\lambda = \frac{1}{35}\)；参考解答则构造了导数为 \(6(x+t)\left(x - \frac{1}{t}\right)\) 的三次函数 \(h(x) = 2x^3 + 3x^2 - 6x\)，利用其在两点导数为零的性质直接得到二阶偏离下界 \(\sum f^2(y_i) \geqslant \frac{1}{6n}\)。此外需指出，参考解答第 11 页倒数第 4 行出现了笔误，将由 \(10\sum f^2(y_i) \geqslant \frac{5}{3n}\) 应得的 \(\sum f(y_i) \geqslant \frac{1}{\sqrt{6n}}\) 误印成了 \(\sum f(y_i) \geqslant \frac{1}{6n}\)（若按 \(\frac{1}{6n}\) 则在 \(n\) 充分大时不能大于 \(4\lambda_0 n^{-0.5}\)），且第 10 页步骤 ③ 中漏写了 \(y_i\) 超出 \(\left[-t, \frac{1}{t}\right]\) 至多 \(\lambda_0 n^{-1.5}\) 的容差（但不影响主要放缩成立）。

### 3. 困难点与破局关键

- **从两点极值模型反推零点多项式与黄金分割数 \(t\)**：仅凭 \(\sum y_i = 0\)、\(\sum y_i^2 = n\)、\(\sum y_i^3 = -n\) 很难直接猜到 \(\sqrt{5}\)。难点在于先假定极端分布只取两值，反推出特征方程 \(x^2 - x - 1 = 0\) 的两个根 \(\frac{1}{t}\) 与 \(-t\)，再反向构造恰好在 \(-t\) 处变号、在 \(\frac{1}{t}\) 处取双零点的三次多项式 \((y_i + t)\left(y_i - \frac{1}{t}\right)^2\)。
- **同时满足三阶矩条件的逼近构造**：要同时满足一、二、三次和约束，直接解非线性方程组极易陷入繁琐计算。参考解答利用“\(s^2\) 个 \(-\frac{r}{s}\) 与 \(r^2\) 个 \(\frac{s}{r}\) 自动使一次和为 \(0\)、二次和等于个数”的结构，把三条件压缩为单一的线性配比问题；而盲解则通过齐次化与介值定理把三条件压缩为一元连续方程，各有巧思。
- **一阶偏差对消与 \(n^{-3/2}\) 阶数的精确匹配**：如果只用一阶偏离量 \(E_1 + H_1 = O(\delta)\)，无法对抗无理数逼近的 \(\Omega(n^{-2})\) 下界（因为按一阶估计只能得到 \(\delta \geqslant c n^{-2}\)，而非 \(n^{-3/2}\)）。核心飞跃在于发现：由均值与二阶矩约束，一阶偏差在三次函数 \(h(x) = 2x^3 + 3x^2 - 6x\)（满足 \(h'(-t) = h'\left(\frac{1}{t}\right) = 0\)）下完全消去，只剩下二阶项 \(\sum f^2(y_i) \geqslant \frac{1}{6n}\)，再通过 \(\left(\sum f(y_i)\right)^2 \geqslant \sum f^2(y_i)\) 开方后与 \(\sum f(y_i) \leqslant O(n\delta) = O(\lambda_0 n^{-1/2})\) 对撞，才精确锁定 \(n^{-3/2}\) 的量级。

### 4. 问题拆解（教学引导）

- **平移中心化，消除常数均值干扰**：注意到 \(\sum x_i = n\) 意味着均值为 \(1\)，而极差 \(\max x_i - \min x_i\) 具有平移不变性。令 \(y_i = x_i - 1\)，条件立即化简为最干净的中心矩形式：\(\sum y_i = 0\)、\(\sum y_i^2 = n\)、\(\sum y_i^3 = -n\)。
- **用两点分布试探极值结构与 \(n^{-3/2}\) 的成因**：设想 \(y_i\) 仅在两个端点 \(A > 0\) 与 \(-B < 0\) 上分布，由 \(\sum y_i = 0\) 与 \(\sum y_i^2 = n\) 立即得 \(AB = 1\)，代入 \(\sum y_i^3 = -n\) 得 \(A - B = -1\)，即 \(B - A = 1\)。解得 \(B = t = \frac{1+\sqrt{5}}{2}\)，\(A = \frac{1}{t} = \frac{\sqrt{5}-1}{2}\)，极差为 \(\sqrt{5}\)，而 \(A\) 的占比 \(p_0 = \frac{5+\sqrt{5}}{10}\) 为无理数。
- **从理想极值向有限 \(n\) 情形的微扰与逼近分析**：由于 \(n p_0\) 不是整数，有限个实数不可能全部落在 \(-t\) 与 \(\frac{1}{t}\) 上。第（1）问需要构造充分接近该两点分布的数列使极差逼近 \(\sqrt{5}\)；第（2）问则需要把极差超出 \(\sqrt{5}\) 的微扰 \(\delta\) 转化为变量对 \(\left\{-t, \frac{1}{t}\right\}\) 的偏离，进而利用 \(p_0\) 的二次无理数丢番图逼近下界导出 \(\delta \gtrsim n^{-3/2}\)。

### 5. 答案拆解（逻辑骨架）

- **步骤 1：中心化与第（1）问极差下界 \(A + B \geqslant \sqrt{5}\) 的证明**（*动机*：将边界条件转化为多项式的非负性，利用 \(\frac{1}{t}\) 处的重根消去取等以外的自由度。）：令 \(y_i = x_i - 1\)，则 \(\sum y_i = 0\)、\(\sum y_i^2 = n\)、\(\sum y_i^3 = -n\)。设 \(\max y_i = A\)，\(\min y_i = -B\)。由 \((y_i + B)(y_i - A) \leqslant 0\) 求和得 \(n(1 - AB) \leqslant 0\)，即 \(AB \geqslant 1\)。再取 \(t = \frac{1+\sqrt{5}}{2}\)，计算恒等式 \(\sum (y_i + t)\left(y_i - \frac{1}{t}\right)^2 = 0\)；若 \(B < t\) 则每项非负，迫使 \(y_i \equiv \frac{1}{t}\)，与 \(\sum y_i = 0\) 矛盾，故 \(B \geqslant t\)。因此 \(A + B \geqslant B + \frac{1}{B} \geqslant t + \frac{1}{t} = \sqrt{5}\)。这一步仅用一个三次恒等式就锁定了边界 \(B \geqslant t\)，无需任何求导。
- **步骤 2：第（1）问的四值有理配对构造**（*动机*：分别从 \(t\) 的左右两侧逼近，利用两组“自动满足一、二阶矩”的有理配对线性调节三阶矩的符号。）：取 \(r, s, r_0, s_0 \in \mathbb{Z}^+\) 满足 \(t - \epsilon < \frac{r_0}{s_0} < t < \frac{r}{s} < t + \epsilon\)，令 \(n = (s^2 + r^2)k + (s_0^2 + r_0^2)l\)，并在 \(y_i\) 中分别放置 \(s^2 k\) 个 \(-\frac{r}{s}\)、\(r^2 k\) 个 \(\frac{s}{r}\)、\(s_0^2 l\) 个 \(-\frac{r_0}{s_0}\)、\(r_0^2 l\) 个 \(\frac{s_0}{r_0}\)。这组权重保证无论 \(k, l\) 取何值，都有 \(\sum y_i = 0\) 与 \(\sum y_i^2 = n\)；而 \(\sum y_i^3 = -n\) 化为关于 \(k, l\) 的齐次一次方程，且因 \(\frac{r_0}{s_0} < t < \frac{r}{s}\)，\(k, l\) 的系数一正一负，故必存在正整数解 \((k, l)\)。此时 \(A + B = \frac{r}{s} + \frac{s_0}{r_0} \to t + \frac{1}{t} = \sqrt{5}\)，由此确证 \(C = \sqrt{5}\)。
- **步骤 3：第（2）问反证法下的两点聚集与总偏离上界**（*动机*：一旦极差只比 \(\sqrt{5}\) 多 \(O(n^{-1.5})\)，就必须证明所有点只能紧贴 \(-t\) 或 \(\frac{1}{t}\) 分布，从而将整体偏差和压缩到 \(O(n^{-0.5})\)。）：反证假设 \(A + B \leqslant \sqrt{5} + \lambda n^{-1.5}\)（取 \(\lambda_0 = 10^{-10}\)，\(\lambda \leqslant 10^{-100}\)）。先后由 \(B \geqslant t\) 与 \(B + \frac{1}{B} = \sqrt{5} + (B-t)\left(1 - \frac{1}{Bt}\right)\) 推出 \(A \leqslant \frac{1}{t} + \lambda_0 n^{-1.5}\) 且 \(B \leqslant t + \lambda_0 n^{-1.5}\)。再借助 \(\sum (y_i + t)\left(y_i - \frac{1}{t}\right) = 0\)，证明所有 \(y_i\) 与 \(\left\{-t, \frac{1}{t}\right\}\) 的距离 \(f(y_i) = \min\left\{|y_i + t|, \left|y_i - \frac{1}{t}\right|\right\}\) 都不超过 \(\frac{1}{1000}\)；并按 \(y_i\) 是否落在 \(\left[-t, \frac{1}{t}\right]\) 外部分为集合 \(S, T\)，结合 \(i \in S\) 时 \(f(y_i) \leqslant \lambda_0 n^{-1.5}\) 得出偏离总和 \(\sum_{i=1}^n f(y_i) \leqslant 4\sum_{i \in S} f(y_i) \leqslant 4\lambda_0 n^{-0.5}\)。
- **步骤 4：第（2）问二阶误差估计与二次无理数逼近下界**（*动机*：寻找在极端两点处一阶导数为零的三次组合，使一次偏差彻底消去，让二次偏差与无理数的丢番图逼近下界直接对撞。）：设靠近 \(-t\) 的有 \(m\) 个，靠近 \(\frac{1}{t}\) 的有 \(n - m\) 个。构造 \(h(x) = 2x^3 + 3x^2 - 6x\)，其导数 \(h'(x) = 6(x^2 + x - 1)\) 在 \(-t\) 与 \(\frac{1}{t}\) 处均为 \(0\)，故在两点邻域内 \(|h(y_i) - h(-t)| \leqslant 10(y_i + t)^2\)，\(\left|h(y_i) - h\left(\frac{1}{t}\right)\right| \leqslant 10\left(y_i - \frac{1}{t}\right)^2\)。求和得 \(10\sum_{i=1}^n f^2(y_i) \geqslant \left|n - m h(-t) - (n - m)h\left(\frac{1}{t}\right)\right| = 5|t(n - 2m) - (n - m)|\)。利用 \(t = \frac{1+\sqrt{5}}{2}\) 满足 \(t^2 - t - 1 = 0\) 的二次无理数共轭放缩，分子 \(|(n - 2m)^2 + (n - m)(n - 2m) - (n - m)^2| \geqslant 1\)，分母小于 \(3n\)，于是 \(10\sum f^2(y_i) \geqslant \frac{5}{3n}\)，即 \(\sum f^2(y_i) \geqslant \frac{1}{6n}\)。从而 \(\sum_{i=1}^n f(y_i) \geqslant \sqrt{\sum_{i=1}^n f^2(y_i)} \geqslant \frac{1}{\sqrt{6n}} > 4\lambda_0 n^{-0.5}\)（注：参考解答此处笔误写作 \(\frac{1}{6n}\)），产生矛盾！

### 6. 易错点分析

- **忽略无理比例导致的伪构造**：常见错法——在第（1）问中，算出极值点 \(y_i \in \left\{-t, \frac{1}{t}\right\}\) 后直接认为“取 \(m\) 个 \(-t\) 和 \(n-m\) 个 \(\frac{1}{t}\) 即可取等”，忽略了比例 \(p_0 = \frac{5+\sqrt{5}}{10}\) 为无理数、\(n p_0\) 不是整数这一事实。；错因——当 \(y_i\) 仅取 \(-t\) 与 \(\frac{1}{t}\) 两个值时，\(\sum y_i = 0\) 要求两者的个数比为无理数，对任何有限正整数 \(n\) 都不可能成立，因此 \(\sqrt{5}\) 只能作为下确界被无限逼近而不能在有限 \(n\) 下达到。；避坑策略——遇到极端点比例 \(p_0\) 为无理数时，不能直接令全体 \(y_i\) 取该两点，而应通过有理逼近（取 3 个或 4 个相近取值）并用介值定理或整数线性组合调整权重来构造。
- **反比例函数单调区间与符号方向漏判**：常见错法——在得到 \(A \geqslant \frac{1}{B}\) 与 \(B \geqslant t\) 后，错误地认为只需用到基本不等式，或未讨论 \(B\) 与 \(1\) 的大小关系就直接放缩 \(B + \frac{1}{B} \geqslant t + \frac{1}{t}\)。；错因——\(x + \frac{1}{x}\) 只在 \([1, +\infty)\) 上单调递增，在 \((0, 1]\) 上单调递减。若缺少 \(t = \frac{1+\sqrt{5}}{2} > 1\) 这一关键验证，单调放缩的依据就不完整；同样，在第（2）问中 \(y_i\) 落在 \([-t, \frac{1}{t}]\) 内外时 \((y_i + t)(y_i - \frac{1}{t})\) 符号相反，若未分集合 \(S, T\) 讨论会导致放缩反向。；避坑策略——在使用 \(AB \geqslant 1\) 和 \(B \geqslant t\) 之后，务必明确标出 \(B \geqslant t > 1\)，再调用 \(g(x) = x + \frac{1}{x}\) 在 \([1, +\infty)\) 上的单调性（或直接像参考解答那样写恒等式 \(B + \frac{1}{B} - \left(t + \frac{1}{t}\right) = (B - t)\left(1 - \frac{1}{Bt}\right)\)）。
- **放缩精度损失与幂次开方失误**：常见错法——由 \(\sum_{i=1}^n f^2(y_i) \geqslant \frac{1}{6n}\) 错误地直接推出 \(\sum_{i=1}^n f(y_i) \geqslant \frac{1}{6n}\)（参考解答第 11 页末尾亦存在此印刷笔误），或在第（2）问步骤 ③ 中把 \(y_i\) 的范围误写成 \(\left[-t, \frac{1}{t}\right]\) 而遗漏 \(\lambda_0 n^{-\frac{3}{2}}\) 的扰动量。；错因——由于 \(\sum f(y_i)\) 的上界量级为 \(O(n^{-1/2})\)，若把下界错写为 \(\frac{1}{6n}\)，当 \(n\) 充分大时 \(\frac{1}{6n} < 4\lambda_0 n^{-1/2}\)，反证法将彻底失效。同时，若忽略 \(y_i\) 可能略微超出 \(\left[-t, \frac{1}{t}\right]\) 达 \(\lambda_0 n^{-3/2}\)，后续对非负项求和的逻辑就会出现漏洞。；避坑策略——在每一步放缩后检查量纲与 \(n\) 的幂次：由 \(\sum_{i=1}^n f^2(y_i) \geqslant \frac{1}{6n}\) 与 \(f(y_i) \geqslant 0\) 应先写 \(\left(\sum_{i=1}^n f(y_i)\right)^2 \geqslant \sum_{i=1}^n f^2(y_i) \geqslant \frac{1}{6n}\)，开方得 \(\sum_{i=1}^n f(y_i) \geqslant \frac{1}{\sqrt{6}} n^{-\frac{1}{2}}\)，再与上界 \(4\lambda_0 n^{-\frac{1}{2}}\) 比较。

**教学小结**：面对多阶矩约束下的极差最值与定量稳定性问题，应先通过平移与“两点极值模型”锁定特征方程和极限分布，再用在极限点处取重零点（或导数为零）的低次多项式将一阶误差自动消去，将结构误差转化为无理数逼近与平方偏离之间的矛盾。

---

## 2025 CMO 试题解答与评分标准 · 1（`cmo-2025-images-ba37a1fa50-combined-q1`）

- **学段**：高中 · **盲解结果**：盲解完全正确
- **教学标签**：训练:基础热身 / 放缩与估值 / 构造与反例 / 反证与分类讨论 / 易错:边界与退化情形 / 易错:隐含假设与越界推广
- **知识专题**：复数 / 复系数多项式 / 三角不等式与放缩

### 原题整理

定义复数集 \(\mathbb{C}\) 的子集
\[A = \left\{ z \in \mathbb{C} \;\middle|\; z = r\mathrm{e}^{\mathrm{i}\theta},\; r \geqslant 0,\; \theta \in \left[0, \frac{\pi}{41}\right] \right\},\]
\[B = \left\{ z \in \mathbb{C} \;\middle|\; z = x + \mathrm{i}y,\; x, y \in \mathbb{R},\; |x - y| < 2025 \right\},\]
其中 \(\mathrm{i}\) 是虚数单位，\(r\mathrm{e}^{\mathrm{i}\theta} = r(\cos\theta + \mathrm{i}\sin\theta)\)。求所有的一元复系数多项式 \(P(z)\)，使得对任意 \(z \in A\)，都有 \(P(z) \in B\)。（说明：单项式也是多项式。）

### 1. 只看原题盲解尝试

**切入思路**：利用复数的实部表示集合 \(B\) 的条件：对 \(w = x + \mathrm{i}y \in \mathbb{C}\)（\(x, y \in \mathbb{R}\)），有 \(x - y = \operatorname{Re}((1+\mathrm{i})w)\)，从而 \(w \in B\) 当且仅当 \(|\operatorname{Re}((1+\mathrm{i})w)| < 2025\)。利用这一表达式分析多项式 \(P(z)\) 当 \(|z| = r \to +\infty\) 时的主项行为：若 \(\deg P = n \geqslant 1\)，则在辐角区间 \(\theta \in \left[0, \frac{\pi}{41}\right]\) 内必能找到至少一个方向 \(\theta_0\)，使得最高次项对 \(\operatorname{Re}((1+\mathrm{i})P(r\mathrm{e}^{\mathrm{i}\theta_0}))\) 的贡献系数非零，从而当 \(r\) 充分大时 \(|\operatorname{Re}((1+\mathrm{i})P(r\mathrm{e}^{\mathrm{i}\theta_0}))| \geqslant 2025\)，产生矛盾。因此 \(P(z)\) 只能是常值多项式，且常数项必须属于 \(B\)。

**推演步骤**：
- 转化集合 \(B\) 的条件：对任意复数 \(w = x + \mathrm{i}y\)（\(x, y \in \mathbb{R}\)），计算得 \((1+\mathrm{i})w = (x - y) + \mathrm{i}(x + y)\)，因此 \(x - y = \operatorname{Re}((1+\mathrm{i})w)\)。于是 \(P(z) \in B\) 等价于 \(|\operatorname{Re}((1+\mathrm{i})P(z))| < 2025\)。
- 反证多项式次数不为正：假设存在满足条件的多项式 \(P(z) = \sum_{k=0}^{n} a_k z^k\)，其中 \(n \geqslant 1\) 且 \(a_n \neq 0\)（\(a_k \in \mathbb{C}\)）。记 \((1+\mathrm{i})a_n = p + \mathrm{i}q\)（\(p, q \in \mathbb{R}\)）。由于 \(1+\mathrm{i} \neq 0\) 且 \(a_n \neq 0\)，故 \(p, q\) 不同时为 \(0\)。
- 选取使最高次项实部非零的辐角 \(\theta_0 \in \left[0, \frac{\pi}{41}\right]\)：对于 \(z = r\mathrm{e}^{\mathrm{i}\theta} \in A\)，有
\[\operatorname{Re}((1+\mathrm{i})a_n z^n) = r^n \operatorname{Re}\big((p + \mathrm{i}q)(\cos n\theta + \mathrm{i}\sin n\theta)\big) = r^n (p\cos n\theta - q\sin n\theta).\]
若 \(p \neq 0\)，取 \(\theta_0 = 0 \in \left[0, \frac{\pi}{41}\right]\)，则 \(c := p\cos(n\theta_0) - q\sin(n\theta_0) = p \neq 0\)；若 \(p = 0\)，则必有 \(q \neq 0\)，此时因 \(n \geqslant 1\)，可取 \(\theta_0 = \frac{\pi}{41n} \in \left(0, \frac{\pi}{41}\right]\)，则 \(c := p\cos(n\theta_0) - q\sin(n\theta_0) = -q\sin\frac{\pi}{41} \neq 0\)。总之，存在 \(\theta_0 \in \left[0, \frac{\pi}{41}\right]\) 使得 \(c = \operatorname{Re}((1+\mathrm{i})a_n \mathrm{e}^{\mathrm{i}n\theta_0}) \neq 0\)。
- 估计其余项并导出矛盾：设 \(M = \sum_{k=0}^{n-1} \sqrt{2}|a_k| \geqslant 0\)。对 \(r \geqslant 1\) 及 \(z = r\mathrm{e}^{\mathrm{i}\theta_0} \in A\)，利用 \(|\operatorname{Re}(w)| \leqslant |w|\) 得
\[\left|\sum_{k=0}^{n-1} \operatorname{Re}((1+\mathrm{i})a_k z^k)\right| \leqslant \sum_{k=0}^{n-1} |(1+\mathrm{i})a_k z^k| = \sum_{k=0}^{n-1} \sqrt{2}|a_k| r^k \leqslant M r^{n-1}.\]
由三角不等式，
\[|\operatorname{Re}((1+\mathrm{i})P(z))| \geqslant |c|r^n - M r^{n-1} = r^{n-1}(|c|r - M).\]
取 \(r = \max\left\{1, \frac{M + 2025}{|c|}\right\}\)，则 \(z = r\mathrm{e}^{\mathrm{i}\theta_0} \in A\)，且 \(r^{n-1} \geqslant 1\)、\(|c|r - M \geqslant 2025\)，故 \(|\operatorname{Re}((1+\mathrm{i})P(z))| \geqslant 2025\)，与 \(P(z) \in B\) 矛盾。从而 \(P(z)\) 不可能是次数 \(\geqslant 1\) 的多项式。
- 检验常值多项式：若 \(P(z) \equiv c_0\)（常数，包括零多项式），记 \(c_0 = x_0 + \mathrm{i}y_0\)（\(x_0, y_0 \in \mathbb{R}\)），则对任意 \(z \in A\) 都有 \(P(z) = c_0\)，故 \(P(z) \in B\) 成立当且仅当 \(|x_0 - y_0| < 2025\)，即 \(c_0 \in B\)。

**盲解结论**：所有满足条件的一元复系数多项式为全部常值多项式 \(P(z) \equiv c\)（其中 \(c \in B\)），即
\[P(z) = x_0 + \mathrm{i}y_0 \quad (x_0, y_0 \in \mathbb{R},\; |x_0 - y_0| < 2025).\]

### 2. 对照答案复盘

盲解结果与参考解答完全一致，均得出所有满足条件的多项式为取值在 \(B\) 内的常值多项式 \(P(z) \equiv c\)（\(c \in B\)）。在证明非常值多项式不满足条件时，双方核心思路相同——均利用主项主导原理，在扇形辐角区间 \(\left[0, \frac{\pi}{41}\right]\) 内选取使最高次项对 \(\operatorname{Re} - \operatorname{Im}\) 贡献非零的辐角，并在 \(|z| = r \geqslant 1\) 时通过三角不等式显式构造足够大的 \(r\) 导出矛盾。细微差异在于：参考解答直接分别对 \(\operatorname{Re} P(z)\) 与 \(\operatorname{Im} P(z)\) 使用三角不等式，并从存在性角度取 \(\theta_1 \in \left[0, \frac{\pi}{41}\right]\) 使 \(\theta_0 + n\theta_1 \neq \frac{\pi}{4} + k\pi\)；而盲解利用恒等式 \(x - y = \operatorname{Re}((1+\mathrm{i})w)\) 将两项合并，并显式构造了 \(\theta_0 \in \left\{0, \frac{\pi}{41n}\right\}\)。两种做法均显式约束了 \(r \ge 1\)（避免了评分标准中 M1–M4 列出的跳步扣分项），逻辑严谨完整。

### 3. 困难点与破局关键

- **从定性极限直觉到定量不等式的严格落地**：很多同学能直观看出“\(|z|\) 很大时 \(P(z) \approx a_0 z^n\)”，甚至直接写“当 \(r \to \infty\) 时 \(\arg P(z) \to \arg(a_0 z^n)\)”，但在竞赛评分中（见评分标准 M2、M3）缺乏定量证明会被重扣分。难点在于用反向三角不等式显式分离主项与低次余项，并给出具体的大 \(r\) 下界。
- **保证主项的 \(\operatorname{Re}(a_0 z^n) - \operatorname{Im}(a_0 z^n)\) 不恒为零**：若题目把 \(A\) 换成单条射线（如正实轴 \(\theta = 0\)），则 \(P(z) = (1+\mathrm{i})z\) 就恒在直线 \(y = x\) 上而满足条件！本题的关键在于 \(A\) 包含一整段非退化的角度区间 \(\left[0, \frac{\pi}{41}\right]\)，因此对任意 \(n \geqslant 1\)，\(n\theta\) 跨过长度 \(\frac{n\pi}{41} > 0\) 的区间，必然能避开离散点集 \(\left\{\frac{\pi}{4} + k\pi\right\}\)（或显式取 \(0\) 与 \(\frac{\pi}{41n}\) 之一）。

### 4. 问题拆解（教学引导）

- **几何化解读集合 \(A\) 与集合 \(B\)**：在复平面上，\(A\) 是从原点出发、张角为 \(\frac{\pi}{41}\) 的无界闭扇形区域（包含任意大模长的复数）；\(B\) 是由 \(|x - y| < 2025\) 界定的、沿直线 \(y = x\) 延伸的无限长开带状区域。因此条件 \(P(A) \subseteq B\) 要求一个无穷扇形的像完全落入一条有界宽度的斜带内。
- **直觉猜想并锁定主项矛盾**：多项式在 \(|z| \to \infty\) 时的性态由最高次项 \(a_0 z^n\) 主导：当 \(z\) 沿扇形内不同射线趋于无穷时，\(a_0 z^n\) 的模长按 \(r^n\) 增长，且其辐角随 \(\theta\) 变化，不可能一直紧贴带状区域 \(B\) 的延伸方向（直线 \(y = x\)，对应辐角 \(\frac{\pi}{4} + k\pi\)）。由此猜想只有常值多项式满足要求。
- **明确证明目标与关键转化**：需将“直觉上不可能一直沿 \(y=x\) 方向走”转化为严格的不等式证明：先在 \(\left[0, \frac{\pi}{41}\right]\) 中选定一个偏离 \(y=x\) 方向的辐角 \(\theta_1\)，再把 \(|\operatorname{Re} P(z) - \operatorname{Im} P(z)|\) 拆为主项下界减去余项上界，最后取足够大的 \(r > 1\) 使该下界超过 \(2025\)。

### 5. 答案拆解（逻辑骨架）

- **分类并处理常值多项式情形**（*动机*：题目特别提示“单项式也是多项式”，提示不要遗漏零次多项式（常数，含零多项式）。）：设 \(P(z) \equiv c\)（\(c\) 为复常数）。由于对任意 \(z \in A\) 均有 \(P(z) = c\)，故 \(P(z) \in B\) 恒成立当且仅当 \(c \in B\)。评分标准中明确指出答案完整写出即可得该部分分数。
- **假设 \(\deg P = n \geqslant 1\) 并选定非临界辐角 \(\theta_1\)**（*动机*：要让 \(|x - y|\) 随 \(r\) 趋于无穷，必须先确保最高次项 \(a_0 z^n\) 本身的 \(|\operatorname{Re}(a_0 z^n) - \operatorname{Im}(a_0 z^n)|\) 不为零，即避免 \(a_0 z^n\) 落在直线 \(y = x\) 上。）：记 \(P(z) = a_0 z^n + a_1 z^{n-1} + \dots + a_n\)（\(n \geqslant 1,\; a_0 \neq 0\)），设 \(a_0\) 的辐角为 \(\theta_0\)。当 \(\theta_1\) 遍历 \(\left[0, \frac{\pi}{41}\right]\) 时，\(\theta_0 + n\theta_1\) 取遍长度为 \(\frac{n\pi}{41} > 0\) 的闭区间，故必存在 \(\theta_1 \in \left[0, \frac{\pi}{41}\right]\) 使得 \(\theta_0 + n\theta_1 \neq \frac{\pi}{4} + k\pi\)（\(k \in \mathbb{Z}\)）。此时 \(\lambda := |\cos(\theta_0 + n\theta_1) - \sin(\theta_0 + n\theta_1)| > 0\)，从而对 \(z = r\mathrm{e}^{\mathrm{i}\theta_1}\)，主项满足 \(|\operatorname{Re}(a_0 z^n) - \operatorname{Im}(a_0 z^n)| = \lambda |a_0| r^n\)。
- **利用 \(|z| > 1\) 控制低次余项并反向三角不等式放缩**（*动机*：需要证明低次项的增长速度严格慢于 \(r^n\)，以便在 \(r\) 足够大时被主项压制。）：记余项 \(R(z) = a_1 z^{n-1} + \dots + a_n\)。当 \(r = |z| > 1\) 时，有 \(r^k \leqslant r^{n-1}\)（\(0 \leqslant k \leqslant n-1\)），故 \(|R(z)| \leqslant (|a_1| + \dots + |a_n|) r^{n-1}\)。结合 \(|\operatorname{Re} R(z)| \leqslant |R(z)|\) 与 \(|\operatorname{Im} R(z)| \leqslant |R(z)|\)，利用反向三角不等式得
\[|\operatorname{Re} P(z) - \operatorname{Im} P(z)| \geqslant \lambda |a_0| r^n - 2(|a_1| + \dots + |a_n|) r^{n-1} = r^n\left(\lambda |a_0| - 2\frac{|a_1| + \dots + |a_n|}{r}\right).\]
- **显式取定足够大的 \(r\) 导出矛盾**（*动机*：同时保证括号内的主项系数留有至少一半的余量，且整体乘积大于 \(2025\)，避免任何模糊的极限语言。）：取 \(r > \max\left\{1,\; \frac{4(|a_1| + \dots + |a_n|)}{\lambda |a_0|},\; \left(\frac{2 \cdot 2025}{\lambda |a_0|}\right)^{1/n}\right\}\)。一方面括号内大于 \(\frac{1}{2}\lambda |a_0|\)，另一方面 \(r^n > \frac{2 \cdot 2025}{\lambda |a_0|}\)，相乘即得 \(|\operatorname{Re} P(z) - \operatorname{Im} P(z)| > 2025\)，说明 \(z = r\mathrm{e}^{\mathrm{i}\theta_1} \in A\) 但 \(P(z) \notin B\)，矛盾！故非常值多项式均不成立。

### 6. 易错点分析

- **用极限直观代替严格估计（评分标准 M2、M3）**：常见错法——直接写出“当 \(|z| \to \infty\) 时，\(\arg P(z) - \arg(a_0 z^n) \to 0\) 且 \(|P(z)| \to \infty\)，故 \(P(z)\) 必离开 \(B\)”，却没有用三角不等式证明余项与主项之比趋于 \(0\)。；错因——复数辐角在接近奇点或大模长下的渐近行为并非无条件成立的公理，在竞赛解答中未经证明直接引用会被判为跳步（评分标准 M2 扣 6 分、M3 扣 3 分）。；避坑策略——在涉及多项式主项主导时，务必显式拆出 \(P(z) - a_0 z^n\)，通过 \(|z| > 1\) 放大为 \(\left(\sum_{k=1}^n |a_k|\right)|z|^{n-1}\)，再用反向三角不等式给出明确的下界。
- **放缩余项时遗漏 \(|z| > 1\)（或 \(r \geqslant 1\)）的前提（评分标准 M1）**：常见错法——在写下 \(|a_1 z^{n-1} + \dots + a_n| \leqslant (|a_1| + \dots + |a_n|)|z|^{n-1}\) 时，未明确说明需要 \(|z| \geqslant 1\)（或 \(|z| > 1\)）。；错因——当 \(0 < |z| < 1\) 时，次数越低模长越大，\(r^k \leqslant r^{n-1}\) 的不等号方向恰好相反（此时 \(1 \leqslant r^{n-1}\) 不成立），导致放缩不成立。；避坑策略——在使用 \(r^k \leqslant r^{n-1}\)（\(0 \leqslant k \leqslant n-1\)）之前，先明确限定 \(r > 1\)（或取 \(r = \max\{1, \dots\}\)）。
- **直接套用实系数多项式结论而未证明（评分标准 M4）**：常见错法——固定 \(\theta_1\) 后将 \(g(r) = \operatorname{Re} P(r\mathrm{e}^{\mathrm{i}\theta_1}) - \operatorname{Im} P(r\mathrm{e}^{\mathrm{i}\theta_1})\) 视为关于 \(r\) 的实系数多项式，直接断言“非常数实多项式在 \(r \to \infty\) 时绝对值趋于无穷”而不加证明。；错因——一方面若未验证 \(\theta_1\) 使 \(r^n\) 的系数非零，\(g(r)\) 甚至可能退化为常数；另一方面竞赛评分要求对基本的多项式无界性给出至少一步三角不等式验证。；避坑策略——先证明存在 \(\theta_1\) 使最高次项系数非零，再用同一套三角不等式给 \(|g(r)|\) 写出显式下界。
- **忽略常值多项式或把“单项式”误解为 \(cz^k\)**：常见错法——看到括号提示“单项式也是多项式”后，误以为答案中应包含某种高次单项式，或漏掉常值多项式 \(P(z) \equiv c\)（包含 \(P(z) \equiv 0\)）。；错因——题干的说明是为了提醒常数（零次单项式）也算多项式，避免考生因“多项式必须有多项”的误区而困惑；而所有次数 \(\geqslant 1\) 的单项式在扇形上同样无法落入 \(B\)。；避坑策略——研究多项式函数问题时，习惯性先单独检验 \(\deg P \leqslant 0\)（常数与零多项式）的边界情况，再讨论 \(\deg P \geqslant 1\)。

**教学小结**：处理复平面上无限区域映射到有界带状（或有界）区域的多项式问题时，核心抓手是“角度避让 + 主项主导”：利用非退化辐角区间保证最高次项不落入临界方向，再在 \(|z| > 1\) 的前提下用反向三角不等式定量压制低次余项。

---

## 2025 CMO 试题解答与评分标准 · 2（`cmo-2025-images-ba37a1fa50-combined-q2`）

- **学段**：高中 · **盲解结果**：盲解正确（不同有效解法）
- **教学标签**：训练:技巧进阶 / 放缩与估值 / 辅助线与几何变换 / 变量代换与重参数化 / 易错:边界与退化情形 / 易错:充分性与必要性混淆 / 易错:隐含假设与越界推广
- **知识专题**：平面几何 / 圆幂与根心定理 / 相似三角形

### 原题整理

设凸四边形 \(ABCD\) 内接于圆心为 \(O\)、半径为 \(1\) 的圆，且满足 \(\angle ABC < \angle BCD < 90^\circ\)。设 \(P\) 为直线 \(BA\) 与 \(CD\) 的交点，\(Q\) 为对角线 \(AC\) 与 \(BD\) 的交点。已知线段 \(BC\) 上存在一点 \(K\)，使得 \(P, A, K, D\) 四点共圆，且 \(KB \cdot KC = \frac{1}{2} OP^2\)。过点 \(Q\) 作 \(BC\) 的垂线，与直线 \(OP\) 交于点 \(T\)。
(1) 求 \(OP\) 的所有可能值；
(2) 求 \(TB + TC\) 的所有可能值。

### 1. 只看原题盲解尝试

**切入思路**：第（1）问先利用凸四边形及 \(\angle ABC < \angle BCD < 90^\circ\) 确定点 \(P\) 位于单位圆 \(\omega=(O,1)\) 外部，再由 \(P,A,K,D\) 四点共圆导角证得 \(\triangle PKA \sim \triangle PBK\)，从而得到 \(PK^2 = PA\cdot PB = OP^2 - 1\)。结合圆幂定理 \(KB\cdot KC = 1 - OK^2 = \frac{1}{2}OP^2\) 与 \(\triangle OKP\) 的中线长公式，推出 \(K\) 恰好为线段 \(OP\) 的中点，进而唯一确定 \(OP = \frac{2\sqrt{3}}{3}\)。第（2）问以 \(K\) 为原点、\(BC\) 为 \(x\) 轴建立平面直角坐标系，利用圆的极点极线（Brocard 定理）求出 \(x_Q = x_T\)，进而通过坐标恒等变形发现 \(TB = \sqrt{3}\,KB\)、\(TC = \sqrt{3}\,KC\)，于是 \(TB + TC = \sqrt{3}\,BC\)；再由四边形存在与凸性条件精确刻画参数范围，求得 \(TB + TC\) 的取值范围。

**推演步骤**：
- **第（1）问：确定 \(P\) 的位置并证明 \(PK^2 = OP^2 - 1\)。**
因为 \(ABCD\) 是凸四边形，点 \(A, D\) 在直线 \(BC\) 的同侧，且线段 \(AB\) 与 \(CD\) 不相交。又 \(\angle ABC + \angle BCD < 90^\circ + 90^\circ = 180^\circ\)，故射线 \(BA\) 与 \(CD\) 交于 \(P\)，且 \(A\) 严格在线段 \(PB\) 上，\(D\) 严格在线段 \(PC\) 上。因此 \(P\) 在单位圆 \(\omega = (O, 1)\) 外，\(OP > 1\)，由圆幂定理得
\[ PA \cdot PB = PD \cdot PC = OP^2 - 1 > 0. \]
由于 \(KB \cdot KC = \frac{1}{2} OP^2 > 0\)，点 \(K\) 严格在线段 \(BC\) 上，即 \(K\) 在 \(\angle BPC\) 内部，于是 \(P, A, K, D\) 按顺序在圆 \((PAKD)\) 上。因此点 \(K, D\) 在直线 \(PA\) 同侧，从而 \(\angle PKA = \angle PDA\)。又因为 \(A, B, C, D\) 共圆，所以 \(\angle PDA = 180^\circ - \angle ADC = \angle ABC = \angle PBK\)。结合公共角 \(\angle APK = \angle KPB\)，有 \(\triangle PKA \sim \triangle PBK\)，于是
\[ PK^2 = PA \cdot PB = OP^2 - 1. \]
- **证明 \(K\) 为 \(OP\) 的中点并求 \(OP\)。**
因为 \(K\) 在单位圆 \(\omega\) 的弦 \(BC\) 上，由相交弦定理（圆幂定理）有
\[ KB \cdot KC = 1 - OK^2 \implies OK^2 = 1 - KB \cdot KC = 1 - \frac{1}{2} OP^2. \]
设 \(M_0\) 为线段 \(OP\) 的中点。在 \(\triangle OKP\) 中应用平行四边形恒等式（中线长公式），得
\[ OK^2 + PK^2 = 2 K M_0^2 + \frac{1}{2} OP^2. \]
将 \(OK^2 = 1 - \frac{1}{2} OP^2\) 与 \(PK^2 = OP^2 - 1\) 代入上式：
\[ \left(1 - \frac{1}{2} OP^2\right) + (OP^2 - 1) = 2 K M_0^2 + \frac{1}{2} OP^2 \implies 2 K M_0^2 = 0 \implies K = M_0. \]
故 \(K\) 为 \(OP\) 的中点，即 \(OK = \frac{1}{2} OP\)。代回 \(OK^2 = 1 - \frac{1}{2} OP^2\) 得
\[ \frac{1}{4} OP^2 = 1 - \frac{1}{2} OP^2 \implies \frac{3}{4} OP^2 = 1 \implies OP = \frac{2\sqrt{3}}{3}. \]
（下方第（2）问同时验证了满足条件且 \(OP = \frac{2\sqrt{3}}{3}\) 的图形确实存在。）
- **第（2）问：建立坐标系并充要刻画满足题设的构型范围。**
以 \(K(0, 0)\) 为原点，射线 \(BC\) 为 \(x\) 轴正方向建立直角坐标系，使点 \(P\) 位于上半平面（\(y > 0\)）。由第（1）问知 \(K\) 是 \(OP\) 的中点，且 \(OK = \frac{\sqrt{3}}{3}\)，故可设 \(P(c, s)\)、\(O(-c, -s)\)，其中 \(s > 0\) 且 \(c^2 + s^2 = \frac{1}{3}\)。
记 \(m = \sqrt{1 - s^2} > 0\) 为弦 \(BC\) 长的一半，因 \(O\) 在 \(BC\) 的垂直平分线上，\(BC\) 中点为 \(N(-c, 0)\)，故
\[ B(-c - m, 0), \qquad C(-c + m, 0). \]
由 \(A, D\) 分别严格在线段 \(PB, PC\) 上，条件 \(\angle ABC < \angle BCD < 90^\circ\) 即 \(\angle PBC < \angle PCB < 90^\circ\)。
- 由 \(\angle PBC < 90^\circ\) 和 \(\angle PCB < 90^\circ\)，\(P\) 在 \(BC\) 上的投影 \(M(c, 0)\) 严格位于线段 \(BC\) 上，即 \(-c - m < c < -c + m\)；
- 由 \(\angle PBC < \angle PCB\)，有 \(BM > CM\)，即 \(2c + m > m - 2c \iff c > 0\)。

反之，对任意满足 \(c > 0, s > 0\) 且 \(c^2 + s^2 = \frac{1}{3}\) 的参数，令 \(A, D\) 分别为直线 \(PB, PC\) 与圆 \(\omega\) 的另一交点。因 \(P\) 在圆外且 \(PB > PC\)，\(A\) 严格在线段 \(PB\) 上且 \(D\) 严格在线段 \(PC\) 上当且仅当 \(PA < PB\) 且 \(PD < PC\)，即 \(PC^2 > PD \cdot PC = \frac{1}{3}\)。计算得
\[ PC^2 = (m - 2c)^2 + s^2 = (1 - s^2) + 4\left(\frac{1}{3} - s^2\right) + s^2 - 4mc = \frac{7}{3} - 4s^2 - 4mc. \]
因此 \(PC^2 > \frac{1}{3}\) 等价于
\[ 1 - 2s^2 > 2mc = 2\sqrt{(1 - s^2)\left(\frac{1}{3} - s^2\right)}. \]
因为 \(s^2 = \frac{1}{3} - c^2 < \frac{1}{3} < \frac{1}{2}\)，左端 \(1 - 2s^2 > 0\)，两边平方化简得
\[ (1 - 2s^2)^2 > 4(1 - s^2)\left(\frac{1}{3} - s^2\right) \iff \frac{4}{3} s^2 > \frac{1}{3} \iff s > \frac{1}{2}. \]
当 \(s \in \left(\frac{1}{2}, \frac{1}{\sqrt{3}}\right)\) 时，\(m^2 - 4c^2 = (1 - s^2) - \left(\frac{4}{3} - 4s^2\right) = 3s^2 - \frac{1}{3} > \frac{5}{12} > 0\)，故 \(2c < m\) 自动成立，即 \(M(c,0)\) 与 \(K(0,0)\) 均严格在线段 \(BC\) 上；又 \(PK^2 = c^2 + s^2 = \frac{1}{3} = PA \cdot PB\) 给出 \(\triangle PKA \sim \triangle PBK\)，从而 \(\angle PKA = \angle PBK = \angle ABC = \angle PDA\)，即 \(P, A, K, D\) 四点共圆，且 \(KB \cdot KC = 1 - OK^2 = \frac{2}{3} = \frac{1}{2} OP^2\)。因此合法构型与 \(s \in \left(\frac{1}{2}, \frac{1}{\sqrt{3}}\right)\) 一一对应。
- **利用极点极线求 \(Q\) 的横坐标与点 \(T\) 的坐标。**
因为 \(ABCD\) 内接于圆且 \(\angle ABC < \angle BCD\)，所以 \(AD\) 与 \(BC\) 不平行，设 \(R = AD \cap BC\)。由完全四边形的调和性质（Brocard 定理）：
1. 直线 \(QR\) 与 \(PB, PC\) 的交点分别与 \(P\) 关于 \((A,B)\) 和 \((D,C)\) 调和共轭，因此直线 \(QR\) 是点 \(P(c, s)\) 关于圆 \(\omega: (x + c)^2 + (y + s)^2 = 1\) 的极线，方程为
   \[ 2c(x + c) + 2s(y + s) = 1. \]
2. 同理，直线 \(PR\) 是点 \(Q\) 关于圆 \(\omega\) 的极线，故 \(OQ \perp PR\)。

由于 \(R(x_R, 0)\) 在直线 \(QR\) 上，代入极线方程得
\[ 2c(x_R + c) + 2s^2 = 1 \implies 2c x_R = 1 - 2(c^2 + s^2) = 1 - \frac{2}{3} = \frac{1}{3}. \]
又设 \(Q(x_Q, y_Q)\)，则 \(Q\) 在 \(QR\) 上且 \(\overrightarrow{OQ} \cdot \overrightarrow{PR} = 0\)，即
\[ 2c(x_Q + c) + 2s(y_Q + s) = 1, \]
\[ (x_R - c)(x_Q + c) - s(y_Q + s) = 0. \]
将第二式乘以 \(2\) 与第一式相加消去 \(y_Q + s\)，得
\[ 2 x_R (x_Q + c) = 1. \]
由 \(2c x_R = \frac{1}{3}\)（注意 \(c > 0\)），代入得 \(\frac{1}{3c}(x_Q + c) = 1\)，解得 \(x_Q = 2c\)。
直线 \(OP\) 过 \(K(0, 0)\) 与 \(P(c, s)\)，方程为 \(y = \frac{s}{c} x\)。过 \(Q\) 作 \(BC\) 的垂线 \(x = x_Q = 2c\) 与直线 \(OP\) 交于点 \(T\)，故 \(T\) 的坐标为 \((2c, 2s)\)。
- **计算 \(TB + TC\) 并求其所有可能值。**
利用 \(c^2 + s^2 = \frac{1}{3}\) 与 \(m^2 = 1 - s^2\)，计算 \(TB^2\) 与 \(TC^2\)：
\[ TB^2 = (3c + m)^2 + 4s^2 = 9c^2 + 6cm + m^2 + 4s^2. \]
注意到
\[ 9c^2 + m^2 + 4s^2 = 9\left(\frac{1}{3} - s^2\right) + (1 - s^2) + 4s^2 = 4 - 6s^2 = 3(1 - s^2) + 3\left(\frac{1}{3} - s^2\right) = 3m^2 + 3c^2, \]
因此
\[ TB^2 = 3m^2 + 6cm + 3c^2 = 3(m + c)^2 \implies TB = \sqrt{3}(m + c). \]
同理，
\[ TC^2 = (3c - m)^2 + 4s^2 = 3m^2 - 6cm + 3c^2 = 3(m - c)^2. \]
因为 \(m > 2c > c > 0\)，所以 \(TC = \sqrt{3}(m - c)\)。两式相加得
\[ TB + TC = \sqrt{3}(m + c) + \sqrt{3}(m - c) = 2\sqrt{3}\, m = 2\sqrt{3(1 - s^2)}. \]
当 \(s\) 在开区间 \(\left(\frac{1}{2}, \frac{1}{\sqrt{3}}\right)\) 内连续变化时，\(2\sqrt{3(1 - s^2)}\) 严格单调递减，其值域为
\[ \left(2\sqrt{3\left(1 - \frac{1}{3}\right)},\; 2\sqrt{3\left(1 - \frac{1}{4}\right)}\right) = (2\sqrt{2}, 3). \]
综上，\(TB + TC\) 的所有可能值为开区间 \((2\sqrt{2}, 3)\) 内的任意实数。

**盲解结论**：(1) \(OP\) 的所有可能值为 \(\frac{2\sqrt{3}}{3}\)；(2) \(TB + TC\) 的所有可能值为开区间 \((2\sqrt{2}, 3)\) 内的任意实数。

### 2. 对照答案复盘

两问最终结论与参考答案完全一致：第（1）问 \(OP = \frac{2\sqrt{3}}{3}\)，第（2）问 \(TB + TC \in (2\sqrt{2}, 3)\)。方法上，第（1）问盲解与参考答案几乎一致，均先由共圆倒角得 \(\triangle PKA \sim \triangle PBK\) 推出 \(PK^2 = PA \cdot PB = OP^2 - 1\)，再结合点 \(K\) 对圆 \(O\) 的幂导出 \(K\) 为 \(OP\) 中点（参考答案用均值不等式取等，盲解用中线长公式）。第（2）问采用了与参考答案不同的有效方法：参考答案运用“同一法”，沿 \(OK\) 延长至 \(T'\) 使 \(OT' = \sqrt{3}\)，利用反演相似 \(\triangle OBT' \sim \triangle OKB\) 证得 \(\angle CAT' = 90^\circ\)，再由三圆根心定理证明 \(T' = T\)，最后以 \(v = TC\) 为参数求得值域；盲解则以 \(K\) 为原点建系，借助完全四边形极点极线（Brocard 定理）求出 \(x_Q = 2c\) 从而确定 \(T\) 的坐标，并通过解析恒等变形同样得到 \(TB = \sqrt{3}\,KB\)、\(TC = \sqrt{3}\,KC\) 及合法参数的充要区间 \(s \in (\frac{1}{2}, \frac{1}{\sqrt{3}})\)。参考答案的纯几何构造在结构洞察上更为精妙。

### 3. 困难点与破局关键

- **第（1）问的“不等式取等”锁点技巧**：从 \(OP^2 - 1 = PK^2\) 和 \(1 - OK^2 = \frac{1}{2}OP^2\) 相加得到 \(PK^2 + OK^2 = \frac{1}{2}OP^2\) 后，学生往往以为只是关于 \(PK, OK\) 的一个普通关系，难以立刻联想到结合三角不等式 \(PK + OK \ge OP\) 与基本不等式 \(PK^2 + OK^2 \ge \frac{1}{2}(PK + OK)^2\) 将不等式逼紧为等式，从而直接锁定 \(K\) 是 \(OP\) 的中点。
- **第（2）问“同一法”与反演点的构造**：第（2）问点 \(T\) 由 \(Q\) 过垂线与 \(OP\) 相交定义，直接追踪 \(Q\) 的平面几何位置非常困难。参考答案采用“同一法”，直接猜想并构造 \(OT' = \sqrt{3}\) 的点 \(T'\)，使其与 \(K\) 关于单位圆反演共轭（即 \(OK \cdot OT' = 1\)），利用反演相似和垂足圆把共点问题转化为三圆的根心定理，这一构造是本题最大的思维飞跃。
- **角度约束向参数区间的充分必要转化**：在得到 \(TB \cdot TC = 2\) 后，还必须精确利用 \(\angle ABC < \angle BCD < 90^\circ\) 确定 \(v = TC\) 的上下界，并反过来说明区间内每个 \(v\) 都能构造出合法凸四边形，不能漏掉退化边界。

### 4. 问题拆解（教学引导）

- **拆解第（1）问条件：双圆共点与双圆幂**：注意到 \(A,B,C,D\) 共圆且 \(P,A,K,D\) 共圆，且 \(P,A,B\) 共线、\(P,D,C\) 共线，这是一个典型的密克尔/反演结构。先利用 \(\angle ABC < \angle BCD < 90^\circ\) 确定 \(P\) 在圆外且 \(A \in PB, D \in PC\)，再对 \(P\) 和 \(K\) 分别使用圆幂定理，即可建立 \(OP, OK, PK\) 之间的联系。
- **捕捉代数线索：消去常数并触发放缩取等**：条件 \(KB \cdot KC = \frac{1}{2} OP^2\) 与 \(OP\) 的平方成正比，提示将 \(PA \cdot PB = OP^2 - 1\) 与 \(1 - OK^2 = KB \cdot KC\) 两式相加消去常数 \(1\)，从而观察 \(PK^2 + OK^2\) 与 \(OP^2\) 的大小关系。
- **拆解第（2）问：反演视角预测 \(T\) 的位置并用同一法验证**：求出 \(OK = \frac{\sqrt{3}}{3}\) 与 \(OP = \frac{2\sqrt{3}}{3}\) 后，若将 \(K\) 反演至单位圆外（使 \(OK \cdot OT' = 1\)），则 \(OT' = \sqrt{3}\)，恰好出现 \(\triangle OBT' \sim \triangle OKB\) 与直角 \(\angle CAT' = 90^\circ\)。据此可通过“同一法”先构造具有良好对称性的点 \(T'\)，再证明 \(T' = T\)。

### 5. 答案拆解（逻辑骨架）

- **第（1）问：相似转化圆幂，放缩锁定中点**（*动机*：第（1）问中，利用相似将 \(PK\) 联系到 \(P\) 的圆幂，再与 \(K\) 的圆幂相加消去 \(1\)，利用不等式取等锁定 \(K\) 为 \(OP\) 中点。）：由 \(P,A,K,D\) 共圆和 \(A,B,C,D\) 共圆，得 \(\angle PKA = \angle PDA = \angle CBA = \angle KBP\)，从而 \(\triangle PKA \sim \triangle PBK\)，给出 \(PK^2 = PA \cdot PB\)。分别写出 \(P\) 和 \(K\) 关于单位圆 \(O\) 的幂：\(OP^2 - 1 = PK^2\) 与 \(1 - OK^2 = \frac{1}{2}OP^2\)。两式相加并结合均值不等式与三角不等式：\(\frac{1}{2}OP^2 = PK^2 + OK^2 \ge \frac{1}{2}(PK + OK)^2 \ge \frac{1}{2}OP^2\)，迫使等号全成立，故 \(K\) 为 \(OP\) 中点，代回解得 \(OP = \frac{2\sqrt{3}}{3}\)。
- **第（2）问构造与倒角：引入反演对应点 \(T'\) 证得 \(\angle CAT' = 90^\circ\)**（*动机*：既然目标求 \(TB + TC\)，将线段比 \(\frac{OB}{OK} = \sqrt{3}\) 延拓为以 \(O\) 为中心的反演相似点 \(T'\)，可把 \(T'B, T'C\) 直接与 \(KB, KC\) 挂钩，同时诱导出垂直关系 \(\angle CAT' = 90^\circ\)。）：延长 \(OK\) 至 \(T'\) 使 \(OT' = \sqrt{3}\)，则 \(OK = KP = PT' = \frac{\sqrt{3}}{3}\)。因 \(\frac{OT'}{OB} = \sqrt{3} = \frac{OB}{OK}\)，有 \(\triangle OBT' \sim \triangle OKB\)。再结合 \(PA \cdot PB = PK^2 = PT'^2\) 得 \(\triangle PAT' \sim \triangle PT'B\)，倒角得 \(\angle PAT' = \angle BT'O = \angle OBK = 90^\circ - \frac{1}{2}\angle BOC = 90^\circ - \angle CAP\)，从而 \(\angle CAT' = 90^\circ\)。
- **第（2）问同一法合流：三圆根心定理证明 \(T' = T\)**（*动机*：要证明构造出的 \(T'\) 就是题目中的 \(T\)，只需证明 \(T'\) 在 \(BC\) 上的射影与 \(Q\) 连线垂直于 \(BC\)；利用两个直径圆与原外接圆的根轴交于 \(Q\)，即可一步完成“同一法”合流。）：作 \(T'\) 在 \(BC\) 上的射影 \(H\)，由 \(\angle CAT' = \angle CHT' = 90^\circ\) 知 \(T', A, H, C\) 共圆（记为 \(\omega_1\)）；同理 \(T', B, H, D\) 共圆（记为 \(\omega_2\)）。对三圆 \(O, \omega_1, \omega_2\) 应用根心定理，三条根轴 \(AC, BD, T'H\) 共点，故 \(T'H\) 必过 \(AC \cap BD = Q\)，因此 \(T'\) 即为过 \(Q\) 作 \(BC\) 垂线与 \(OP\) 的交点 \(T\)。
- **第（2）问双变量代换与充要边界分析**（*动机*：利用相似比将 \(TB + TC\) 转化为单变量函数 \(v + \frac{2}{v}\)，再通过锐角约束与充分性反推精确界定参数 \(v\) 的开区间。）：由相似比 \(\sqrt{3}\) 设 \(TB = u, TC = v\)，则 \(KB = \frac{\sqrt{3}}{3}u, KC = \frac{\sqrt{3}}{3}v\)，由 \(KB \cdot KC = \frac{2}{3}\) 得 \(uv = 2\)。由 \(\angle ABC < \angle BCD < 90^\circ\) 得 \(PB > PC \implies TB > TC \implies u > \sqrt{2} > v\)；由 \(QH \perp BC\) 且 \(H\) 在线段 \(BC\) 上（及 \(T\) 与 \(P\) 同侧）得 \(\angle TCK < 90^\circ\)，故 \(\frac{4}{3} = TK^2 < TC^2 + CK^2 = \frac{4}{3}v^2 \implies v > 1\)。反过来验证对任意 \(v \in (1, \sqrt{2})\)，中线 \(CP\) 满足 \(PC > PK = \sqrt{PA \cdot PB} = \sqrt{PC \cdot PD}\)，确证构型合法。最终 \(TB + TC = v + \frac{2}{v}\) 在 \((1, \sqrt{2})\) 上严格递减，值域为 \((2\sqrt{2}, 3)\)。

### 6. 易错点分析

- **边界与退化情形未排除，误写为闭区间**：常见错法——将第（2）问 \(TB + TC\) 的取值范围误写成闭区间 \([2\sqrt{2}, 3]\) 或半开半闭区间。；错因——\(v = \sqrt{2}\) 破坏了 \(\angle ABC < \angle BCD\)，而 \(v = 1\) 破坏了 \(\angle BCD < 90^\circ\) 及四边形的凸性（评分标准明确指出开区间误写为闭区间扣 \(3\) 分）。；避坑策略——严格检查题目中的严格不等号（\(\angle ABC < \angle BCD < 90^\circ\)）与“凸四边形”条件：当 \(v = 1\) 时，\(\angle TCK = 90^\circ\)，对应 \(D\) 与 \(C\) 重合（四边形退化为三角形）；当 \(v = \sqrt{2}\) 时，\(u = v\)，对应 \(\angle ABC = \angle BCD\)。两端点均不满足题设严格条件，故必须取开区间。
- **忽略充分性（存在性）验证**：常见错法——仅由必要条件推出 \(v \in (1, \sqrt{2})\) 后便直接断言值域为 \((2\sqrt{2}, 3)\)，未验证区间内每个值都能对应合法四边形。；错因——“求所有可能值”要求充要刻画，仅证必要性无法排除参数区间内隐含其他几何约束导致部分值不可达的可能。；避坑策略——在导出 \(v \in (1, \sqrt{2})\) 后，应按标答做法补全充分性验证：利用中线 \(CP\) 验证 \(PC > PK > \sqrt{PA \cdot PB} = \sqrt{PC \cdot PD}\)，从而确证 \(PB > PC > PD > PA\)，即 \(A, D\) 确实严格位于线段 \(PB, PC\) 上且所有题设条件都能取到。
- **构型位置关系的隐含假设未加说明**：常见错法——未说明 \(A, D\) 分别位于线段 \(PB, PC\) 上以及 \(K\) 在 \(\angle BPC\) 内部，就直接写 \(\angle PKA = \angle PDA = \angle CBA\) 或 \(OP^2 - 1 = PA \cdot PB\)。；错因——若 \(P\) 在圆内或 \(A\) 在线段 \(PB\) 延长线上，圆幂公式符号及倒角关系（同旁内角与对角互补）都会发生变化，推理不严谨易被扣分。；避坑策略——第（1）问中，应先由 \(\angle ABC + \angle BCD < 180^\circ\) 与四边形凸性说明 \(P\) 落在射线 \(BA, CD\) 延长线上（在圆外），进而由 \(KB \cdot KC > 0\) 确定 \(K\) 在 \(\angle BPC\) 内，从而严格得到 \(\angle PKA = \angle PDA = \angle ABC\) 与 \(\triangle PKA \sim \triangle PBK\)。

**教学小结**：在圆几何中，遇到两点对同一圆的幂满足特殊线性关系时，尝试联立圆幂式往往能诱导出隐藏的不等式取等条件；而当所求点由垂线与中线（或连心线）交点定义时，从反演共轭位置预设目标点并结合“同一法”与根心定理，是打通纯几何证明的高效路径。

---

## 2025 CMO 试题解答与评分标准 · 3（`cmo-2025-images-ba37a1fa50-combined-q3`）

- **学段**：高中 · **盲解结果**：盲解正确（不同有效解法）
- **教学标签**：训练:压轴攻坚 / 归纳与递推 / 放缩与估值 / 构造与反例 / 易错:计算精度与等价替换 / 易错:隐含假设与越界推广 / 易错:边界与退化情形
- **知识专题**：组合最值 / 递推与二项式系数 / 不等式放缩

### 原题整理

设 \(n\) 是正整数。有 \(n\) 张红色卡片与 \(n\) 张蓝色卡片，最初每张红色卡片上都写有一个实数 \(0\)，每张蓝色卡片上都写有一个实数 \(1\)。一次操作是指：选择一张红色卡片与一张蓝色卡片，满足红色卡片上的实数 \(x\) 小于蓝色卡片上的实数 \(y\)，将这两个实数擦去，并在这两张卡片上都写下实数 \(\frac{x+y}{2}\)。求最小的正整数 \(n\)，使得可以适当地进行有限次操作，让所有 \(n\) 张红色卡片上的实数之和大于 \(100\)。

### 1. 只看原题盲解尝试

**切入思路**：首先通过构造“网格顺序”操作策略（依次让第 \(i\) 张红色卡片与第 \(1, 2, \dots, n\) 张蓝色卡片操作）证明可以达到红色卡片之和 \(S_n = n - n \frac{\binom{2n}{n}}{4^n}\)；接着利用“分解为两个极端初始世界求平均”的线性性质，对操作次数作数学归纳法，证明对任意合法操作序列（甚至不限制 \(x < y\) 且允许重复配对），所有红色卡片之和都不超过 \(S_n\)；最后通过放缩估算出满足 \(S_n > 100\) 的最小正整数为 \(n = 106\)。

**推演步骤**：
- **第一步：构造性下界（网格策略）**
将 \(n\) 张红色卡片记为 \(R_1, R_2, \dots, R_n\)，\(n\) 张蓝色卡片记为 \(B_1, B_2, \dots, B_n\)。按字典序依次对 \((R_i, B_j)\)（\(i = 1, \dots, n\)；\(j = 1, \dots, n\)）进行操作，即先让 \(R_1\) 依次与 \(B_1, \dots, B_n\) 操作，再让 \(R_2\) 依次与 \(B_1, \dots, B_n\) 操作，以此类推。
定义数列 \(f(i, j)\)（\(i, j \ge 0\) 且 \(i+j \ge 1\)）：
\[f(i, 0) = 0 \ (i \ge 1), \quad f(0, j) = 1 \ (j \ge 1), \quad f(i, j) = \frac{f(i-1, j) + f(i, j-1)}{2} \ (i, j \ge 1).\]
由概率意义可知，\(f(i, j)\) 等于在连续 \(i+j-1\) 次独立抛硬币（正反面概率均为 \(\frac{1}{2}\)）中至少出现 \(i\) 次正面的概率：
\[f(i, j) = \mathbb{P}\!\left(\operatorname{Bin}(i+j-1, \tfrac{1}{2}) \ge i\right).\]
显然当 \(i, j \ge 1\) 时，\(f(i, j)\) 关于 \(i\) 严格递减、关于 \(j\) 严格递增，故 \(f(i, j-1) < f(i, j) < f(i-1, j)\)。因此每次操作 \((R_i, B_j)\) 前，均有 \(R_i\) 上的数 \(f(i, j-1)\) 严格小于 \(B_j\) 上的数 \(f(i-1, j)\)，所有 \(n^2\) 次操作均合法。操作结束后，红色卡片上的数依次为 \(f(1, n), f(2, n), \dots, f(n, n)\)，其和为 \(S(n, n) = \sum_{i=1}^n f(i, n)\)。
- **第二步：计算 \(S(m, k) = \sum_{i=1}^m f(i, k)\) 的递推关系与封闭形式**
对任意正整数 \(m, k\)，由定义易知 \(f(i, j) + f(j, i) = 1\)。在 \(m\) 张红卡与 \(k\) 张蓝卡上执行上述网格操作，所有卡片总和恒为 \(k\)，故
\[S(m, k) + \sum_{j=1}^k f(m, j) = k \implies S(m, k) + k - \sum_{j=1}^k f(j, m) = k \implies S(m, k) = S(k, m).\]
约定 \(S(0, k) = S(m, 0) = 0\)。对 \(m, k \ge 1\)，有
\[S(m, k) - S(m-1, k) = f(m, k), \quad S(m, k) - S(m, k-1) = S(k, m) - S(k-1, m) = f(k, m) = 1 - f(m, k),\]
两式相加得核心递推式：
\[S(m, k) = \frac{S(m-1, k) + S(m, k-1) + 1}{2} \quad (m, k \ge 1).\]
此外，对于 \(n \ge 1\)，利用对称性可得
\[f(n-1, n) = \mathbb{P}\!\left(\operatorname{Bin}(2n-2, \tfrac{1}{2}) \ge n-1\right) = \frac{1}{2} + \frac{\binom{2n-2}{n-1}}{2 \cdot 4^{n-1}}, \quad f(n, n-1) = 1 - f(n-1, n) = \frac{1}{2} - \frac{\binom{2n-2}{n-1}}{2 \cdot 4^{n-1}}.\]
由 \(S(n, n) = \frac{S(n-1, n) + S(n, n-1) + 1}{2} = S(n, n-1) + \frac{1}{2}\)，得
\[S(n, n) - S(n-1, n-1) = f(n, n-1) + \frac{1}{2} = 1 - \frac{\binom{2n-2}{n-1}}{2 \cdot 4^{n-1}}.\]
结合恒等式 \(n \frac{\binom{2n}{n}}{4^n} - (n-1) \frac{\binom{2n-2}{n-1}}{4^{n-1}} = \frac{\binom{2n-2}{n-1}}{2 \cdot 4^{n-1}}\)，归纳（或累加）即得
\[S_n := S(n, n) = n - n \frac{\binom{2n}{n}}{4^n}.\]
- **第三步：证明任意操作序列下的上界**
考虑更一般的初始状态：设红色卡片中有 \(m\) 张写有 \(0\)、\(d_R\) 张写有 \(1\)；蓝色卡片中有 \(k\) 张写有 \(1\)、\(d_B\) 张写有 \(0\)（\(m, d_R, k, d_B \ge 0\)）。我们证明：对此初始状态执行任意 \(L\) 次配对平均操作 \((R_i, B_j) \mapsto \left(\frac{R_i+B_j}{2}, \frac{R_i+B_j}{2}\right)\)（甚至不要求操作前 \(R_i < B_j\)），最终所有红色卡片之和不超过 \(d_R + S(m, k)\)。
对操作次数 \(L\) 作数学归纳：
- 当 \(L = 0\) 时，红色卡片之和为 \(d_R \le d_R + S(m, k)\)，成立。
- 设对 \(L-1\) 成立，考虑第 \(1\) 次操作 \((R_i, B_j)\)：
  1. 若初始 \((R_i, B_j) = (0, 0)\) 或 \((1, 1)\)，该操作不改变任何数值，由归纳假设结论成立。
  2. 若初始 \((R_i, B_j) = (0, 1)\)，操作后 \((R_i, B_j) = (\frac{1}{2}, \frac{1}{2})\)，这恰好是“世界 A（将 \((R_i, B_j)\) 改为 \((0, 0)\)）”与“世界 B（将 \((R_i, B_j)\) 改为 \((1, 1)\)）”初始状态的平均值。由于后续 \(L-1\) 次平均操作均为线性变换，最终红色卡片之和等于两世界结果的平均值。世界 A 的参数为 \((m, d_R; k-1, d_B+1)\)，世界 B 的参数为 \((m-1, d_R+1; k, d_B)\)，由归纳假设，总和不超过
     \[\frac{\big(d_R + S(m, k-1)\big) + \big(d_R + 1 + S(m-1, k)\big)}{2} = d_R + \frac{S(m, k-1) + S(m-1, k) + 1}{2} = d_R + S(m, k).\]
  3. 若初始 \((R_i, B_j) = (1, 0)\)，同理分解为世界 A（参数 \((m+1, d_R-1; k, d_B)\)）与世界 B（参数 \((m, d_R; k+1, d_B-1)\)），由归纳假设，总和不超过
     \[d_R + \frac{S(m+1, k) + S(m, k+1) - 1}{2}.\]
     当 \(m = 0\) 或 \(k = 0\) 时，直接验证可得上式不超过 \(d_R + S(m, k)\)；当 \(m, k \ge 1\) 时，
     \[\frac{S(m+1, k) + S(m, k+1) - 1}{2} - S(m, k) = \frac{f(m+1, k) + (1 - f(m, k+1)) - 1}{2} = \frac{f(m+1, k) - f(m, k+1)}{2} < 0.\]
     故归纳成立。
取 \(m = k = n, d_R = d_B = 0\)，即证得对任意有限次合法操作，所有红色卡片之和不超过 \(S_n\)。
- **第四步：确定满足 \(S_n > 100\) 的最小正整数 \(n\)**
记 \(W_n = \frac{\binom{2n}{n}}{4^n} = \prod_{j=1}^n \frac{2j-1}{2j}\)，则 \(S_n = n(1 - W_n)\)，且 \(S_n - S_{n-1} = 1 - \frac{1}{2} W_{n-1} > 0\)，即 \(S_n\) 关于 \(n\) 严格递增。
1. 当 \(n = 105\) 时，利用 \((2j-1)^2 > (2j-2)(2j)\)（\(j \ge 2\)），有
   \[W_n^2 = \frac{1}{4} \prod_{j=2}^n \frac{(2j-1)^2}{(2j)^2} > \frac{1}{4} \prod_{j=2}^n \frac{j-1}{j} = \frac{1}{4n}.\]
   故 \(W_{105}^2 > \frac{1}{420} > \frac{1}{441} = \left(\frac{1}{21}\right)^2\)，从而 \(W_{105} > \frac{1}{21}\)，因此
   \[S_{105} = 105(1 - W_{105}) < 105\left(1 - \frac{1}{21}\right) = 100.\]
   由单调性可知，对所有 \(n \le 105\)，均有 \(S_n \le S_{105} < 100\)。
2. 当 \(n = 106\) 时，利用 \(\left(\frac{2j-1}{2j}\right)^2 < \frac{2j-1}{2j+1}\)（\(j \ge 1\)），结合 \(W_4 = \frac{1 \cdot 3 \cdot 5 \cdot 7}{2 \cdot 4 \cdot 6 \cdot 8} = \frac{35}{128}\)，有
   \[W_{106}^2 = W_4^2 \prod_{j=5}^{106} \left(\frac{2j-1}{2j}\right)^2 < \left(\frac{35}{128}\right)^2 \prod_{j=5}^{106} \frac{2j-1}{2j+1} = \left(\frac{35}{128}\right)^2 \cdot \frac{9}{213} = \frac{3675}{1163264}.\]
   比较 \(\frac{3675}{1163264}\) 与 \(\left(\frac{3}{53}\right)^2 = \frac{9}{2809}\)：约去公因子 \(3\) 后，\(1225 \times 2809 = 3441025 < 3489792 = 3 \times 1163264\)，故 \(W_{106} < \frac{3}{53}\)，从而
   \[S_{106} = 106(1 - W_{106}) > 106\left(1 - \frac{3}{53}\right) = 100.\]

综上，最小的正整数 \(n\) 为 \(106\)。

**盲解结论**：最小的正整数 \(n\) 为 \(106\)。

### 2. 对照答案复盘

Turn 1 盲解完全独立地得到了正确答案 \(n = 106\)、精确最大值表达式 \(S_n = n - n\frac{\binom{2n}{n}}{4^n}\)、相同的网格构造方案以及完全一致的沃利斯型手工放缩（包括在 \(W_4 = \frac{35}{128}\) 处截断放缩）。在核心难点“最优性（上界）证明”上，盲解采用了与官方参考解答不同的有效方法：参考解答先将操作放宽为转移量 \(r \in [0, \frac{y-x}{2}]\)，利用紧致性说明最大值可达，再通过“分散化（majorization）引理”证明相邻区间内不含其它数时可按 \(j-i\) 顺序重排；而盲解则利用操作本身的线性性，将首次 \((0,1) \to (\frac{1}{2}, \frac{1}{2})\) 拆分为 \((0,0)\) 与 \((1,1)\) 两个极端初始状态的平均，直接对操作次数作数学归纳，避免了紧致性与连续性讨论，证明同样严格且更为简短。

### 3. 困难点与破局关键

- **二维网格和式的封闭化简**：将 \(T(n, n) = \sum_{i=1}^n h(i, n)\) 化简为封闭形式 \(n - n\frac{\binom{2n}{n}}{4^n}\) 是第一个技术难点。参考解答通过差分 \(h(n, k) - h(n, k+1)\) 将双重和化为关于 \(\binom{n+k-1}{n} 2^{n-1-k}\) 的单重和，再用组合意义求和；盲解则利用 \(T(n, n) - T(n-1, n-1)\) 的递推关系配合对称概率直接得出。
- **任意操作序列与网格策略之间的最优性证明**：任意合法操作序列可能交错进行，无法直接与网格顺序一一对应。参考解答通过放宽操作为 \(r \in [0, \frac{y-x}{2}]\)、证明最大值可达，并建立“分散化不减最大值”的调整引理，逐步把任意操作序列规范化为网格顺序；盲解则通过“线性拆分首次操作为两个 \(0/1\) 极端世界”对操作步数作归纳。
- **\(n = 105\) 与 \(n = 106\) 临界处的高精度手工放缩**：\(S_{105} \approx 99.23\) 而 \(S_{106} \approx 100.20\)，\(S_{106}\) 超出 \(100\) 仅约 \(0.2\%\)，常规的 \(\frac{1}{\sqrt{2n+1}}\) 放缩失效，必须保留前几项精确值（如算到 \(W_4 = \frac{35}{128}\)）再对剩余项做沃利斯型平方放缩。

### 4. 问题拆解（教学引导）

- **识别单调性与操作次数的有限性**：操作中红卡数值只增不减、蓝卡数值只减不增，且所有数值始终保持在 \([0, 1]\) 内，全体 \(2n\) 张卡片总和恒为 \(n\)。一旦某对 \((R_i, B_j)\) 操作一次变成相等，之后必恒有 \(R_i \ge B_j\)，故每对 \((R_i, B_j)\) 至多操作一次。
- **小规模枚举猜想最优策略与结构**：从 \(n=1, 2, 3\) 入手试验发现：按“让最强的红卡依次与所有蓝卡操作，再让次强的红卡依次与所有蓝卡操作”的网格顺序，红卡之和依次为 \(\frac{1}{2}, \frac{5}{4}, \frac{33}{16}\)，恰好与穷举最大值完全一致。
- **将对称问题推广为双参数问题以利于递推与归纳**：若要把最优性（上界）和表达式一起拿下，往往需要把 \(n\) 张红卡、\(n\) 张蓝卡推广为一般情形（如参考解答中的 \(n\) 张红卡、\(m\) 张蓝卡 \(T(m, n)\)，或盲解中的含 \(0/1\) 哑元卡的一般初始态），以便建立递推与归纳框架。

### 5. 答案拆解（逻辑骨架）

- **构造网格操作方案并建立递推 \(h(i, j)\)**（*动机*：先给出能取到的具体方案并算出其结果，作为后续证明的目标上界。）：将网格操作推广到 \(n\) 张红卡与 \(m\) 张蓝卡，设第 \(i\) 张蓝卡与第 \(j\) 张红卡操作后的共同数值为 \(h(i, j)\)，由递推 \(h(i, j) = \frac{h(i, j-1) + h(i-1, j)}{2}\)（边界 \(h(0, j)=0, h(i, 0)=1\)）得到组合表达式 \(h(i, j) = \frac{1}{2^{i+j-1}}\sum_{t=0}^{i-1}\binom{i+j-1}{t}\)，并验证其关于 \(i\) 递增、关于 \(j\) 递减，保证每次操作均满足“红小于蓝”。
- **化简 \(T(n, n)\) 为封闭表达式**（*动机*：只有将双重组合和式化为单一中心二项式系数的形式，才能准确估算 \(n\) 的临界值。）：利用 \(h(n, n) = \frac{1}{2}\) 与差分 \(h(n, k) - h(n, k+1) = \frac{\binom{n+k-1}{n-1}}{2^{n+k}}\)，通过阿贝尔变换（或分部求和）将 \(T(n, n) - \frac{n}{2}\) 化为 \(\sum_{k=1}^{n-1}\frac{n\binom{n+k-1}{n}}{2^{n+k}}\)，再借助组合计数恒等式 \(\sum_{k=1}^{n-1}\binom{n+k-1}{n}2^{n-1-k} = 2^{2n-2} - \binom{2n-1}{n}\) 得到 \(T(n, n) = n - n\frac{\binom{2n}{n}}{4^n}\)。
- **沃利斯型放缩严格判定 \(n=105\) 与 \(n=106\)**（*动机*：在 \(n=105\) 和 \(n=106\) 之间差值极小，需要足够精细的初等不等式严格界定临界点。）：用 \(f(n) \approx n - \sqrt{n/\pi}\) 锁定临界在 \(n=106\) 附近。对 \(n=105\)，利用 \(\frac{(2k-1)^2}{(2k)^2} > \frac{2k-2}{2k}\) 平方裂项证得 \(W_{105} > \frac{1}{\sqrt{420}} > \frac{1}{21}\)，故 \(f(105) < 100\)；对 \(n=106\)，保留前 \(4\) 项精确值 \(\frac{35}{128}\)，对第 \(5\) 项至第 \(106\) 项利用 \(\frac{(2k-1)^2}{(2k)^2} < \frac{2k-1}{2k+1}\) 放缩，证得 \(W_{106} < \frac{35}{128}\sqrt{\frac{9}{213}} < \frac{3}{53}\)，故 \(f(106) > 100\)。
- **放宽操作、分散化引理与操作序规范化（证明最优性）**（*动机*：排除其它交错操作顺序得到更大红卡和的可能性，完成“最小 \(n\)”的必要性证明。）：参考解答先放宽操作为将一对 \((x, y)\)（\(x \le y\)）改为 \((x+r, y-r)\)（\(r \in [0, \frac{y-x}{2}]\)），说明可合并重复对使操作次数 \(\le n^2\)，并用紧致性说明最大得分 \(h(x_1, \dots, x_n, y_1, \dots, y_n)\) 可达。再证核心引理：将两张红卡（或蓝卡）数值向外“分散”且保持和不变，最大得分不减。由此可将任意跨越中间值的操作拆分为相邻两步，使得每次操作的两张卡之间没有其它卡，从而迫使整个过程只能按 \(j-i\) 从小到大的网格序进行，且每步均取 \(r = \frac{y-x}{2}\)。

### 6. 易错点分析

- **默认“最自然/最贪心”的构造就是全局最优**：常见错法——仅给出“网格顺序”构造并算出 \(T(n,n) = n - n\frac{\binom{2n}{n}}{4^n}\)，就默认这就是最大值而跳过最优性证明。；错因——评分标准中，构造与表达式仅占前两部分分数（3 分 + 6 分），而“证明该操作方式是最大的”单独占 12 分。若无严格上界证明，无法排除存在某种交错操作顺序能使红卡之和更大。；避坑策略——用归纳法或调整法严格证明任意合法操作序列都不超过 \(T(n,n)\)，或如盲解中将第一次操作线性拆分为 \((0,0)\) 与 \((1,1)\) 两个极端世界并对操作次数作归纳，才能彻底拿下“最值证明”的 12 分。
- **数值估计精度不够或以渐近代替严格证明**：常见错法——仅用渐近公式 \(n - \frac{n}{\sqrt{\pi n}} \approx n - \sqrt{n/\pi}\) 估算 \(n=106\)，或直接用粗糙的 \(W_n < \frac{1}{\sqrt{2n+1}}\) 来证明 \(n=106\) 可行。；错因——渐近估计只能猜出临界值，不能替代严格不等式；而粗糙放缩 \(W_{106} < \frac{1}{\sqrt{213}}\) 只能推出 \(106 - \frac{106}{\sqrt{213}} \approx 98.7 < 100\)，无法证明 \(S_{106} > 100\)。；避坑策略——在初步用 \(n - \sqrt{n/\pi} > 100\) 锁定临界值 \(n=106\) 后，必须用手工可算的沃利斯型放缩分别证明 \(S_{105} < 100\) 与 \(S_{106} > 100\)。对于上界，需从前几项精确算出 \(W_4 = \frac{35}{128}\) 再对后续项裂项放缩，才能把误差控制在 \(\sqrt{2/\pi}\) 与 \(\sqrt{\pi}\) 之间的足够窄范围内。
- **忽略操作次数有限性与合法性约束**：常见错法——不加证明地假设任意一对 \((R_i, B_j)\) 最多操作一次，或在调整操作顺序时忽略 \(x < y\) 的合法性约束。；错因——若不利用单调性说明每对 \((R_i, B_j)\) 至多操作一次，就无法将操作总次数限制在 \(n^2\) 以内，也会在交换相邻操作时破坏 \(x < y\) 的前提。；避坑策略——明确写清：红卡单调不减、蓝卡单调不增，一旦 \((R_i, B_j)\) 操作后二者相等，此后必恒有 \(R_i \ge B_j\)，故每对卡至多操作一次；若在证明中放宽条件（如允许 \(r \in [0, \frac{y-x}{2}]\)），需单独说明多次操作同一对卡可合并。

**教学小结**：面对“带条件限制的交互平均/配对最值”问题，构造端往往可以通过小规模枚举发现“按序扫描”的网格结构并借助概率/组合和式精确求解，而严格的上界证明既可以通过“放宽约束 + 分散化调整引理”将任意操作规范化，也可以利用操作本身的线性性将局部操作拆分为极端 \(0/1\) 状态的平均后直接归纳。

---

## 2025 CMO 试题解答与评分标准 · 4（`cmo-2025-images-ba37a1fa50-combined-q4`）

- **学段**：高中 · **盲解结果**：盲解正确（不同有效解法）
- **教学标签**：训练:压轴攻坚 / 不变量与单调量 / 放缩与估值 / 构造与反例 / 易错:边界与退化情形 / 易错:隐含假设与越界推广
- **知识专题**：组合最值 / 操作与不变量 / 纸牌问题

### 原题整理

有 \(30\) 种颜色的纸牌，每种颜色的纸牌均有 \(70\) 张。初始时从这些纸牌中任意选取 \(70\) 张，并从上至下摆成一叠。接着进行如下操作：从最下方 \(20\) 张纸牌中选一张纸牌 \(X\)，满足其颜色在最上方 \(50\) 张纸牌中未出现；再从最上方 \(50\) 张纸牌中选一张纸牌 \(Y\)，满足其颜色在最上方 \(50\) 张纸牌中至少出现两次；从这叠纸牌中取出 \(X\) 并将其紧贴着 \(Y\) 的上方放回这叠纸牌中。称上述过程为一次操作。重复上述操作直至无法选取这样的纸牌 \(X\) 时，整个操作过程结束。\n(1) 证明：对所有可能的初始情况及操作方式，整个操作过程都会在有限次操作后结束；\n(2) 在所有可能的初始情况及操作方式中，求操作次数的最大可能值。

### 1. 只看原题盲解尝试

**切入思路**：首先在第一问中利用最上方 \(50\) 张牌中互异颜色数 \(|S|\) 与重复颜色牌的最大位置 \(M\) 构造单调递减的非负整数势函数 \(\Psi\)，证明每次操作势函数至少严格减少 \(1\)，从而过程必在有限步内结束。在第二问中，通过分析整副 \(70\) 张牌至多包含 \(K \le \min(30, |S_0|+20)\) 种颜色，进一步精细化势函数 \(\Psi = (50 - M) + \sum_{j=|S|+1}^{K-1} j\)，结合初始状态单色牌数量 \(s_1(0) \le |S_0|-1\) 的估计，分 \(|S_0| \ge 10\) 与 \(|S_0| \le 9\) 两种情况证明操作次数上界为 \(390\)；最后给出恰好达到 \(390\) 次操作的初始排布与逐轮“冒泡”操作构造。

**推演步骤**：
- **记号与基本观察**：将这叠 \(70\) 张纸牌从上至下依次记为位置 \(1, 2, \dots, 70\)，其中位置 \(1 \sim 50\) 为“上方 \(50\) 张”，位置 \(51 \sim 70\) 为“下方 \(20\) 张”。设整副 \(70\) 张牌中共包含 \(K\) 种不同颜色（\(K\) 为不变量）。在任意时刻，设上方 \(50\) 张牌中出现过的颜色集合为 \(S\)。若某时刻 \(|S| = K\)，则所有 \(K\) 种颜色均已出现在上方 \(50\) 张中，下方 \(20\) 张里不可能选出 \(X\)，操作已经结束。因此，在每次操作前必有 \(|S| \le K - 1 \le 29\)；由抽屉原理，上方 \(50\) 张中至多有 \(29\) 种颜色，故必至少有一种颜色出现至少两次，即只要能选出 \(X\) 就一定能选出 \(Y\)。
- **构造势函数**：在每次操作前（此时 \(|S| \le K - 1\)），设 \(D\) 为上方 \(50\) 张牌中“其颜色在上方 \(50\) 张中至少出现两次”的牌的集合（显然 \(D \neq \emptyset\)），并记 \(M = \max\{\text{pos}(c) : c \in D\}\) 为 \(D\) 中最靠下那张牌的位置（\(2 \le M \le 50\)）。定义函数 \(F(m) = \sum_{j=m}^{K-1} j = \frac{(K-1+m)(K-m)}{2}\)（\(1 \le m \le K\)，约定 \(F(K) = 0\)），并定义非负整数势函数：\[\Psi = (50 - M) + F(|S| + 1) \ge 0\]。
- **证明 (1) —— 势函数严格单调递减**：考虑一次操作，将下方牌 \(X\) 插入上方位置 \(q \in \{1, \dots, 50\}\)（紧贴 \(Y\) 上方），原位置 \(50\) 的牌记为 \(Z\)（移至位置 \(51\)）。只要操作后仍有 \(|S_{\text{new}}| \le K - 1\)（至多最后一次操作会使 \(|S_{\text{new}}| = K\)），分两种情况讨论：\n- **情况 A**：\(Z\) 的颜色在操作前上方 \(50\) 张中仅出现 \(1\) 次。此时 \(Z \neq Y\)，故 \(q \le 49\) 且 \(Z \notin D_{\text{old}}\)，从而 \(M_{\text{old}} \le 49\)。操作中 \(Z\) 离开，\(X\) 以新颜色进入并仅出现 \(1\) 次，于是 \(|S_{\text{new}}| = |S_{\text{old}}|\) 且 \(D_{\text{new}} = D_{\text{old}}\)。因 \(Y \in D_{\text{old}}\) 且 \(q \le M_{\text{old}}\)，原位置 \(M_{\text{old}}\) 处的牌下移一位至 \(M_{\text{old}} + 1 \le 50\)，其余 \(D_{\text{old}}\) 中牌的位置均不上升，故 \(M_{\text{new}} = M_{\text{old}} + 1\)，从而 \(\Psi_{\text{new}} = \Psi_{\text{old}} - 1\)。\n- **情况 B**：\(Z\) 的颜色在操作前上方 \(50\) 张中至少出现 \(2\) 次。此时 \(Z \in D_{\text{old}}\)，故 \(M_{\text{old}} = 50\)。操作后 \(Z\) 离开而 \(X\) 带来新颜色，故 \(|S_{\text{new}}| = |S_{\text{old}}| + 1\)。记 \(m = |S_{\text{new}}| \le K - 1\)，设新上方 \(50\) 张中仅出现 \(1\) 次的颜色有 \(s_1\) 种。因 \(m < 50\)，必有至少一种颜色出现至少 \(2\) 次，故 \(s_1 \le m - 1\)。于是 \(|D_{\text{new}}| = 50 - s_1\)，从而 \(M_{\text{new}} \ge |D_{\text{new}}| = 50 - s_1\)，即 \(50 - M_{\text{new}} \le s_1 \le m - 1\)。又 \(F(m+1) - F(m) = -m\)，因此 \[\Psi_{\text{new}} - \Psi_{\text{old}} = (50 - M_{\text{new}}) - m \le (m - 1) - m = -1\]。\n综上，只要未终止，每一步 \(\Psi\) 至少减少 \(1\)。设总操作次数为 \(T\)，则前 \(T-1\) 步之后仍满足 \(|S| \le K-1\)，故 \(T - 1 \le \Psi_0 - \Psi_{T-1} \le \Psi_0\)，过程必在有限步内结束，(1) 得证。
- **证明 (2) 的上界 \(T \le 390\)**：设初始状态上方 \(50\) 张有 \(|S_0|\) 种颜色。若 \(T = 0\) 显然 \(T \le 390\)；若 \(T \ge 1\)，则 \(|S_0| \le K - 1\)。与情况 B 同理，初始时上方 \(50\) 张中仅出现 \(1\) 次的颜色数 \(s_1(0) \le |S_0| - 1\)，故 \(50 - M_0 \le s_1(0) \le |S_0| - 1\)。代入 \(T \le \Psi_0 + 1\) 得：\[T \le (|S_0| - 1) + F(|S_0| + 1) + 1 = |S_0| + F(|S_0| + 1) = F(|S_0|) = \sum_{j=|S_0|}^{K-1} j\]。另一方面，初始时上方 \(50\) 张有 \(|S_0|\) 种颜色，下方 \(20\) 张至多有 \(20\) 种颜色，故整副牌的总颜色数满足 \(K \le \min(30, |S_0| + 20)\)。\n- 若 \(|S_0| \ge 10\)，则 \(K \le 30\)，故 \(T \le \sum_{j=10}^{29} j = \frac{(10 + 29) \times 20}{2} = 390\)。\n- 若 \(|S_0| \le 9\)，则 \(K \le |S_0| + 20\)，故 \(T \le \sum_{j=|S_0|}^{|S_0|+19} j = 20|S_0| + 190 \le 20 \times 9 + 190 = 370 < 390\)。\n因此，任意初始情况与操作方式下均有 \(T \le 390\)。
- **构造达到 \(390\) 次操作的例子**：初始时从上至下依次摆放：\n- 位置 \(1 \sim 41\)：\(41\) 张颜色 \(1\)；\n- 位置 \(42 \sim 50\)：颜色 \(2, 3, \dots, 10\) 各 \(1\) 张；\n- 位置 \(51 \sim 70\)：颜色 \(11, 12, \dots, 30\) 各 \(1\) 张。\n按轮次 \(r = 1, 2, \dots, 20\) 操作。在第 \(r\) 轮开始时，上方 \(50\) 张为：位置 \(1 \sim 42-r\) 是 \(42-r\) 张颜色 \(1\)（\(42-r \ge 22 \ge 2\)），位置 \(43-r \sim 50\) 是颜色 \(2, \dots, r+9\) 的 \(r+8\) 张单牌（从上到下记为 \(c_1, \dots, c_{r+8}\)）；下方 \(20\) 张为 \(r-1\) 张颜色 \(1\) 以及颜色 \(r+10, \dots, 30\)。\n第 \(r\) 轮进行 \(r+9\) 次操作：\n1. 取下方颜色 \(r+10\) 作为 \(X\)，紧贴位置 \(42-r\) 的颜色 \(1\)（\(Y\)）上方插入，将 \(c_{r+8}\) 挤到位置 \(51\)；\n2. 接下来 \(r+8\) 步，依次取位置 \(51\) 处新挤出的单色牌 \(c_{r+8}, c_{r+7}, \dots, c_1\) 作为 \(X\)，每次紧贴同一张不断下移的颜色 \(1\)（此时位于位置 \(43-r, \dots, 50\)）上方插入，最终将该张颜色 \(1\) 挤到位置 \(51\)。\n第 \(r\) 轮结束后，下方增加 \(1\) 张颜色 \(1\)、减少颜色 \(r+10\)，上方变为 \(41-r\) 张颜色 \(1\) 与颜色 \(2, \dots, r+10\) 各 \(1\) 张，恰好进入第 \(r+1\) 轮状态。\(20\) 轮总操作次数为 \(\sum_{r=1}^{20} (r + 9) = 10 + 11 + \dots + 29 = 390\)。

**盲解结论**：(1) 证明见步骤（每次操作使非负整数势函数 \(\Psi = (50 - M) + \sum_{j=|S|+1}^{K-1} j\) 至少减少 \(1\)，故必在有限次操作后结束）。\n(2) 操作次数的最大可能值为 \(390\)。

### 2. 对照答案复盘

盲解结果完全正确：第一问严格证明了有限步终止，第二问准确求得最大操作次数为 \(390\)，且给出了完全一致的最优初始排布与逐轮“冒泡”构造。方法上，参考解答采用“仅保留每种颜色最上方一张不贴标签，其余贴标签”的精准计数论证，直接得出任意初态的精确上界 \(\sum_{j=1}^s (51-i_j)\) 再放缩至 \(390\)；盲解则采用“上方重复颜色牌的最大位置 \(M\) 与颜色数 \(|S|\) 的联合势函数 \(\Psi = (50-M) + \sum_{j=|S|+1}^{K-1} j\)”，并利用 \(K \le \min(30, |S_0|+20)\) 完成放缩，属于另一种完全等价且严密的有效解法。

### 3. 困难点与破局关键

- **识别单色牌循环中的单调量**：在顶部颜色数 \(|S|\) 不变的操作中，位于第 \(50\) 位的牌 \(Z\) 离开顶部后成为底部可用牌，之后又可被选为 \(X\) 放回顶部，形成“单色牌循环”。如果不找到一个能穿透这种循环的单调量（如最下方贴标签牌的位置，或重复颜色牌的最大位置 \(M\)），就很难证明有限性，更难得到紧的上界。
- **从粗略终止性到精确上界 \(390\) 的跃迁**：粗略的势函数（例如对所有重复颜色牌的 \((51-i)\) 求和）虽然能证明有限步终止，但其初值可达 \(\frac{50 \times 51}{2}=1275\)，远大于真正的最大值 \(390\)。必须结合“底部只有 \(20\) 张牌，故特殊颜色至多 \(20\) 种（或总颜色数 \(K \le |S_0|+20\)）”以及“前 \(20\) 种特殊颜色逐一引入顶部”这一约束，才能把上界精确卡死在 \(390\)。

### 4. 问题拆解（教学引导）

- **翻译操作机制与终止条件**：每次操作从下方 \(20\) 张取走 \(X\)（颜色不在上方 \(50\) 张中），放到上方 \(50\) 张中某张重复颜色牌 \(Y\) 的紧上方，导致原第 \(50\) 张牌 \(Z\) 被挤到第 \(51\) 位。先检查操作能否持续：只要存在 \(X\)，上方 \(50\) 张至多含 \(29\) 种颜色，由抽屉原理必存在至少出现两次的颜色 \(Y\)，因此终止条件完全等价于“所有颜色都在上方 \(50\) 张中出现”（或下方牌的颜色均已在上方出现）。
- **分析单步操作对颜色分布的影响**：把注意力集中在上方 \(50\) 张的颜色集合 \(S\) 上。\(X\) 的颜色原本不在 \(S\) 中，进入后在上方仅出现 \(1\) 次；而挤出的 \(Z\) 若在上方仅出现 \(1\) 次，则 \(|S|\) 不变；若 \(Z\) 在上方至少出现 \(2\) 次，则 \(|S|\) 严格增加 \(1\)。由此发现 \(|S|\) 单调不减，且“冗余牌”（每种颜色除最上方一张外的其余牌）只减不增。
- **寻找控制“循环步数”的势函数或标记法**：当 \(|S|\) 不变时，冗余牌（或贴标签牌）整体不会减少也不会上移，且因为 \(Y\) 本身属于重复颜色，\(Y\) 及其下方的冗余牌至少下移 \(1\) 位。由此自然想到用“最下方冗余牌的位置”或“所有最下方的 \(s\) 张冗余牌距底部的距离之和”来控制总步数。

### 5. 答案拆解（逻辑骨架）

- **第一步：定义特殊颜色与“贴标签”机制**（*动机*：将“上方能否再容纳新颜色”转化为“顶部有多少张冗余牌可以被挤到底部”，同时精准刻画顶部 \(50\) 张中的位置结构。）：称仅在底部 \(20\) 张中出现的颜色为“特殊颜色”，设初始有 \(s\) 种（\(0 \le s \le 20\)）。在顶部 \(50\) 张中，对每种颜色保留最上方的一张不贴标签，其余均贴上标签。由于顶部颜色数不超过 \(30 - s\)，故不贴标签的牌至多 \(30 - s\) 张，贴标签的牌至少 \(20 + s \ge s\) 张。设所有贴标签的牌从下到上位于第 \(i_1 > i_2 > \dots > i_l\) 位。
- **第二步：追踪标签数量与特殊颜色数的变化**（*动机*：建立“贴标签牌离开顶部”与“特殊颜色消耗”之间的一一对应，把终止条件转化为最下方 \(s\) 张贴标签牌离开顶部。）：规定贴标签的牌一旦进入底部就撕掉标签。每次操作中，新加入顶部的 \(X\) 颜色在顶部仅出现一次，故不会新增标签；而每当有一张贴标签的牌从第 \(50\) 位离开顶部，顶部就多出一种颜色（即减少一种特殊颜色）。因此过程终止当且仅当贴标签的牌恰好减少了 \(s\) 张（此时所有初始存在的颜色都已在顶部出现，或精确地说，最下方的 \(s\) 张贴标签的牌逐个离开顶部）。
- **第三步：利用位置单调性证明操作次数上界为 \(\sum_{j=1}^s (51 - i_j)\)**（*动机*：用位置下移的单调性直接给出从任意初始状态出发的精确操作次数上界，一并解决第 (1) 问和第 (2) 问的局面估值。）：每次操作中，上方至少有一张贴标签的牌（例如选作 \(Y\) 的颜色至少有两张，其最下方一张必贴标签）会向下方移动至少 \(1\) 位，从而顶部当前最下方的那张贴标签的牌必定下移 \(1\) 位且永不上移。因此，第 \(1\) 张贴标签牌离开顶部至多需 \(51 - i_1\) 步；此时第 \(2\) 张贴标签牌位置至少为 \(i_2\)，故其离开至多还需 \(51 - i_2\) 步；依此类推，总操作次数不超过 \(\sum_{j=1}^s (51 - i_j)\)（每次选最下方的贴标签牌作为 \(Y\) 即可取等）。
- **第四步：位置放缩求最大值 \(390\) 并给出构造**（*动机*：通过极端位置估计将关于位置 \(i_j\) 的和式放缩为关于 \(s\) 的二次函数，完成最值求解并反推出取等条件。）：由于初始顶部至多有 \(30 - s\) 张不贴标签的牌，且第 \(1\) 张牌必不贴标签，故在第 \(i_j\) 张牌下方至多有 \(29 - s\) 张不贴标签的牌以及 \(j - 1\) 张贴标签的牌，因此 \(i_j \ge 50 - (29 - s) - (j - 1) = 22 + s - j\)。代入求和得 \(\sum_{j=1}^s (51 - i_j) \le \sum_{j=1}^s (29 - s + j) = \frac{1}{2}s(59 - s)\)。结合 \(0 \le s \le 20\)，当 \(s = 20\) 时取得最大值 \(390\)，并以“前 \(41\) 张同色，第 \(42 \sim 70\) 张为其余 \(29\) 种颜色各一张”实现等号。

### 6. 易错点分析

- **边界与终止步的越界分析**：常见错法——忽略最后一步操作使 \(|S|\) 达到总颜色数 \(K\) 后立刻终止的边界情形，或直接假设每次操作后上方 \(50\) 张中仍存在重复颜色的牌 \(Y\)。；错因——当最后一次操作将最后一种未出现颜色引入上方 \(50\) 张时，操作结束后 \(|S|=K\)，此时上方可能不再满足进一步操作的条件，若未把“终止前”与“终止步”分开处理，势函数或最大位置的定义会出现空集越界。；避坑策略——在定义 \(M\)（或构造“贴标签”的牌）以及计算单调量差值时，显式区分“\(Z\) 在上方仅出现一次”与“\(Z\) 在上方至少出现两次”两种情形，并单独说明最后一步可能使 \(|S|=K\) 后过程立刻终止的边界情况。
- **误以为底部“可用牌”单调减少**：常见错法——误以为每次操作消耗底部 \(20\) 张中的一张“可用牌”，从而错误声称总操作次数或颜色增加次数不超过 \(20\)。；错因——当上方 \(50\) 张中仅出现 \(1\) 次的牌 \(Z\) 被挤到底部第 \(51\) 位时，\(Z\) 的颜色不再出现在上方 \(50\) 张中，此时底部中所有与 \(Z\) 同色的牌都会重新变为可选的 \(X\)，因此底部可用牌数和“顶部颜色数不变的操作”并不受限于 \(20\)。；避坑策略——严格追踪单种颜色离开上方 \(50\) 张的可能性，认识到“某颜色曾被挤出上方”不代表“该颜色永不再回来”，应通过“底部新颜色种类数 \(s\)（或贴标签牌总数减少量）”以及“整副牌总颜色数 \(K \le |S_0|+20\)”来建立全局界。
- **构造最值时插入位置选择不当**：常见错法——在构造 \(390\) 次操作时，误将新牌直接插在最上方（第 \(1\) 张），导致只能操作 \(20\) 次或达不到每步仅推进一步的效果。；错因——若把 \(X\) 插在远离底部的 \(Y\) 上方，会同时把大量重复颜色牌整体下推，浪费了后续可推动的步数；必须每次都选择尽量靠下的多色牌 \(Y\)（最好紧邻底部单色牌区）才能使推进步数最大化。；避坑策略——在构造达到 \(390\) 的例子时，必须明确写出“将单色牌依次从位置 \(51\) 放回上方、逼迫同一张多色牌逐位下移”的精确操作顺序，确保每一步都满足 \(X\) 在上方未出现且 \(Y\) 至少出现两次。

**教学小结**：在纸牌或队列移动类的组合最值问题中，当部分元素会在边界反复进出形成“循环”时，应尝试忽略元素具体身份、改用“每种颜色保留代表元，其余视为冗余（贴标签）”或“联合颜色数与最值位置构造势函数”的视角，把看似可逆的局部移动转化为整体不可逆的单调消耗。

---

## 2025 CMO 试题解答与评分标准 · 5（`cmo-2025-images-ba37a1fa50-combined-q5`）

- **学段**：高中 · **盲解结果**：盲解正确（不同有效解法）
- **教学标签**：训练:技巧进阶 / 变量代换与重参数化 / 放缩与估值 / 构造与反例 / 易错:边界与退化情形 / 易错:符号与方向 / 易错:充分性与必要性混淆
- **知识专题**：对称不等式 / 幂和与初等对称多项式 / 参数存在性证明

### 原题整理

求所有实数 \(\lambda\) 使得如下命题成立：存在仅依赖于 \(\lambda\) 的正整数 \(N\)，使得对任意正整数 \(n \geqslant N\) 及任意总和为 \(1\) 的非负实数 \(x_1, x_2, \cdots, x_n\)，都有
\[\left(\sum_{1 \leqslant i < j \leqslant n} x_i x_j\right)^2 \leqslant \lambda \cdot \left(\sum_{1 \leqslant i < j < k \leqslant n} x_i x_j x_k\right) + \frac{1}{n} \cdot \left(\sum_{1 \leqslant i < j \leqslant n} (x_i - x_j)^2\right).\]

### 1. 只看原题盲解尝试

**切入思路**：首先取均匀分布 \(x_1 = x_2 = \cdots = x_n = \frac{1}{n}\) 验证必要条件，得到 \(\lambda > \frac{3}{2}\)。随后记幂和 \(S_k = \sum_{i=1}^n x_i^k\)（\(k=1,2,3\)），利用对称多项式与幂和的恒等关系将不等式两侧全部用 \(S_2, S_3, n\) 表示，并结合柯西-施瓦茨不等式 \(S_3 \ge S_2^2\) 证明：当 \(\frac{3}{2} < \lambda \le 3\) 时取 \(N = \left\lceil \frac{12}{2\lambda - 3} \right\rceil\) 即可使不等式恒成立；当 \(\lambda > 3\) 时，利用 \(\sum_{1 \le i < j < k \le n} x_i x_j x_k \ge 0\) 将其归约到 \(\lambda = 3\) 的情形（取 \(N = 3\) 即可）。

**推演步骤**：
- 第一步（必要性）：证明 \(\lambda > \frac{3}{2}\)。假设 \(\lambda \leqslant \frac{3}{2}\)，对任意正整数 \(N\)，取正整数 \(n = \max\{N, 3\}\)，并令 \(x_1 = x_2 = \cdots = x_n = \frac{1}{n}\)。此时 \(x_i \geqslant 0\) 且 \(\sum_{i=1}^n x_i = 1\)，\(\sum_{1 \leqslant i < j \leqslant n} (x_i - x_j)^2 = 0\)。不等式左边为 \(\left(\binom{n}{2}\frac{1}{n^2}\right)^2 = \frac{(n-1)^2}{4n^2}\)，右边为 \(\lambda \binom{n}{3}\frac{1}{n^3} = \lambda \frac{(n-1)(n-2)}{6n^2}\)。由于 \(n \geqslant 3\)，有 \((n-1)(n-2) > 0\)，故由 \(\lambda \leqslant \frac{3}{2}\) 可得右边不超过 \(\frac{3}{2} \cdot \frac{(n-1)(n-2)}{6n^2} = \frac{(n-1)(n-2)}{4n^2} < \frac{(n-1)^2}{4n^2}\)，与原不等式矛盾。因此必有 \(\lambda > \frac{3}{2}\)。
- 第二步（恒等变形）：设 \(S_1 = \sum_{i=1}^n x_i = 1\)，\(S_2 = \sum_{i=1}^n x_i^2\)，\(S_3 = \sum_{i=1}^n x_i^3\)，以及 \(e_2 = \sum_{1 \leqslant i < j \leqslant n} x_i x_j\)，\(e_3 = \sum_{1 \leqslant i < j < k \leqslant n} x_i x_j x_k\)（当 \(n < 3\) 时 \(e_3 = 0\)）。由 \(1 = S_1^2 = S_2 + 2e_2\) 得 \(e_2 = \frac{1 - S_2}{2}\)。由 \(1 = S_1^3 = S_3 + 3(S_1 S_2 - S_3) + 6e_3 = 3S_2 - 2S_3 + 6e_3\) 得 \(e_3 = \frac{1 - 3S_2 + 2S_3}{6}\)。又 \(\sum_{1 \leqslant i < j \leqslant n} (x_i - x_j)^2 = \frac{1}{2}\sum_{i=1}^n \sum_{j=1}^n (x_i^2 - 2x_i x_j + x_j^2) = nS_2 - S_1^2 = nS_2 - 1\)，故 \(\frac{1}{n}\sum_{1 \leqslant i < j \leqslant n} (x_i - x_j)^2 = S_2 - \frac{1}{n}\)。
- 第三步（充分性，情形一：\(\frac{3}{2} < \lambda \leqslant 3\)）：取 \(N = \left\lceil \frac{12}{2\lambda - 3} \right\rceil\)（显然 \(N \geqslant 4\)）。对任意 \(n \geqslant N\) 及满足条件的非负实数 \(x_1, \cdots, x_n\)，由柯西-施瓦茨不等式有 \(S_1 S_3 = \left(\sum_{i=1}^n x_i\right)\left(\sum_{i=1}^n x_i^3\right) \geqslant \left(\sum_{i=1}^n x_i^2\right)^2 = S_2^2\)，即 \(S_3 \geqslant S_2^2\)。由于 \(\lambda > 0\)，将右边减去左边并乘以 \(12\)，得：
\[12(\text{RHS} - \text{LHS}) = 2\lambda(1 - 3S_2 + 2S_3) + 12S_2 - \frac{12}{n} - 3(1 - S_2)^2 \geqslant 2\lambda(1 - 3S_2 + 2S_2^2) + 12S_2 - \frac{12}{n} - 3(1 - 2S_2 + S_2^2) = (4\lambda - 3)S_2^2 + 6(3 - \lambda)S_2 + \left(2\lambda - 3 - \frac{12}{n}\right).\]
因为 \(\frac{3}{2} < \lambda \leqslant 3\) 且 \(S_2 \geqslant 0\)，所以 \(4\lambda - 3 > 0\)，\(3 - \lambda \geqslant 0\)，且由 \(n \geqslant \frac{12}{2\lambda - 3}\) 知 \(2\lambda - 3 - \frac{12}{n} \geqslant 0\)。从而 \(\text{RHS} - \text{LHS} \geqslant 0\)，原不等式成立。
- 第四步（充分性，情形二：\(\lambda > 3\)）：取 \(N = 3\)。对任意 \(n \geqslant 3\)，由第三步在 \(\lambda = 3\) 时的推导，有 \(12\left(3e_3 + S_2 - \frac{1}{n} - e_2^2\right) \geqslant 9S_2^2 - 1\)。又由柯西-施瓦茨不等式知 \(S_2 = \sum_{i=1}^n x_i^2 \geqslant \frac{1}{n}\left(\sum_{i=1}^n x_i\right)^2 = \frac{1}{n}\)（特别地当 \(n = 3\) 时 \(9S_2^2 \geqslant 1\)，而当 \(n \geqslant 4\) 时 \(12\left(3e_3 + S_2 - \frac{1}{n} - e_2^2\right) \geqslant 9S_2^2 + 3 - \frac{12}{n} > 0\)），因此对所有 \(n \geqslant 3\) 均有 \(e_2^2 \leqslant 3e_3 + S_2 - \frac{1}{n}\)。又因 \(x_i \geqslant 0\)，有 \(e_3 \geqslant 0\)，从而当 \(\lambda > 3\) 时 \(\lambda e_3 \geqslant 3e_3\)，故 \(e_2^2 \leqslant \lambda e_3 + S_2 - \frac{1}{n}\) 成立。综上，所有满足条件的 \(\lambda\) 为 \(\lambda > \frac{3}{2}\)。

**盲解结论**：所有满足条件的实数 \(\lambda\) 的集合为 \(\left(\frac{3}{2}, +\infty\right)\)，即 \(\lambda > \frac{3}{2}\)。

### 2. 对照答案复盘

Turn 1 盲解完全独立地得出了正确答案 \(\lambda > \frac{3}{2}\)，且在必要性与充分性两方面均给出了严格完整的证明。两者在必要性部分完全一致（均取 \(x_1 = \cdots = x_n = \frac{1}{n}\) 排除 \(\lambda \le \frac{3}{2}\)）。在充分性部分采用了不同的有效方法：参考解答先借助 \(e_3 \ge 0\) 将固定 \(\lambda > \frac{3}{2}\) 归约到随 \(n\) 变化的精确阈值 \(\frac{3(n-1)}{2(n-2)}\)，再作中心化代换 \(d_i = x_i - \frac{1}{n}\)，把不等式化为 \(A = \sum d_i^2\) 与 \(\sum d_i^3\) 的关系并利用 \(d_i \ge -\frac{1}{n}\) 与 \(A \le \frac{n-1}{n}\) 完成对所有 \(n \ge 3\) 的放缩；而 Turn 1 直接用幂和 \(S_2 = \sum x_i^2\) 与 \(S_3 = \sum x_i^3\) 表示各项，利用柯西-施瓦茨不等式 \(S_3 \ge S_2^2\) 对 \(\frac{3}{2} < \lambda \le 3\) 直接导出显式阈值 \(N = \left\lceil \frac{12}{2\lambda - 3} \right\rceil\)，再利用 \(e_3 \ge 0\) 覆盖 \(\lambda > 3\)。参考解答给出了对 \(n \ge 3\) 的最优系数界，Turn 1 的幂和法计算量更小且无需寻找精确常数 \(\frac{3(n-1)}{2(n-2)}\)。

### 3. 困难点与破局关键

- **三元对称和的化简与结构转化**：既可以用 \(d_i = x_i - \frac{1}{n}\) 做中心化把常数项消去、把二次误差项写成 \(A = \sum d_i^2\)，也可以直接把 \(e_2, e_3\) 与 \(\sum (x_i - x_j)^2\) 全部写成幂和 \(S_2, S_3\) 的线性组合；若直接硬展开 \(x_i x_j x_k\) 而不转成幂和或中心化变量，式子会非常繁琐。
- **处理量词“存在 \(N(\lambda)\)”与渐近取等结构**：不等式右端的系数 \(\lambda\) 是常数，但在 \(x_i = \frac{1}{n}\) 处不等式随 \(n\) 渐近取等（而非对有限 \(n\) 取等）。参考解答通过将 \(\lambda\) 替换为紧阈值 \(\frac{3(n-1)}{2(n-2)}\) 来精确消去常数项；或者如另一种思路那样利用余量 \(2\lambda - 3 > 0\) 对抗 \(-\frac{1}{n}\) 的误差项。如何把“\(n\) 充分大”这一量词精准地落到代数不等式中是本题的思维跃迁点。
- **三次矩与二次矩的恰当放缩**：无论化为 \((d_i)\) 还是 \((S_2, S_3)\)，最终都会出现三次幂和（\(\sum d_i^3\) 或 \(S_3\)）与二次幂和（\(A\) 或 \(S_2\)）的比较。关键在于利用非负性约束 \(x_i \ge 0\)：参考解答中体现为 \(d_i \ge -\frac{1}{n}\)，从而 \(\sum d_i^3 \ge -\frac{1}{n}A\)；幂和法中则体现为柯西-施瓦茨不等式 \(S_1 S_3 \ge S_2^2\)。

### 4. 问题拆解（教学引导）

- **1. 先用特值探路求必要条件**：题目要求找 \(\lambda\) 使得“存在 \(N(\lambda)\)，对一切 \(n \ge N\) 及非负和为 \(1\) 的变量不等式成立”。遇到这类带全称量词与存在量词的不等式参数问题，第一步先代特值（尤其是对称点 \(x_i = \frac{1}{n}\)）探测 \(\lambda\) 的必要下界。
- **2. 识别对称多项式与幂和的结构联系**：在 \(\sum x_i = 1\) 条件下，\(\sum_{i<j}(x_i-x_j)^2 = n\sum x_i^2 - 1\)，\(\sum_{i<j} x_i x_j = \frac{1-\sum x_i^2}{2}\)，且 \(\sum_{i<j<k} x_i x_j x_k\) 可由牛顿恒等式用 \(\sum x_i^2\) 和 \(\sum x_i^3\) 表示。整个不等式实质上只涉及二阶和与三阶和的关系。
- **3. 利用非负性确认 \(\lambda\) 的单调性**：由于 \(x_i \ge 0\)，必有 \(\sum_{i<j<k} x_i x_j x_k \ge 0\)，说明关于 \(\lambda\) 具有单调性：若 \(\lambda_0\) 满足条件，则所有 \(\lambda \ge \lambda_0\) 自动满足。因此只需关心临界值 \(\frac{3}{2}\) 右侧任意靠近 \(\frac{3}{2}\) 的 \(\lambda\) 是否可行。

### 5. 答案拆解（逻辑骨架）

- **第一步：特值构造确定 \(\lambda > \frac{3}{2}\)**（*动机*：探测 \(\lambda\) 的下界，并精确区分 \(\lambda > \frac{3}{2}\) 与 \(\lambda \ge \frac{3}{2}\)。）：令 \(x_1 = x_2 = \cdots = x_n = \frac{1}{n}\)，此时差平方和为 \(0\)，不等式化为 \(\lambda \frac{\binom{n}{3}}{n^3} \ge \left(\frac{\binom{n}{2}}{n^2}\right)^2\)，即 \(\lambda \ge \frac{3}{2}\cdot\frac{n-1}{n-2}\)。因为对所有 \(n \ge 3\) 均有 \(\frac{n-1}{n-2} > 1\)，故必然要求 \(\lambda > \frac{3}{2}\)。
- **第二步：归约到随 \(n\) 变化的精确阈值 \(\frac{3n-3}{2n-4}\)**（*动机*：把固定参数 \(\lambda\) 转化为使 \(x_i = \frac{1}{n}\) 恰好取等的有限 \(n\) 阈值，便于后续恒等变形后常数项完全抵消。）：对任意 \(\lambda > \frac{3}{2}\)，因 \(\lim_{n\to\infty}\frac{3n-3}{2n-4} = \frac{3}{2}\)，故存在 \(N \ge 3\) 使 \(n \ge N\) 时 \(\frac{3n-3}{2n-4} \le \lambda\)。再由 \(\sum_{i<j<k} x_i x_j x_k \ge 0\)，只需对所有 \(n \ge 3\) 证明系数为 \(\frac{3n-3}{2n-4}\) 的齐次化不等式即可。
- **第三步：中心化代换化简不等式**（*动机*：由于不等式在 \(x_i = \frac{1}{n}\) 处取等，中心化代换能自动消去零阶和一阶项，暴露出高阶小量的真正主导关系。）：令 \(d_i = x_i - \frac{1}{n}\)，则 \(\sum d_i = 0\)。设 \(A = \sum d_i^2\)，利用 \(\sum_{i<j} d_i d_j = -\frac{1}{2}A\) 及 \(\sum_{i<j<k} d_i d_j d_k = \frac{1}{3}\sum d_i^3\)，将原不等式各项展开为 \(A\) 与 \(\sum d_i^3\) 的表达式，常数项 \(\frac{(n-1)^2}{4n^2}\) 恰好抵消，化简为 \(A \ge \frac{n-1}{4n}A - \frac{n-1}{2(n-2)}\sum d_i^3 + \frac{1}{4}A^2\)。
- **第四步：利用下界 \(d_i \ge -\frac{1}{n}\) 与上界 \(A \le \frac{n-1}{n}\) 完成放缩**（*动机*：利用变量非负性分别控制平方项 \(A^2\) 的上界与三次和 \(\sum d_i^3\) 的下界，从而一次性完成对所有 \(n \ge 3\) 的证明。）：由 \(x_i \ge 0\) 和 \(\sum x_i = 1\)，一方面有 \(A = \sum x_i^2 - \frac{1}{n} \le 1 - \frac{1}{n} = \frac{n-1}{n}\)，故 \(\frac{1}{4}A^2 \le \frac{n-1}{4n}A\)；另一方面由 \(d_i = x_i - \frac{1}{n} \ge -\frac{1}{n}\)，有 \(\sum d_i^3 = \sum d_i \cdot d_i^2 \ge -\frac{1}{n}A\)。代入右边得其不超过 \(\frac{(n-1)^2}{2n(n-2)}A\)，而 \(n \ge 3\) 时 \(\frac{(n-1)^2}{2n(n-2)} < 1\)，从而不等式成立。

### 6. 易错点分析

- **误判临界值 \(\lambda = \frac{3}{2}\) 成立**：常见错法——仅求极限 \(\lim_{n\to\infty}\frac{3n-3}{2n-4} = \frac{3}{2}\) 就误判 \(\lambda \ge \frac{3}{2}\) 均成立，忽略了 \(\frac{3n-3}{2n-4} > \frac{3}{2}\)（阅卷评分标准中亦特别指出此常见扣分点）。；错因——不等号方向是 \(\lambda \ge \frac{3(n-1)}{2(n-2)}\)，而对一切 \(n \ge 3\) 均有 \(\frac{n-1}{n-2} > 1\)，故 \(\lambda = \frac{3}{2}\) 在所有 \(n \ge 2\) 时均被 \(x_i = \frac{1}{n}\) 严格违背。；避坑策略——对 \(\frac{3(n-1)}{2(n-2)}\) 做带余分离常数：\(\frac{3}{2}\cdot\frac{n-1}{n-2} = \frac{3}{2}\left(1 + \frac{1}{n-2}\right) > \frac{3}{2}\)，明确其从右侧趋近于 \(\frac{3}{2}\)，从而排除临界值 \(\lambda = \frac{3}{2}\)。
- **中心化代换后忽略变量可负与符号方向**：常见错法——引入中心化变量 \(d_i = x_i - \frac{1}{n}\) 后，误把 \(d_i\) 当作非负实数处理，或直接忽略 \(\sum d_i^3\) 的符号而错误使用均值不等式。；错因——中心化后满足 \(\sum d_i = 0\)，\(d_i\) 有正有负且下界为 \(-\frac{1}{n}\)，因此 \(\sum d_i^3\) 可正可负，必须利用 \(d_i \ge -\frac{1}{n}\) 得到 \(\sum d_i^3 \ge -\frac{1}{n}\sum d_i^2\) 来控制其下界。；避坑策略——代换后立即写出变量范围 \(d_i \ge -\frac{1}{n}\) 与 \(\sum_{i=1}^n d_i = 0\)，并核对不等式放缩时各项的符号；必要时用具体数值（如 \(n=3\)，\(x=(1,0,0)\)）检验放缩方向。
- **混淆局部渐近成立与一致成立**：常见错法——只验证了少量特例或仅在 \(x_i\) 接近 \(\frac{1}{n}\) 的局部微扰下做渐近展开，未给出对所有非负数组及充分大 \(n\) 一致成立的证明。；错因——题目要求存在仅依赖于 \(\lambda\) 的 \(N\)，使对一切 \(n \ge N\) 及全部非负和为 \(1\) 的数组都成立，包含如 \(x_1=1, x_2=\dots=x_n=0\) 等远离中心点的边界情形，必须全局估计。；避坑策略——在证明充分性时，严格写出 \(N\) 关于 \(\lambda\) 的明确表达式或存在性依据，并保证所用的放缩（如 \(e_3 \ge 0\)、\(d_i \ge -\frac{1}{n}\)）对所有满足 \(\sum x_i = 1, x_i \ge 0\) 的 \(n\) 元数组一致有效。

**教学小结**：面对带渐近量词“存在 \(N(\lambda)\)”的对称不等式，既可以通过中心化代换 \(d_i = x_i - \frac{1}{n}\) 消去平衡点处的常数项并结合边界约束 \(d_i \ge -\frac{1}{n}\) 放缩，也可以直接化成幂和 \(S_2, S_3\) 后用柯西-施瓦茨不等式 \(S_3 \ge S_2^2\) 解决；同时务必检查有限 \(n\) 下阈值函数是从左侧还是右侧趋近极限，避免在临界值处失分。

---

## 2025 CMO 试题解答与评分标准 · 6（`cmo-2025-images-ba37a1fa50-combined-q6`）

- **学段**：高中 · **盲解结果**：盲解正确（不同有效解法）
- **教学标签**：训练:压轴攻坚 / 奇偶与同余 / 变量代换与重参数化 / 局部-整体转化 / 易错:边界与退化情形 / 易错:充分性与必要性混淆 / 易错:隐含假设与越界推广
- **知识专题**：线性递推数列 / 同余与p进赋值 / 中国剩余定理

### 原题整理

给定大于 \(1\) 的奇数 \(n\)。已知 \(n\) 的每个素因子 \(p\) 都满足 \(p-1\) 与 \(n\) 互素。求同时满足下述两个条件的有序数组 \((a, b, c)\) 的个数：
(i) \(a, b, c \in \{1, 2, \cdots, n\}\)，且不存在素数同时整除 \(a, b, c, n\)；
(ii) 存在 \(1, 2, \cdots, n\) 的排列 \(x_1, x_2, \cdots, x_n\)，使得对 \(k = 1, 2, \cdots, n\) 都有
\[ n \mid a x_{k+2} + b x_{k+1} + c x_k, \]
其中 \(x_{n+1} = x_1\)，\(x_{n+2} = x_2\)。

### 1. 只看原题盲解尝试

**切入思路**：利用算子多项式与模素数幂分析线性递推数列在周期为 \(n\) 的排列条件下的限制：先在模每个素因子 \(p \mid n\) 下利用 \(\gcd(p-1,n)=1\) 与多项式最大公因式确定 \(p \nmid a\) 且 \(aT^2+bT+c \equiv a(T-1)^2 \pmod{p}\)；再借助差分算子 \(\Delta = S - I\) 分析模 \(p^e\) 下的周期与遍历性（区分 \(p \ge 5\) 与 \(p=3, e \ge 2\) 两种情况）；最后由中国剩余定理（CRT）将各素数幂的结果合并，从而算出满足条件的 \((a,b,c)\) 总数。

**推演步骤**：
- **第一步：模素因子 \(p\) 的必要条件。** 设 \(p\) 是 \(n\) 的任意一个素因子，且 \(p^e \parallel n\)，记 \(n = p^e m\)，其中 \(p \nmid m\)。将 \((x_k)\) 以周期 \(n\) 延拓为整数指标数列，并令 \(y_k = x_k \bmod p \in \mathbb{F}_p\)。由条件 (i) 知 \(p\) 不能同时整除 \(a, b, c\)，故多项式 \(P(T) = aT^2 + bT + c \in \mathbb{F}_p[T]\) 是次数不超过 \(2\) 的非零多项式。记左移算子 \(S\) 满足 \((Sy)_k = y_{k+1}\)，则 \(P(S)y = 0\) 且 \((S^n - 1)y = 0\)。令 \(g(T) = \gcd(P(T), T^n - 1) \in \mathbb{F}_p[T]\)（首一），由裴蜀定理有 \(g(S)y = 0\)。又因 \(x_1, \dots, x_n\) 是 \(1, \dots, n\) 的排列，每个模 \(p\) 余数在 \((y_1, \dots, y_n)\) 中均恰好出现 \(n/p = p^{e-1}m\) 次，故 \(y_k\) 取遍 \(\mathbb{F}_p\) 中的 \(p \ge 3\) 个值，非零且非常数。若 \(\deg g = 0\)，则 \(y_k \equiv 0\)，矛盾；若 \(\deg g = 1\)，设 \(g(T) = T - r\)，由 \(T^n - 1 = (T^m - 1)^{p^e}\) 知 \(r^m = 1\)，结合 \(r^{p-1} = 1\) 与 \(\gcd(p-1, n) = 1\)（从而 \(\gcd(p-1, m) = 1\)）得 \(r = 1\)，于是 \(y_{k+1} = y_k\) 为常数，矛盾。因此 \(\deg g = 2\)，这迫使 \(p \nmid a\) 且 \(P(T) \mid (T^m - 1)^{p^e}\)（在 \(\mathbb{F}_p[T]\) 中）。
- **第二步：确定 \(P(T) \bmod p\) 的形式。** 因为 \(p \nmid m\)，多项式 \(T^m - 1\) 在 \(\mathbb{F}_p\) 上无重根。若 \(P(T)\) 在 \(\overline{\mathbb{F}_p}\) 中无重根，则由 \(P(T) \mid (T^m - 1)^{p^e}\) 推出 \(P(T) \mid T^m - 1\)，从而 \((S^m - 1)y = 0\)，即 \(y_{k+m} = y_k\)。于是 \((y_1, \dots, y_n)\) 由 \((y_1, \dots, y_m)\) 重复 \(n/m = p^e\) 次构成，每个模 \(p\) 余数出现次数必为 \(p^e\) 的倍数，但这与每个余数恰好出现 \(p^{e-1}m\) 次（且 \(p \nmid m\)）矛盾。故 \(P(T)\) 在 \(\overline{\mathbb{F}_p}\) 中必有重根，即 \(P(T) = a(T - r)^2\)，其中 \(r = -b/(2a) \in \mathbb{F}_p\)（因 \(p\) 为奇素数）。由 \(r^m = 1\)、\(r^{p-1} = 1\) 及 \(\gcd(p-1, m) = 1\) 得 \(r = 1\)。因此对每个素因子 \(p \mid n\)，必有 \(p \nmid a\)，\(b \equiv -2a \pmod{p}\)，\(c \equiv a \pmod{p}\)（从而 \(\gcd(a, n) = \gcd(c, n) = 1\)）。
- **第三步：模素数幂 \(p^e\)（\(p^e \parallel n\)）的充要条件。** 由于 \(p \nmid a\)，令 \(\tilde{b} \equiv a^{-1}b \pmod{p^e}\)、\(\tilde{c} \equiv a^{-1}c \pmod{p^e}\)，则 \(\tilde{b} \equiv -2 \pmod{p}\)、\(\tilde{c} \equiv 1 \pmod{p}\)。记 \(\tilde{P}(T) = T^2 + \tilde{b}T + \tilde{c}\)。令 \(\Delta = T - 1\)，可写为 \(\tilde{P}(1+\Delta) = \Delta^2 + pu\Delta + pw\)（其中 \(pu \equiv \tilde{b}+2 \pmod{p^e}\)，\(pw \equiv 1+\tilde{b}+\tilde{c} \pmod{p^e}\)）。在 \(\mathbb{Z}[\Delta]\) 中模 \(\tilde{P}(1+\Delta)\)，有 \(\Delta^2 \equiv -p(u\Delta + w)\)，进而由归纳法对任意 \(j \ge 2\) 有 \(\Delta^j \equiv 0 \pmod{p^{\lfloor j/2 \rfloor}, \tilde{P}(1+\Delta)}\)。
1. 若 \(p \ge 5\)：在 \((1+\Delta)^p - 1 = \sum_{j=1}^{p-1}\binom{p}{j}\Delta^j + \Delta^p\) 中，\(2 \le j \le p-1\) 时 \(p \mid \binom{p}{j}\) 且 \(\Delta^j \equiv 0 \pmod{p}\)，而 \(j = p\) 时 \(\lfloor p/2 \rfloor = \frac{p-1}{2} \ge 2\) 故 \(\Delta^p \equiv 0 \pmod{p^2}\)。因此 \((1+\Delta)^p - 1 \equiv p\Delta \pmod{p^2, \tilde{P}(1+\Delta)}\)。归纳可得对一切 \(r \ge 1\)，
\[ (1+\Delta)^{p^r} - 1 \equiv p^r \Delta \pmod{p^{r+1}, \tilde{P}(1+\Delta)}. \]
特别地，取 \(r=e\) 知任意满足 \(\tilde{P}(S)z \equiv 0 \pmod{p^e}\) 的数列 \(z\) 自动以 \(p^e\) 为周期；取初值 \(z_1 = 0, z_2 = 1\)，因 \(\Delta z_k = z_{k+1} - z_k \equiv 1 \pmod{p}\)，由上式对 \(0 \le r \le e-1\) 得 \(z_{k+p^r} - z_k \equiv p^r \pmod{p^{r+1}}\)。对任意 \(1 \le i < j \le p^e\)，写 \(j - i = t p^r\)（\(0 \le r \le e-1, p \nmid t\)），则 \(z_j - z_i \equiv t p^r \not\equiv 0 \pmod{p^{r+1}}\)，故 \(z_1, \dots, z_{p^e}\) 构成模 \(p^e\) 的完全剩余系。于是 \(p \ge 5\) 时对 \((a,b,c) \bmod p^e\) 无额外限制。
2. 若 \(p = 3\)：当 \(e = 1\) 时同上，\(\tilde{b} \equiv 1, \tilde{c} \equiv 1 \pmod{3}\) 已足够（如 \(z_k = k\)）。当 \(e \ge 2\) 时，模 \(\tilde{P}(1+\Delta) = \Delta^2 + 3u\Delta + 3w\) 计算：
\[ (1+\Delta)^3 - 1 = 3\Delta + 3\Delta^2 + \Delta^3 \equiv 3(1-w)\Delta + 9(u^2-u)\Delta + 9w(u-1) \pmod{\tilde{P}(1+\Delta)}. \]
- 若 \(w \equiv 1 \pmod{3}\)（即 \(a+b+c \equiv 3a \pmod{9}\)），则 \((1+\Delta)^3 - 1 \equiv 0 \pmod{9, \tilde{P}(1+\Delta)}\)，归纳得 \((1+\Delta)^{3^{e-1}} - 1 \equiv 0 \pmod{3^e, \tilde{P}(1+\Delta)}\)。从而 \(x_k \bmod 3^e\) 必满足 \(x_{k+3^{e-1}} \equiv x_k \pmod{3^e}\)；因 \(3^{e-1} \mid n\)，\((x_1 \bmod 3^e, \dots, x_n \bmod 3^e)\) 最多取 \(3^{e-1}\) 个不同值，不可能取遍 \(\mathbb{Z}/3^e\mathbb{Z}\)，矛盾！
- 若 \(w \not\equiv 1 \pmod{3}\)（即 \(a+b+c \not\equiv 3a \pmod{9}\)），则 \(Y_1 = (1+\Delta)^3 - 1 \equiv 3(1-w)\Delta \pmod{9, \tilde{P}(1+\Delta)}\)；又由 \(\Delta^2, \Delta^3 \equiv 0 \pmod{3, \tilde{P}(1+\Delta)}\) 可得 \(3 Y_1^2, Y_1^3 \equiv 0 \pmod{81, \tilde{P}(1+\Delta)}\)，从而 \(Y_2 \equiv 3Y_1 \equiv 9(1-w)\Delta \pmod{27, \tilde{P}(1+\Delta)}\)，进而归纳对一切 \(r \ge 1\) 有
\[ (1+\Delta)^{3^r} - 1 \equiv 3^r (1-w)\Delta \pmod{3^{r+1}, \tilde{P}(1+\Delta)}. \]
同样取 \(r=e\) 知任意解周期整除 \(3^e\)，取 \(z_1=0, z_2=1\) 得 \(z_{k+3^r} - z_k \equiv 3^r(1-w)^{\mathbf{1}_{r \ge 1}} \not\equiv 0 \pmod{3^{r+1}}\)（\(0 \le r \le e-1\)），故 \(z_1, \dots, z_{3^e}\) 构成模 \(3^e\) 的完全剩余系。
- **第四步：由 CRT 合并并计数。** 综上所述，条件 (i)(ii) 对 \((a,b,c)\) 成立的必要条件是：对 \(n\) 的每个素数幂因子 \(p_i^{e_i} \parallel n\)，均有 \(p_i \nmid a\)，\(b \equiv -2a \pmod{p_i}\)，\(c \equiv a \pmod{p_i}\)，且当 \(p_i = 3\)、\(e_i \ge 2\) 时还需 \(a + b + c \not\equiv 3a \pmod{9}\)。反之，若 \((a,b,c)\) 满足上述条件，则对每个 \(i\) 均存在周期为 \(p_i^{e_i}\) 的模 \(p_i^{e_i}\) 排列数列 \((z_k^{(i)})\)；由 CRT 取 \(x_k \in \{1, \dots, n\}\) 使 \(x_k \equiv z_k^{(i)} \pmod{p_i^{e_i}}\)（\(1 \le i \le s\)），则 \((x_k)\) 满足递推式与周期 \(n\)，且 \(x_j \equiv x_k \pmod{n} \iff \forall i, z_j^{(i)} \equiv z_k^{(i)} \pmod{p_i^{e_i}} \iff \forall i, j \equiv k \pmod{p_i^{e_i}} \iff j \equiv k \pmod{n}\)，故 \(x_1, \dots, x_n\) 确为 \(1, \dots, n\) 的排列。计算模 \(p_i^{e_i}\) 的合法 \((a,b,c)\) 组数：当 \(p_i \ge 5\) 或 \((p_i, e_i) = (3, 1)\) 时，\(a\) 有 \(\varphi(p_i^{e_i}) = (p_i - 1)p_i^{e_i - 1}\) 种取法，\(b, c\) 各有 \(p_i^{e_i - 1}\) 种取法，共 \((p_i - 1)p_i^{3e_i - 3}\) 组；当 \(p_i = 3\) 且 \(e_i \ge 2\) 时，\(a, b\) 确定后 \(c \equiv a \pmod{3}\) 的 \(3^{e_i - 1}\) 个取值中有 \(\frac{2}{3}\) 满足 \(a+b+c \not\equiv 3a \pmod{9}\)，故共 \(\frac{2}{3}(3-1)3^{3e_i - 3} = 4 \cdot 3^{3e_i - 4}\) 组。由 CRT 相乘即得最终答案。

**盲解结论**：设 \(n\) 的标准素因数分解为 \(n = \prod_{i=1}^s p_i^{e_i}\)（其中 \(p_1, \dots, p_s\) 为互异奇素数，\(e_i \ge 1\)），记 \(R = \prod_{i=1}^s p_i\) 为 \(n\) 的所有不同素因子之积，\(\varphi(n)\) 为欧拉函数。则满足条件的有序数组 \((a, b, c)\) 的个数为：
- 当 \(9 \nmid n\) 时，个数为
\[ \frac{n^2 \varphi(n)}{R^2} = \prod_{i=1}^s (p_i - 1) p_i^{3e_i - 3}; \]
- 当 \(9 \mid n\) 时，个数为
\[ \frac{2 n^2 \varphi(n)}{3 R^2} = \frac{2}{3} \prod_{i=1}^s (p_i - 1) p_i^{3e_i - 3}. \]

**盲解时的疑虑/卡点**：无实质性不确定之处。全部推演（包括 \(p \ge 5\) 与 \(p=3, e \ge 2\) 的差异、以及 \(\gcd(a,n)>1\) 或 \(\gcd(c,n)>1\) 的不可能情形）均已严格证明，且对 \(n=3, 5, 7, 9, 15, 25, 27, 45, 75, 81\) 等小规模数值用程序进行了交叉检验，结果完全吻合。

### 2. 对照答案复盘

盲解与参考答案的最终结果完全一致（\(9 \nmid n\) 时为 \(\frac{n^2 \varphi(n)}{(\prod_{p \mid n} p)^2}\)，\(9 \mid n\) 时需乘以 \(\frac{2}{3}\)），且每一步逻辑均严密无误。两者采用了两条不同但等价的路径：参考答案通过重参数化 \(b \equiv -2u\)、\(c \equiv u^2 - v \pmod{n}\) 写出二项式展开通项，并借助升幂定理（LTE）与 \(v_p((2i+1)!)\) 估值完成模素数幂分析；盲解则采用移位算子 \(S = I + \Delta\) 与多项式模同余，在 \(\mathbb{F}_p[T]\) 中利用 \(T^m - 1\) 的无重根性直接导出 \(P(T) \equiv a(T-1)^2 \pmod{p}\)，再以差分算子归纳计算 \((1+\Delta)^{p^r}-1\)，同样精准刻画了 \(p \ge 5\) 与 \(p=3, 9 \mid n\) 的分化。

### 3. 困难点与破局关键

- **排列约束向特征根与 \(p\)-进间距的转化**：如何处理“排列周期为 \(n\)”这一全局组合条件与线性递推的关系：既不能让序列在模 \(p\) 下因出现非 \(1\) 特征根而导致周期无法覆盖全部剩余类，又要从模 \(p\) 的必要条件进一步追踪到任意素数幂 \(p^\beta \parallel n\) 下的单射性与周期性。
- **\(p = 3\) 在高次幂 \(3^\beta\)（\(\beta \ge 2\)）下的退化与抵消现象**：当 \(p = 3\) 且 \(9 \mid n\) 时，二阶项 \(\binom{k}{3} v\) 中的 \(3\)-进赋值不再严格压过一次项 \(k u^{k-1}\)，必须精细区分 \(v \equiv 0, 3, 6 \pmod{9}\)（等价于 \(a+b+c \not\equiv 3a \pmod{9}\) 否决 \(v \equiv 6 \pmod{9}\)）。

### 4. 问题拆解（教学引导）

- **第一步：把排列与整除条件翻译为模 \(n\) 线性递推及归一化**：条件 (ii) 实质上是关于循环序列 \((x_k)_{k \in \mathbb{Z}/n\mathbb{Z}}\) 的常系数二阶线性递推 \(a x_{k+2} + b x_{k+1} + c x_k \equiv 0 \pmod{n}\)。由 \(1, \dots, n\) 构成模 \(n\) 完系，先对每个素因子 \(p \mid n\) 考虑 \(\gcd(a, p)\) 与 \(\gcd(c, p)\)，排除退化情形从而完成归一化（如令 \(a=1\)、\(x_0=0, x_1=1\)）。
- **第二步：挖掘关键条件“\(n\) 为奇数”与“\(\gcd(p-1, n) = 1\)”的作用**：注意到题设“\(n\) 为奇数”保证了 \(2\) 模 \(n\) 可逆（从而可配方令 \(b \equiv -2u, c \equiv u^2 - v\)），而“对每个素因子 \(p \mid n\) 有 \(\gcd(p-1, n) = 1\)”提示在模 \(p\) 下应用费马小定理或 \(T^n - 1\) 的根时，\(1\) 将是唯一可能的 \(\mathbb{F}_p\) 根。
- **第三步：借助中国剩余定理进行素数幂分解与局部检验**：利用中国剩余定理（CRT）将模 \(n\) 的计数与构造问题拆解为各素数幂 \(p^\beta \parallel n\) 上的问题；在每个 \(p^\beta\) 上，只需保证序列周期整除 \(p^\beta\) 且满足“\(p^\alpha \parallel k - \ell \iff p^\alpha \parallel x_k - x_\ell\)”，再重点检查小素数 \(p=3\) 是否出现例外。

### 5. 答案拆解（逻辑骨架）

- **步骤一：归一化与二项式通项公式**（*动机*：消除自由度并建立显式通项公式，避免在抽象递推中反复讨论初值。）：先证对任意 \(p \mid n\) 有 \(p \nmid a\)（否则 \(p\) 整除 \(a, b, c\) 中的两个会推出所有 \(x_k\) 被 \(p\) 整除，仅 \(p \mid a\) 则会推出 \(p \mid x_{k+1} \iff p \mid x_k\)，均与完系矛盾）。因此 \(\gcd(a, n) = 1\)，可乘 \(a^{-1}\) 归一化为 \(a=1\)（最终乘 \(\varphi(n)\)）。再将下标平移使 \(x_0 = 0\)，同理证 \(\gcd(x_1, n)=1\)，乘 \(x_1^{-1}\) 归一化为 \(x_1 = 1\)。由于 \(n\) 为奇数，可取 \(u, v\) 使 \(2u \equiv -b \pmod{n}\)、\(u^2 - v \equiv c \pmod{n}\)（且取 \(v\) 非平方数），得通项公式 \(x_k \equiv \frac{(u+\sqrt{v})^k - (u-\sqrt{v})^k}{2\sqrt{v}} \equiv \sum_{i=0}^{\lfloor (k-1)/2 \rfloor} \binom{k}{2i+1} u^{k-2i-1} v^i \pmod{n}\)。这一步把复杂的同余递推完全显式化为二项式和，是后续 \(p\)-进分析的基础。
- **步骤二：模 \(p\) 分析导出必要条件 \(p \mid v\) 且 \(p \mid u-1\)**（*动机*：利用模 \(p\) 的循环周期性与完系均匀性，限制特征根的判别式 \(v\) 与中心 \(u\)。）：若 \(p \nmid v\)，在 \(\mathbb{Z}[\sqrt{v}]\) 中利用二项式展开与费马小定理及欧拉准则，得到 \((u \pm \sqrt{v})^{p^2} - (u \pm \sqrt{v}) \equiv 0 \pmod{p}\)，从而 \(x_{k+p^2-1} \equiv x_k \pmod{p}\)。这意味着模 \(p\) 的每个剩余类出现次数必为 \(\frac{n}{\gcd(n, p^2-1)}\) 的倍数；由 \(\gcd(p-1, n)=1\) 与周期内各剩余类均等分布为 \(\frac{n}{p}\) 次矛盾（\(p \nmid p^2-1\)），故必有 \(p \mid v\)。将 \(p \mid v\) 代入通项式得 \(x_k \equiv k u^{k-1} \pmod{p}\)，取 \(k = n+1\) 结合 \(x_{n+1} \equiv x_1 \equiv 1 \pmod{p}\) 得 \(u^n \equiv 1 \pmod{p}\)，再由 \(\gcd(p-1, n)=1\) 得 \(u \equiv 1 \pmod{p}\)。这一步干净地证明了“对所有 \(p \mid n\)，\(p \mid v\) 且 \(p \mid u-1\)”是必要条件。
- **步骤三：\(p \ge 5\) 与 \(3 \parallel n\) 时的 \(p\)-进估值与充分性证明**（*动机*：验证 \(p \ge 5\) 及 \(3 \parallel n\) 时必要条件亦充分。）：当 \(p \ge 5\) 且 \(p \mid v, p \mid u-1\) 时，若 \(p^\alpha \parallel k - \ell\)，由升幂定理（LTE）得 \(u^{k-\ell} \equiv 1 \pmod{p^{\alpha+1}}\)。对 \(i \ge 1\)，利用勒让德公式估得 \(v_p((2i+1)!) \le \lfloor \frac{2i+1}{p-1} \rfloor \le i-1\)，而分子中 \(v^i\) 贡献至少 \(i\) 个 \(p\) 因子，且 \(k(k-1)\cdots(k-2i) - \ell(\ell-1)\cdots(\ell-2i)\) 被 \(p^\alpha\) 整除，因此通项和 \(x_k - x_\ell\) 中所有 \(i \ge 1\) 项的 \(p\)-进赋值均 \(\ge \alpha + 1\)，唯有 \(i=0\) 项 \((k u^{k-1} - \ell u^{\ell-1})\) 恰被 \(p^\alpha\) 整除，从而 \(p^\alpha \parallel x_k - x_\ell\)。由此立即得出对 \(p^\beta \parallel n\)，\(x_0, \dots, x_{p^\beta - 1}\) 构成模 \(p^\beta\) 完系且周期为 \(p^\beta\)；若 \(3 \nmid n\) 或 \(3 \parallel n\)（此时模 \(3\) 下 \(x_k \equiv k u^{k-1} \equiv k\) 自动成完系），再由 CRT 即知充分性成立。
- **步骤四：精细讨论 \(9 \mid n\) 时的 \(v \bmod 9\) 情形并计数**（*动机*：精确攻克 \(p=3, \beta \ge 2\) 的临界情形并完成最终计数。）：当 \(3^\beta \parallel n\)（\(\beta \ge 2\)）时，因为 \(v_3((2i+1)!) \le \lfloor \frac{2i+1}{2} \rfloor = i\)，不能直接压过 \(v^i\) 的 \(3\)-进赋值，需要按 \(v \bmod 9\) 分类：
1. 若 \(9 \mid v\)，则 \(v^i\) 贡献 \(2i\) 个 \(3\) 因子，\(2i - i = i \ge 1\)，与 \(p \ge 5\) 同理，所有 \(i \ge 1\) 项赋值 \(\ge \alpha + 1\)，成立。
2. 若 \(v \equiv 6 \pmod{9}\)，则通项模 \(9\) 仅保留 \(i=0, 1\) 两项，得 \(x_k \equiv k u^{k-1} + k(k-1)(k-2) u^{k-3} \pmod{9}\)（因 \(v/6\) 使 \(\binom{k}{3} v \equiv k(k-1)(k-2) \pmod{9}\)），由此算得 \(x_{9i+1} \equiv x_{9i+4} \equiv 1 \pmod{9}\)，导致模 \(9\) 余 \(1\) 的项至少出现 \(\frac{2}{9}n\) 次，矛盾！
3. 若 \(v \equiv 3 \pmod{9}\)，进一步分析 \(i \ge 2\) 项：\(i=2,3\) 时 \(v_3((2i+1)!) < i\)，而 \(i \ge 4\) 时从乘积差展开中证明其至少被 \(3^{\alpha+1}\) 整除；故模 \(3^{\alpha+1}\) 下仅需计算 \(i=0, 1\) 两项之和，利用 \(k^2 + k\ell + \ell^2 \equiv 0 \pmod{3}\) 与 \(v \equiv 3 \pmod{9}\) 证得两项相加恰不被 \(3^{\alpha+1}\) 整除（即 \(3^\alpha \parallel x_k - x_\ell\)），从而成立。
综上，\(9 \nmid n\) 时 \(a\) 有 \(\varphi(n)\) 种，\(u, v\) 各有 \(\frac{n}{\prod_{p \mid n} p}\) 种；\(9 \mid n\) 时 \(v\) 须排除 \(v \equiv 6 \pmod{9}\)，选项乘以 \(\frac{2}{3}\)。

### 6. 易错点分析

- **遗漏 \(p=3, 9 \mid n\) 的特殊情形**：常见错法——忽视 \(p=3\) 且 \(9 \mid n\) 的特殊情形，直接套用 \(p \ge 5\) 的估值或结论，从而漏掉最终答案中的因子 \(\frac{2}{3}\)。；错因——当 \(p \ge 5\) 时有 \(v_p((2i+1)!) \le \lfloor \frac{2i+1}{p-1}\rfloor \le i-1\)（或 \(\Delta^p \in p^2\)），高次项严格高一阶；而当 \(p=3\) 时 \(v_3(3!) = 1 = i\)，导致 \(i=1\) 的二项式项与 \(i=0\) 的线性项处于同一 \(3\)-进阶，当 \(v \equiv 6 \pmod{9}\) 时两者恰好抵消，使数列产生周期 \(3^{e-1}\)。；避坑策略——在将模 \(p\) 性质推广到模 \(p^e\) 时，务必单独检验小素数 \(p=3\) 处 \((2i+1)!\) 的 \(3\)-进赋值或 \((1+\Delta)^3-1\) 中 \(\Delta^3\) 项的贡献；当 \(9 \mid n\) 时要分 \(v \equiv 0, 3, 6 \pmod{9}\) 三类讨论。
- **混淆必要性与充分性，或误将模 \(p\) 关系直接提升为模 \(n\)**：常见错法——误以为 \(b \equiv -2a \pmod{n}\)、\(c \equiv a \pmod{n}\) 才合法，或者只证明了模 \(p\) 的必要条件就默认对模 \(p^e\) 充分。；错因——线性递推在模 \(p^e\) 下只需特征根在模 \(p\) 意义下重合为 \(1\)，高阶项可以偏离 \(p\) 的倍数；反之，\(n=9\) 时 \((1,1,1)\)（即 \(v=3\)? 不，\(1+b+c=3 \implies v \equiv 6 \pmod{9}\)）反而失效，因此不能未经证明就凭直觉下结论。；避坑策略——在得出必要性后，必须对每个素数幂 \(p^\beta \parallel n\) 完整验证：任意周期为 \(p^\beta\) 的条件成立，且对 \(1 \le \alpha \le \beta - 1\) 有 \(p^\alpha \parallel x_k - x_\ell\)（等价于 \(p^\alpha \parallel k - \ell\)），再结合中国剩余定理合并构造出模 \(n\) 的排列。
- **未经论证进行归一化或错误平移数列值域**：常见错法——直接设 \(a=1, x_0=0, x_1=1\) 而未先证明 \(\gcd(a,n)=1\) 与 \(\gcd(x_1,n)=1\)，或擅自令 \(x_k \mapsto x_k + C\) 归约。；错因——条件 (i) 仅保证 \(\gcd(a,b,c,n)=1\)，并不直接给出 \(\gcd(a,n)=1\)；若 \(x_k\) 全部加上常数 \(C\)，递推式会多出 \((a+b+c)C\)，当 \(n \nmid a+b+c\) 时将破坏整除性。；避坑策略——做任何归一化（如 \(a=1\)、\(x_0=0\)、\(x_1=1\)）之前，先逐一证明 \(\gcd(a,n)=1\)、存在下标使 \(x_0=0\)（平移指标不改变循环条件）、以及 \(\gcd(x_1,n)=1\)；且若通过常系数齐次线性递推消去偏移，需注意 \(a+b+c\) 未必被 \(n\) 整除，不能随意给所有 \(x_k\) 加上同一常数。

**教学小结**：处理模合数 \(n\) 的线性递推与排列构造问题时，先借助归一化与变量代换（或移位算子）将局部特征多项式化为标准形，再通过中国剩余定理拆解到各素数幂 \(p^\beta \parallel n\) 上做 \(p\)-进赋值分析，并时刻警惕小素数（如 \(p=3\)）在高次幂下因阶乘估值紧绷而产生的退化分支。

---
