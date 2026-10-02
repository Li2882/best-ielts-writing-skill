⭐ **觉得有帮助，欢迎给项目点个 [Star](https://github.com/Li2882/best-ielts-writing-skill)！** · If this helps, please star the project.

# IELTS Writing Correction for Academic Task 1 & 2

## 雅思大小作文批改 · Band Score Review · The best IELTS writing review Codex Skill

**四项估分、原文证据、错误诊断、修改建议。**

**经过测验，比大多数现有的雅思批改 Skill 更好。**

这是一个面向 Codex 的 IELTS Academic Writing 批改 Skill。它保留作文原文，分别评估 Task Achievement / Task Response、Coherence and Cohesion、Lexical Resource、Grammatical Range and Accuracy，再用同任务、同分项锚点作文校准分数，输出能回到原文核对的反馈。

![IELTS Writing Correction Codex Skill](assets/cover.svg)

## 快速开始

1. 下载仓库，在 Codex 中打开**整个项目根目录**。
2. 使用 **GPT-6 Astra / High** 或更高推理档。
3. 在对话中输入：

```text
请使用 $ielts-writing-review-final 批改下面的 IELTS Academic 作文。
完整题目：……
Task 1 原图（如适用）：……
未经修改的作文原文：……
```

Task 1 要提供原图或完整、已核实的图表数据；Task 2 要提供完整题目。运行前可以执行：

```powershell
python scripts/check_ready.py
```

详细输入要求见[使用指南](docs/usage.md)，完整批改片段见[真实示例](examples/review.md)。

## 能做什么

| 能力 | 输出 |
| --- | --- |
| 四项 Band Score Review | TA/TR、CC、LR、GRA 的独立初评、锚点调整和最终模拟分 |
| Evidence-based correction | 引用原文，定位真实错误，区分错误、档位限制和可选润色 |
| Task 1 图表核验 | 核对时间、单位、对象、趋势、比较和数据事实 |
| Task 2 论证诊断 | 核对题目覆盖、立场、核心论点、why/how 展开和例证 |
| Anchor calibration | 使用同任务、同分项参考作文进行整数档和半分位置比较 |
| Revision advice | 按预期提分影响给出三个优先修改方向和最小必要改法 |
| 可追溯报告 | 列出实际读取的标准、提示词、锚点编号、缺项和版本 |

## 工作方式

```text
完整题目 / 原图 / 作文原文
              ↓
题目与图表事实核验
              ↓
TA/TR · CC · LR · GRA 四项独立初评
              ↓
同任务、同分项锚点比较与证据校准
              ↓
四项最终分 + 原文证据 + 修改建议
```

每项先保留初评证据，再决定分数；校准不能回写初评。LR 的成功词汇评分与问题诊断分开，问题卡用于解释和修改建议，不在最终分之后重复扣分。

## 我们做了多少工作

当前索引和研究资料包含：

| 项目 | 数量 / 状态 |
| --- | --- |
| 样本记录 | **562** 条 Task 1 / Task 2 记录 |
| 可作为参考的已核验样本 | **464** 条 `verified + reference` |
| 有独立分项标签的记录 | **396** 条 `label_scope=individual` |
| 初评提示词与路线 | **23** 个 prompt 记录，覆盖多个公开路线 |
| 锁定的评分输入 | **9** 个原始提示词 / 标准文件，逐项 SHA-256 锁定 |
| 研究与校准证据 | **1,093** 个随评分链路引用的公开文件 |
| 评估记录 | **22** 个阶段性 evaluation 记录 |
| 目标锚点格 | **32** 格：2 个任务 × 4 个分项 × 6/7/8/9 分 |
| 每格目标 | 至少 **10** 篇同任务、同分项参考作文 |
| 当前开发回归 | **28** 篇，大小作文各 14 篇 |
| 锚点比较记录 | **4,382** 次逐对比较 |
| 评分初评记录 | **112** 项分项初评与 **112** 项校准记录 |

### 锚点怎样筛选

一个样本进入参考库前，要同时检查：

1. 任务类型匹配：Task 1 与 Task 2 分开，四个分项也分开。
2. 原文可读：保留未经修改的作文文本；Task 1 还要有原图或可核实图表事实。
3. 标签可追溯：优先使用逐篇、逐分项的人工标签，不从总分反推小分。
4. 状态合格：索引中标记为 `verified` 且属于 `reference` split。
5. 来源可回查：保留来源 URL、题目组、原稿哈希、评语和证据路径。
6. 先去重再入格：相同原稿、转载版本和修订版本不重复投票。

因此，562 条是研究索引总量，464 条是当前可进入参考比较的已核验记录；实际评分还会继续按任务、分项、分数档和题目资料逐篇读取。

## 测试结果

当前发布版 `final-composite-1.4` 使用 `gpt-6-astra`、`high` 完成 28 篇开发回归：

| 范围 | 阶段 | N | 总分 MAE | 误差 ≤ 0.5 |
| --- | --- | ---: | ---: | ---: |
| 全部 | 初评 | 28 | 0.518 | 78.6% |
| 全部 | 锚点校准后 | 28 | **0.482** | **82.1%** |
| Task 1 | 锚点校准后 | 14 | 0.536 | 85.7% |
| Task 2 | 锚点校准后 | 14 | 0.429 | 78.6% |

早期公开路线筛选还记录了 quyen244 **0.857**、Gishguo **0.946** 等四项 MAE。它们属于路线形成过程中的独立记录；每个版本都保留自己的样本、指标和输入条件。完整的迭代过程见[研究过程与实测](docs/research.md)。

## 思路怎样一步步改变

| 阶段 | 做了什么 | 形成的决定 |
| --- | --- | --- |
| 公开路线筛选 | 在同一批公开作文上比较多套提示词的四项表现 | 为 TA/TR、CC、LR、GRA 分别保留候选初评路线 |
| 任务分路 | 把 Task 1 的图表完成度和 Task 2 的论证展开分开观察 | 不再用一套固定调整同时处理两个任务 |
| 证据卡 | 先记录原文、上下文、核验结果，再讨论分数 | 把事实错误、语言错误和可选润色分开 |
| LR 处理 | 比较成功词汇评分与问题诊断的关系 | 问题卡保留在反馈中，不做第二次独立扣分 |
| GRA 处理 | 保留 independent V4 初评，再加入同任务锚点 | 语法分数先锁定，再做有证据的定位调整 |
| final-composite-1.4 | 四项独立初评 + 32 格整数锚点框架 + 半分比较 | 形成当前发布版批改流程 |
| 28 篇回归 | 锁定输入、初评和锚点结果后计算指标 | 记录当前版本的 MAE、RMSE、Bias 和一致率 |

这不是一次性拼接提示词，而是从路线筛选、样本入库、证据核验、分项处理到锚点校准逐步形成的版本记录。详细表格、来源和数值文件在[研究目录](docs/research.md)和[`research-data/`](research-data/)中。

## 项目结构

```text
.
├── .agents/skills/ielts-writing-review-final/
│   ├── SKILL.md                  # Codex 的项目级 Skill 入口
│   └── references/               # 评分核心、校准规则、哈希锁定
├── library/
│   ├── index.json                # 样本、题目、来源和标签索引
│   ├── prompts/                 # 初评提示词与路线资料
│   ├── task1/                   # Task 1 参考样本
│   ├── task2/                   # Task 2 参考样本
│   └── standards/               # IELTS 分项描述符
├── research-data/                # 公开数值、来源和复核数据
├── scripts/
│   ├── check_ready.py            # 检查评分依赖和哈希
│   └── verify_public_data.py     # 只读重算公开指标
├── docs/research.md              # 版本演变和研究过程
├── docs/usage.md                 # 输入、模型和运行说明
└── examples/review.md            # 真实批改片段
```

## 下一步路线

- [x] 发布 Codex 项目级 Skill 和可直接运行的评分依赖
- [x] 建立 Task 1 / Task 2 分路和四项独立初评
- [x] 建立同任务、同分项锚点比较和可追溯反馈
- [x] 完成 28 篇当前版本开发回归
- [ ] 继续补齐 32 个锚点格的同任务、同分项样本
- [ ] 增加冻结版本后的新样本回归包，并分别记录 Task 1、Task 2 和四项指标
- [ ] 增加更多可复核的中文、英文批改示例和结构化输出示例

## 资料、来源与复核

公开来源、提示词哈希、样本索引和数值导出记录在 [`research-data/`](research-data/) 中；每条样本保留来源 URL 和版本信息。运行：

```powershell
python scripts/check_ready.py
python scripts/verify_public_data.py
```

前一个命令检查 Codex 评分链路是否齐全，后一个命令只读重算公开数据，不调用模型。资料来源和研究过程见[研究文档](docs/research.md)。

## English

IELTS Academic Writing Correction and Band Score Review for Task 1 and Task 2. This Codex Skill provides four-criterion estimates, quoted evidence, task-specific anchor calibration, error diagnosis, and prioritized revision advice.

The project contains 562 indexed sample records, 464 verified reference records, 23 prompt records, a 32-cell anchor plan, and a 28-essay development regression. Open the whole repository in Codex and invoke `$ielts-writing-review-final`. Recommended minimum: **GPT-6 Astra / High**.

Read the [usage guide](docs/usage.md), [real review](examples/review.md), and [research record](docs/research.md) before adapting the workflow. Results are unofficial simulated estimates; changing the model, reasoning level, reference library, or scoring route creates a new test condition.

## 版本与支持

当前公开版本见 [CHANGELOG.md](CHANGELOG.md) 和 [v1.0.0 Release](https://github.com/Li2882/best-ielts-writing-skill/releases/tag/v1.0.0)。欢迎通过 GitHub Issues 提交可复核的错误、输入问题或改进建议。
