# 严格门槛公开雅思评分提示词候选集

检索与核验日期：2026-09-23

本目录保存两类公开来源：

- `qualified/`：10 个来自不同来源的正式候选。每组均能取得完整评分指令或完整 skill 包，分别覆盖 TR/TA、CC、LR、GRA，明确区分 Band 6、7、8、9，并要求从作文证据映射到分数档位。
- `controls/`：3 个热度较高、但不满足上述结构门槛的对照组。它们不占 10 个正式名额，也不参与“最佳完整提示词”资格排名。

这里的“合格”只表示**有资格进入统一测试**，不表示已经证明准确。stars、forks、作者背景和公开宣传也不等于评分准确率。准确性必须用同一批隐藏标签作文实测。

## 正式候选

| 编号 | 来源 | 公开热度快照 | 覆盖范围 | 通过硬门槛的关键点 |
|---:|---|---:|---|---|
| 1 | [AaronL725 IELTS Writing Review Skills](https://github.com/AaronL725/ielts-writing-review-skills) | 34 stars / 3 forks | Academic Task 1、Task 2 | 两项任务各有完整评分流程和四项 Band 6–9 描述，并要求先评原稿、按相邻档给半分。 |
| 2 | [Gishguo IELTS Examiner Claude Skill](https://github.com/Gishguo/your_ielts_writing_examiner_claude_skill) | 2 / 0 | Task 1、Task 2 | skill 要求逐项评分、引用具体证据；配套文件含两项任务完整分档。 |
| 3 | [unrealinux IELTS Writing Coach](https://github.com/unrealinux/ielts-writing-coach) | 0 / 0 | Academic Task 1、Task 2 | 中文 Band 5–9 四项门槛；每项执行“门槛→原文证据→上一档差距”。 |
| 4 | [quyen244 IELTS AI Evaluator](https://github.com/quyen244/IELTS-AI-Evaluator) | 4 / 0 | Academic Task 1、Task 2 | 代码把四项量表注入独立提示词，要求先写理由、比较上下档、再给分并逐字引用。 |
| 5 | [ryangwn VTM IELTS Writing Assessment](https://github.com/ryangwn/vtm-ietls-writing-assessment) | 0 / 0 | Task 1、Task 2 | 实际运行提示词含四项 Band 6–9 描述及分项分析流程。 |
| 6 | [AustinWang668 IELTS Writing Scorer](https://github.com/AustinWang668/ielts-writing-scorer) | 0 / 0 | Academic/General Task 1、Task 2 | 明确比较相邻整数档、选最高稳定达标档、应用限制项并引用原文；任务项和通用三项均有 6–9 锚点。 |
| 7 | [imgzw IELTS Writing Marker](https://github.com/imgzw/ielts-writing-marker) | 0 / 0 | Academic/General Task 1、Task 2 | 评分 skill 配完整四项量表，要求以原文证据解释为何达到当前档、为何未达上一档。 |
| 8 | [hippone IELTS Writing Diagnostic](https://github.com/hippone/ielts-writing-diagnostic) | 0 / 0 | Academic Task 1、Task 2 | 两项任务分别给出四项 Band 6–9，主要扣分点必须有 3–15 词逐字证据。 |
| 9 | [dungnotnull Language Cert Prep Scorer](https://github.com/dungnotnull/language-cert-prep-scorer-agent-skill) | 5 / 0 | IELTS Writing | 完整四项 Band 6–9 表；每项必须匹配描述行、引用原文并给理由。 |
| 10 | [Mustafa IELTS Writing Evaluator](https://github.com/MustafaAhmedMahfoodhBinOthman/IELTS_Writing_Evaluator) | 1 / 1 | Academic/General Task 1、Task 2 | TR/TA、CC、LR、GRA 分开评分，每项含 Band 6–9 描述和证据→分数步骤。目录只保存原文件中对应提示词赋值片段，未复制无关配置或凭据。 |

## 高热度对照组（不计入 10 个正式名额）

| 来源 | 公开热度快照 | 未通过原因 |
|---|---:|---|
| [OpenIELTS-AI](https://github.com/Shpaldik/OpenIELTS-AI) | 99 stars / 88 forks | 有四项、证据引用和结构化输出，但公开评分配置没有逐项列出 Band 6、7、8、9 的差异。 |
| [ieltsGPT](https://github.com/araloak/ieltsGPT) | 32 / 5 | 四项提示词分开，但只写 Band 5–8，缺 Band 9；若补写 Band 9 就违反“不得补全原文”。 |
| [AIELTS-WRITING](https://github.com/maruf009sultan/AIELTS-WRITING) | 22 / 0 | 输出四项分数，但公开完整提示词没有四项 6–9 分档，也没有相邻档证据判定过程。 |

## 作者背景记录原则

作者背景只记录仓库或公开主页能够核实的内容。除 quyen244 的 README 明确标出学生项目 Developer 外，其余来源主要是公开软件、skill 或产品项目；没有公开资质时统一记录为“未发现可核实的 IELTS 教师/考官资质声明”，不会把提示词中的角色扮演语句当作作者资质。

## 文件与完整性

- `manifest.json`：机器可读清单，含来源、热度、作者背景、范围、文件路径、SHA-256 和门槛审计结果。
- `qualified/<id>/source/`：正式候选的原始公开文件快照。
- `controls/<id>/source/`：高热度对照组的原始公开文件快照。
- 同一仓库的 Task 1 与 Task 2 合计为一组，没有拆分凑数。
- 正式候选机械审计结果：10/10 通过；高热度对照组：0/3 通过。

## 测试边界

本轮完成的是候选检索和资格筛选，尚未产生准确率排名。后续测试必须使用相同作文、相同模型与采样设置，在揭示人工小分前保存全部输出；正式候选与高热度对照组分别报告四项 MAE、偏差和重复运行波动。
