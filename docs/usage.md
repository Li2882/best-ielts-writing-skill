# 使用说明 / Usage

## 1. 下载并打开

在 GitHub 选择 **Code → Download ZIP**，解压后在 Codex 中打开整个项目目录。不要只复制 `SKILL.md`：它依赖相邻规则文件、评分资料和本地索引。

本项目沿用 `.agents/skills/ielts-writing-review-final/` 的项目级布局。若 Skill 未出现在列表中，可以重新打开项目，或直接要求读取根目录 `AGENTS.md` 和该 `SKILL.md`。

配置说明参考 [OpenAI 官方 Skills 文档](https://learn.chatgpt.com/docs/build-skills)。

## 2. 模型与费用

- 本项目推荐最低配置：**GPT-6 Astra，推理档 High**。本次28篇测试请求配置为 `gpt-6-astra`、`high`。
- 可以使用同一模型更高的推理档，但没有证据保证档位升高会带来相同或更好的雅思评分结果；改变配置后应重新测试。
- 其他模型、较低推理档以及不同参考库，不继承本项目的测试成绩。
- Skill 本身不是模型服务。需要自行取得可用模型账号；订阅或 API 使用费用按服务提供方计费。
- 完整参考比较可能耗时较长，不承诺秒级批改。

模型名称与推理档依据 [GPT-6 Astra 官方模型页](https://developers.openai.com/api/docs/models/gpt-6-astra)。最低推荐配置是本项目维护者的选择，不是官方 IELTS 或 OpenAI 认证门槛。

## 3. 资料准备：公开流程与本地参考库分开

本仓库发布评分流程、研究数据、来源清单及公开示例，**不重发剑桥整本书、第三方完整作文和教师批改库**。这些材料公开可见，不代表本项目取得了重新分发授权。

完整运行需要你在本地准备有权使用的资料：

1. IELTS 官方评分标准和锁定的原初评提示词。文件路径与哈希见 Skill 的 `references/baseline-lock.json`；来源见 `research-data/dependencies.json`。
2. `library/index.json`：本地资料索引。
3. 同任务、有人类分项评分的独立参考原稿、完整题目和评语；Task 1 还需原图或已核实图表事实。结构见 Skill 的 `references/library-format.md`。
4. 6、7、8、9 分各任务各分项的参考材料。缺项须明示，不能伪造已完成校准。

如果你已经拥有本项目的完整、合法本地研究副本，可运行：

```powershell
python scripts/setup_local_materials.py --from "你的完整研究项目路径"
python scripts/check_ready.py
```

导入器只在本地复制评分所需材料，不上传、不调用模型、不覆盖已有文件。`library/` 被 `.gitignore` 排除。

如果没有完整本地资料，应先根据来源清单和格式要求建立参考库。**仅下载公开仓库并不等于取得经过测试的全部依赖**；缺失初评必需文件时应停止评分并列出缺项。参考锚点不足时，按原规则保留独立初评并注明校准范围，不能宣称复现了 README 的性能。

## 4. 提交作文

```text
请使用 $ielts-writing-review-final。
任务：IELTS Academic Task 2
完整题目：……
未经修改的作文原文：……
请用中文解释，引用英文原文，给出四项估分和三个优先改进建议。
```

Task 1 还应提供清晰原图，或完整且独立核实的图表数据。给出剑桥册数、Academic、Test、Task 编号可以帮助定位，但不能从作文反推图表。

评分会区分初评、锚点调整和最终结果；中文解释配英文证据，通常不自动重写全文。不要提交不希望模型服务处理的个人信息。

完整批改末尾可能出现一行自愿 GitHub Star 提示，同一对话最多一次。它不影响评分、功能或费用；可以要求“不显示支持提示”。Skill 无法保证所有 AI 都会遵循这条展示规则，也不会替你点赞。

## English quick guide

Download and open the whole project in Codex. Use GPT-6 Astra with High reasoning as this project's recommended minimum. Supply the complete task, unedited essay, and the original chart or independently verified chart facts for Task 1.

The public repository contains the workflow and research records, **not the complete third-party corpus**. Prepare licensed local dependencies using the manifest, or import your existing complete research workspace with the scripts above. Missing mandatory prompts must be resolved before scoring. Incomplete anchors must be disclosed; another model or corpus does not inherit the reported evaluation results.
