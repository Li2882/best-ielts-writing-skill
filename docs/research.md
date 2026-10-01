# 研究过程与实测 / Research and evaluation

本页记录 `final-composite-1.4` 是怎样从公开路线筛选，逐步形成现在的批改流程。更新时间：2026年10月2日（Asia/Shanghai）。

## 1. 当前版本

当前流程包含四项独立初评、原文证据核验、同任务同分项锚点校准和可追溯反馈。评分库、原始提示词和被引用的校准证据已随仓库提供；个人提交、凭证和无关私有研究材料不随仓库发布。

2026年10月1日完成 28 篇开发回归，配置为 `gpt-6-astra`、`high`：总分 MAE **0.482**，误差不超过 0.5 分的比例 **82.1%**。这组结果对应当前版本、当前配置和当前测试记录。

## 2. 路线如何一步步形成

### 2026年9月23日：公开提示词路线筛选

先把公开项目放到同一批 7 篇作文上，记录不同路线在 TA/TR、CC、LR、GRA 四项上的表现。指标是四项 MAE，主要标签来自公开教师练习评分。

| 公开项目 | 篇数 | 四项 MAE |
| --- | ---: | ---: |
| quyen244 IELTS AI Evaluator | 7 | 0.857 |
| Mustafa IELTS Writing Evaluator | 7 | 0.911 |
| Gishguo IELTS Examiner Claude Skill | 7 | 0.946 |
| ryangwn VTM IELTS Writing Assessment | 7 | 0.982 |
| hippone IELTS Writing Diagnostic | 7 | 0.982 |
| dungnotnull Language Cert Prep Scorer | 7 | 0.982 |
| unrealinux IELTS Writing Coach | 7 | 1.000 |
| imgzw IELTS Writing Marker | 7 | 1.054 |
| AustinWang668 IELTS Writing Scorer | 7 | 1.107 |
| AaronL725 IELTS Writing Review Skills | 7 | 1.161 |

另有 3 个只支持 Task 2 的路线，4 篇四项 MAE 分别为：OpenIELTS-AI **1.031**、ieltsGPT **1.156**、AIELTS-WRITING **1.219**。此前 3 篇 Task 2 的米勒公开提示词记录为 **1.042**。这些数据保留为路线选择的起点。

### 2026年9月24日：从一条路线转为任务分路

共享样本让 Task 1 和 Task 2 的处理方式分开比较。Task 1 继续使用 quyen 的独立 TA 路线；Task 2 的 TR 保留能更好覆盖题目展开的路线。由此，流程不再用一套固定补偿同时处理两个任务。

### 2026年9月27日：把 LR 的“成功词汇”和问题诊断分开

LR 先用 V4 的成功词汇阶段形成 `provisional_score`，再把搭配、拼写、词形等问题放进证据卡和反馈。后续测试保留成功词汇锚点比较，不把问题卡重新变成第二次独立扣分。

### 2026年9月30日：形成 final-composite-1.4

GRA 保留 independent V4 初评；四项都加入同任务、同分项的整数锚点，并在相邻整数之间做半分定位。事实、句法和指代核验在初评锁定前完成，校准阶段只处理有证据的分数位置变化。

### 2026年10月1日：28 篇开发回归

大小作文各 14 篇，人工单篇总分覆盖 6 至 9 分，每个半分档每种任务 2 篇。先锁定初评，再锁定锚点比较，最后计算总分指标。

## 3. 方法的演变

1. **从公开路线到分项路线。** 先观察不同公开提示词的分项特点，再为 TA/TR、CC、LR、GRA 分别保留合适的初评来源。
2. **从总分印象到证据卡。** 每项先记录原文证据，再给分；题目、图表、句法和指代核验不直接生成扣分。
3. **从固定调整到同任务锚点。** 锚点按任务和分项读取，整数档逐格比较，半分使用相邻整数档，不把四项混票。
4. **从一次反馈到可追溯结果。** 输出保留初评、锚点调整、最终分、引用、缺项和版本信息。

## 4. 版本结果记录

| 测试阶段 | 样本 | 记录到的结果 | 对当前流程的影响 |
| --- | ---: | --- | --- |
| 公开提示词筛选 | 7 篇 | quyen244 0.857；Gishguo 0.946；其他路线见上表 | 建立初评路线候选 |
| Task 1 路线比较 | 4 篇 | 独立 TA 0.25；V3 TA 0.50 | 当前保留独立 TA 初评 |
| Task 2 路线比较 | 4 篇 | 独立 TR 1.125；V3 TR 0.50 | 当前保留更适合 TR 的路线 |
| LR 后置处理比较 | 8 篇 | 不做第二次独立扣分时 MAE 0.375 | 当前只保留成功词汇分数与锚点调整 |
| GRA 面板比较 | 8 篇 | independent V4 0.875；六锚点面板 0.938 | 当前保留 independent V4 初评并使用新锚点 |
| final-composite-1.4 回归 | 28 篇 | 初评总分 MAE 0.518；校准后 0.482；误差≤0.5 从 78.6% 到 82.1% | 形成当前发布版流程 |

这些数字属于各自测试阶段；完整输入、标签和导出记录见 [`research-data/`](../research-data/)。

## 5. 当前 28 篇结果

| 范围 | 阶段 | N | 总分 MAE | RMSE | Bias | 完全一致 | 误差≤0.5 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 全部 | 初评 | 28 | 0.518 | 0.634 | -0.054 | 21.4% | 78.6% |
| 全部 | 校准 | 28 | 0.482 | 0.605 | -0.089 | 25.0% | 82.1% |
| Task 1 | 校准 | 14 | 0.536 | 0.582 | -0.036 | 7.1% | 85.7% |
| Task 2 | 校准 | 14 | 0.429 | 0.627 | -0.143 | 42.9% | 78.6% |

本批从初评到校准的变化，是当前版本内部流程的前后记录。分项人工标签覆盖、锚点配额和每篇预测均保存在[当前测试数据](../research-data/current-evaluation.json)。

## 6. 使用边界

- Task 1 需要原图或完整、已核实的数据；Task 2 需要完整题目。
- 当前回归使用 `gpt-6-astra`、`high`；更换模型、推理档或参考库后应重新测试。
- 有人工分项标签的样本按分项报告；不能从单篇总分反推四项标签。
- 公开结果是模拟估分研究，不是官方 IELTS 成绩。
- 后续版本应在冻结流程后继续记录样本、配置、分项指标和输入版本。

## 7. 复核数据

运行 `python scripts/verify_public_data.py` 可以只读重算公开指标，不调用模型，也不重新批改作文。`research-data/provenance.json` 记录导出源文件的 SHA-256 和公开文件范围。

## English summary

`final-composite-1.4` evolved from public prompt screening into a four-criterion workflow with task-specific routes, locked independent assessments, evidence checks, and same-task anchor calibration. The 28-essay development regression with `gpt-6-astra` / `high` recorded overall-band MAE 0.482 and 82.1% within ±0.5. The research page presents the sequence of tests, decisions, and current results so the workflow can be followed and extended.
