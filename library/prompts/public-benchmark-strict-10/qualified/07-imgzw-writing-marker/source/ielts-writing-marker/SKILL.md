---
name: ielts-writing-marker
description: Grade and coach IELTS Academic or General Training Writing Task 1 and Task 2 using the official IELTS Writing criteria and public band descriptors. Use when a user asks to 批改、评分、估分、诊断、润色或提升雅思作文, compare a response with a target band, explain Task Achievement/Task Response, Coherence and Cohesion, Lexical Resource, or Grammatical Range and Accuracy, or review a revised IELTS essay.
---

# IELTS Writing Marker

Read [references/official-rubric.md](references/official-rubric.md) before scoring.

## Required input

Identify:

- test: Academic or General Training;
- task: Task 1 or Task 2;
- complete question, including chart/table/process/map or all letter bullet points;
- candidate response;
- optional target band.

Infer test/task only when the prompt makes it unambiguous. If the question or visual data is missing, still assess CC, LR and GRA, but label TA/TR and the overall estimate **provisional**. Never invent missing chart data or task instructions.

## Workflow

1. Separate the question from the response. Exclude copied task wording from the response word count when identifiable.
2. Count English whitespace-delimited tokens as an approximate word count. Note the Task 1 minimum of 150 words or Task 2 minimum of 250 words. Do not apply an invented fixed point deduction; judge the resulting lack of coverage or evidence through the descriptors. A response of 20 words or fewer is Band 1 under the public descriptors.
3. Check task fulfilment before language quality:
   - Academic Task 1: appropriate format, overview, key-feature selection, comparisons, accurate supporting data;
   - General Training Task 1: clear purpose, all bullet points, suitable tone, relevant development;
   - Task 2: address every part, maintain a clear position, develop relevant main ideas with support.
4. Score TA/TR, CC, LR and GRA independently in whole bands. Start with the closest anchor, then check the bands immediately above and below. Award a band only when the response sufficiently fits its positive features; let explicit negative/limiting features cap the score.
5. Cite brief evidence from the candidate response for every criterion. Distinguish recurring patterns from isolated slips. Do not reward memorised-looking phrases, rare words, or sentence complexity by themselves.
6. Calculate the task estimate as the arithmetic mean of the four criteria and report the raw mean plus a practice band rounded to the nearest 0.5. If both tasks are supplied, calculate `(Task 1 + 2 × Task 2) / 3` and label it an estimated Writing band.
7. Select the three changes most likely to raise the band. Prefer root causes over exhaustive proofreading.
8. Correct representative sentences while preserving the writer's meaning and level. Do not rewrite the entire essay unless requested.

## Output

Respond in the user's language; keep essay corrections in English.

### 1. 结论

- 类型、题型、约词数
- 估分：`X.X` and confidence `高/中/低`
- one-sentence diagnosis
- state `练习估分，并非 IELTS 官方成绩`

### 2. 四项评分

| 评分项 | 分数 | 作文证据 | 对照标准与主要限制 |
|---|---:|---|---|
| TA/TR | | | |
| CC | | | |
| LR | | | |
| GRA | | | |

For each row, explain both why it reaches that band and why it does not yet reach the next band.

### 3. 优先修改

Give exactly three ranked actions. Make each specific enough to apply to the current response.

### 4. 代表性精改

Use up to eight high-value examples:

`原句 → 修改 → 原因（TA/TR、CC、LR 或 GRA）`

Do not list every typo when a repeated error pattern explains them.

### 5. 下一步练习

Give one short, measurable exercise tied to the main score ceiling. If a target band was supplied, state the smallest observable changes needed to reach it.

## Calibration rules

- Keep criterion scores independent; strong grammar does not repair an incomplete response.
- Treat relevance, clarity and accuracy as more important than ornate vocabulary.
- For CC, evaluate progression, paragraph logic, referencing and cohesion, not just linking-word count.
- For LR, evaluate range, precision, collocation, register, spelling and word formation.
- For GRA, evaluate structural range, control, punctuation and communication impact; count repeated manifestations of one root error as a pattern.
- Use `.5` only for the reported average, not for individual criterion judgements.
- When evidence sits between bands, choose the lower band and explain what observable feature would justify the higher one.
- Lower confidence when handwriting/OCR is unclear, the prompt is incomplete, the response is very short, or chart data cannot be verified.
