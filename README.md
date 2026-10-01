⭐ **觉得好用的话，点个 [Star](https://github.com/Li2882/best-ielts-writing-skill) 支持一下！** · If this helps, please give it a star!

# IELTS Writing Coach

**最好的雅思批改 Skill · The best IELTS writing review skill**

比大多数现有的雅思批改 Skill 更好。 · Better than most existing IELTS writing review skills.

![IELTS Writing Coach](assets/cover.svg)

## 中文

批改 IELTS Academic 大小作文：**四项估分、原文证据、错误诊断、修改建议**。区分真实错误与可选润色，让你知道分数从哪里来、下一稿怎么改。[真实示例](examples/review.md)

**工作方式：**先由大模型分别评估四项，再用同任务锚点作文进行证据校准，最后输出可追溯的分数和修改建议。

**28 篇开发测试：总分 MAE 0.482；82.1% 的作文误差不超过 0.5 分。**

外部 Skill 历史实测：quyen244 **0.857**、Gishguo **0.946**（7 篇、四项 MAE）。与本版测试集及指标不同，不作直接胜负结论。[完整对比与研究过程](docs/research.md)

**使用：**下载本项目，在 Codex 打开文件夹，选择 **GPT-6 Astra / High 或更高推理档**，发送：

```text
请使用 $ielts-writing-review-final 批改下面的作文。
题目／Task 1 原图：……
作文原文：……
```

本项目推荐最低配置为 GPT-6 Astra / High；换模型需重新验证。评分库及被引用的校准证据已随仓库提供；模拟估分，非官方成绩，模型费用另计。

## English

IELTS Academic Task 1 & 2 feedback: **four-criterion band estimates, quoted evidence, error diagnosis, and actionable revisions**. [See a real review](examples/review.md).

**How it works:** the model scores the four criteria independently first, then calibrates each score against same-task anchor essays before producing traceable bands and revision advice.

**28-essay development evaluation: overall-band MAE 0.482; 82.1% within ±0.5 band.** Earlier external-prompt results: quyen244 **0.857**, Gishguo **0.946** (7 essays, criterion-level MAE). Different datasets and metrics: not a head-to-head ranking. [Research & comparisons](docs/research.md).

Download this project, open it in Codex, and invoke `$ielts-writing-review-final` with the question, original essay, and Task 1 chart. Recommended minimum: **GPT-6 Astra / High**. The scoring library and referenced calibration evidence are included. Unofficial estimates; model costs apply.
