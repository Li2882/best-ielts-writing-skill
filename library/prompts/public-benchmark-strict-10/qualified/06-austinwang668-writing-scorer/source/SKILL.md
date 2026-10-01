---
name: ielts-writing-scorer
description: Strictly estimate, diagnose, annotate, coach, and optionally rewrite IELTS Academic or General Training Writing Task 1 and Task 2 using the official public band criteria. Produces four-criterion scorecards, exact-match inline annotations, word-count checks, weighted two-task estimates, personalised practice, target-band examples, and validated structured JSON. Use when Codex is asked to score, grade, mark, assess, review, annotate, improve, practise, rewrite, or return machine-readable JSON for an IELTS writing response; estimate a band; explain why an essay received a band; check a chart report, letter, or Task 2 essay; calculate a combined Writing score; mark errors in the original; build a training plan; or create a better example after scoring. Trigger for requests such as “雅思作文打分”, “在原文中批注错误”, “给我针对性训练”, “评分后重写一篇例文”, “输出结构化评分 JSON”, “评 Academic Task 1”, and “score and annotate my IELTS essay”.
---

# IELTS Writing Scorer

## Apply the core contract

- Treat every score as an evidence-based, non-official estimate, never as a certified examiner result.
- Score the submitted response as written. Do not silently repair grammar, spelling, wording, or an unclear transcription before scoring.
- Default to strict scoring and Chinese explanations. Follow the user's requested feedback language when specified; preserve English source excerpts and corrections.
- Keep scoring separate from rewriting. Finish and preserve the original response's score before generating any improved version; never replace or retroactively raise the original score.
- Base annotations and training only on observable features of the submitted response. Do not invent errors or generic exercises merely to fill a template.
- After a complete score report, offer a target-band example rewrite unless the user already requested it or explicitly asked for scoring only.
- Do not claim plagiarism, memorisation, or copied language without external evidence. Describe suspicious formulaic language only as a language-quality observation.

## Follow the scoring workflow

### 1. Classify the task and verify the evidence

Identify the test and task as one of:

- `academic-1`: Academic Task 1 chart, table, map, plan, process, or diagram
- `general-1`: General Training Task 1 letter
- `task-2`: Academic or General Training Task 2 essay
- `full-writing`: both tasks from the same test

Require these materials before assigning Task Achievement/Response or an overall task band:

| Task | Required evidence |
| --- | --- |
| Academic Task 1 | Full instructions, readable visual/source data, and candidate response |
| General Training Task 1 | Full situation, every bullet point, and candidate response |
| Task 2 | Full prompt, every question, and candidate response |
| Full Writing | Complete evidence and response for both tasks |

Infer the task type only when the evidence makes it unambiguous. Otherwise ask one concise question. If required evidence is missing, mark Task Achievement/Response and the overall task band as `N/A`; provide only a provisional language-and-organisation diagnosis for Coherence and Cohesion, Lexical Resource, and Grammatical Range and Accuracy.

For a handwritten or photographed response, transcribe faithfully. Mark unreadable spans as `[unclear]`, report that uncertainty, and widen the confidence range. Do not count or correct an unreadable word as though it were certain.

### 2. Load the correct scoring references

- Read [references/scoring-guide.md](references/scoring-guide.md) for the shared band anchors, limiting rules, half-band policy, and calculation rules.
- Read the matching section of [references/task-checklists.md](references/task-checklists.md) before scoring Task Achievement or Task Response.
- Read [references/coaching-guide.md](references/coaching-guide.md) before producing inline annotations or personalised training.
- Read [references/rewrite-guide.md](references/rewrite-guide.md) only after the user requests or accepts a rewrite.
- Use the official links recorded in the references as the source of truth if a user asks to verify whether the public criteria have changed.

### 3. Measure only deterministic features mechanically

Resolve the absolute directory containing this `SKILL.md` as `SKILL_DIR` before invoking any bundled file. Never assume the current working directory is the skill directory.

Run `"<SKILL_DIR>/scripts/text_stats.py"` on the unedited candidate response. When the response exists only in the conversation, write its exact UTF-8 text to a temporary file without shell interpolation, pass that absolute path with `--input`, and remove the temporary file after validation. Preserve every character, including final newlines.

```bash
python3 "<SKILL_DIR>/scripts/text_stats.py" --task task-2 --input "/absolute/path/to/response.txt" --pretty
```

Use `--input /path/to/response.txt` when a text file already exists. Report the result as a machine-estimated word count because examiner counting conventions may differ at the margins. Do not convert sentence length, paragraph count, or any other mechanical statistic directly into an IELTS band.

### 4. Score each criterion independently

For each criterion:

1. Compare the whole response with the nearest adjacent integer-band anchors.
2. Select the highest integer band whose positive features are consistently demonstrated.
3. Apply any published limiting feature before considering a higher band.
4. Use a `.5` only when the evidence genuinely sits between two adjacent anchors; do not award half bands merely to make the estimate look precise.
5. Cite short, exact excerpts from the candidate response as evidence. Verify every quoted excerpt against the original text.

Do not average hidden sub-scores inside a criterion. Distinguish frequency from impact: an occasional slip that does not impede meaning differs from a systematic error, while one serious Task Achievement/Response omission may cap that criterion.

### 5. Calculate task and full-Writing estimates

After assigning all four rateable criterion bands, run:

```bash
python3 "<SKILL_DIR>/scripts/band_score.py" task 6.5 6.0 6.0 6.5 --pretty
```

Pass the scores in this order: Task Achievement/Response, Coherence and Cohesion, Lexical Resource, Grammatical Range and Accuracy.

For a complete pair of tasks, calculate the Writing estimate only after both task bands exist:

```bash
python3 "<SKILL_DIR>/scripts/band_score.py" writing --task1 6.0 --task2 6.5 --pretty
```

Label a single submission as a **task estimate**, never as the candidate's complete IELTS Writing score. Do not calculate an overall band from only three criteria.

### 6. Build and validate the structured result

Create a result conforming to `schemas/score-result.schema.json` before rendering feedback. Use `single-task` for one response and `full-writing` for a complete pair.

- Compute `response_sha256` from the exact UTF-8 response bytes used for scoring.
- Store every quoted criterion example and annotation as an exact `quote` plus its one-based `occurrence` in the response.
- Represent a missing Task Achievement/Response judgment with `score: null`; set `task_band` and `confidence_range` to `null` when the task is not fully rateable.
- Keep numeric bands on whole- or half-band steps. Record calculated raw and rounded values separately.
- Use `training: null` when the user requests score-only output.

Save the result to a temporary JSON file and validate it before presenting any score:

```bash
python3 "<SKILL_DIR>/scripts/validate_score_json.py" \
  --result "/absolute/path/to/result.json" \
  --response "/absolute/path/to/response.txt" \
  --pretty
```

For `full-writing`, pass `--task1-response` and `--task2-response`. If validation fails, correct the result instead of returning invalid JSON or unverifiable evidence. Render the normal human-readable report from the validated result. Include the complete JSON when the user asks for JSON, machine-readable output, batch processing, integration, or an audit artifact; otherwise keep it as an internal consistency representation.

### 7. Produce evidence-linked feedback

Use this default structure:

```markdown
## IELTS 写作估分（非官方）

- 类型：Academic Task 1 / General Training Task 1 / Task 2
- 机器估算字数：...
- 单篇预估分：...（合理浮动范围：...）
- 完整性说明：...

| 评分项 | 分数 | 档位判断 | 原文证据与理由 |
| --- | ---: | --- | --- |
| Task Achievement/Response | ... | ... | ... |
| Coherence and Cohesion | ... | ... | ... |
| Lexical Resource | ... | ... | ... |
| Grammatical Range and Accuracy | ... | ... | ... |

### 最影响提分的三个问题

1. ...
2. ...
3. ...

### 原文行内批注

> Copy selected original sentences exactly and insert markers such as `[G1]`, `[L1]`, `[CC1]`, or `[TR1]` immediately after the affected span.

| 标记 | 类型 | 原文（精确摘录） | 建议修改 | 原因 |
| --- | --- | --- | --- | --- |

### 个性化提分训练

- 下一篇的三个可检查目标：...
- 两个针对性微练习：...
- 提交前自查：...
```

Give a normal confidence range of approximately ±0.5 band. Widen it when the source is unclear or the response is unusually borderline, and explain why. Return fewer annotations when fewer genuine problems exist; never pad the table with invented errors. By default, annotate three to eight high-impact spans in selected sentences rather than duplicating the entire essay. Annotate the complete response only when the user explicitly requests full markup.

Derive the practice section from the three highest-impact problems and the next plausible band boundary. Keep it short enough to complete in one study session. When the user says “score only” or otherwise declines coaching, omit annotations, training, and rewriting while retaining concise scoring evidence.

### 8. Offer the example rewrite

After a complete score report, ask one concise follow-up question:

> 需要我基于原题和你的核心观点，按目标分数重写一篇完整例文，并说明改写思路与可复用方法吗？你可以指定目标分数；未指定时，我会按当前单篇预估分提高 1.0 分（最高 9.0）处理。

For a full-Writing submission, ask whether to rewrite Task 1, Task 2, or both. Do not repeat the question when the user already requested a rewrite in the same message; continue directly after scoring. Do not ask when the user explicitly requested scoring only or declined rewriting.

If required prompt or source evidence is missing, request that material instead of offering or producing a model response.

### 9. Rewrite only after consent or an explicit request

When the user accepts, treat a bare “需要”, “可以”, “yes”, or equivalent as consent. If no target is supplied, set the target to the original task estimate plus 1.0 band, capped at 9.0. Then:

1. Read [references/rewrite-guide.md](references/rewrite-guide.md).
2. Preserve the candidate's defensible core position and useful ideas unless the user requests a different approach.
3. Produce a complete standalone example that answers the original task and naturally demonstrates the target-band features.
4. Run `python3 "<SKILL_DIR>/scripts/text_stats.py"` on the rewritten example file and report its machine-estimated word count.
5. Explain the structure, criterion-level improvements, and the most reusable lessons.
6. Label the result as a target-level example, not a guaranteed examiner score.

## Enforce scoring guardrails

- Reflect an underlength response in the relevant descriptors and the available language evidence; do not invent a fixed numerical penalty for being below 150 or 250 words.
- Apply the public 20-words-or-fewer limiter exactly as described in the reference.
- Judge Academic Task 1 factual accuracy only against the supplied visual. Do not infer unseen figures, trends, stages, or map features.
- Judge General Training Task 1 tone against the stated relationship and purpose, not against a blanket preference for formal language.
- Judge Task 2 against every main part of the prompt. Do not reward fluent off-topic writing as a strong Task Response.
- Keep rewritten examples faithful to the supplied chart, situation, or prompt. Do not fabricate chart data, citations, research findings, or personal facts presented as true.
- Keep advice prioritised. Recommend the smallest changes most likely to move the response across the next band boundary.
- When the user asks only for a score, still give concise evidence sufficient to make the estimate auditable.
