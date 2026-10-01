# TR/TA task-fulfilment gate v2.1

Date: 2026-09-24

This is a project adaptation for Task Response (Task 2) and Task Achievement
(Academic Task 1) only. It is not a replacement for the official IELTS
descriptors and does not score LR, GRA or CC.

## Scope

Assess only whether the response fulfils the task. Ignore vocabulary, grammar,
spelling, collocation, punctuation, fluency and stylistic elegance. A language
problem belongs to TR/TA only when it makes the relevant idea, position, trend or
comparison impossible to determine.

## Descriptor reference

Use the official IELTS writing descriptors identified by:

- `ielts-descriptors-2023-05`
- `ielts-key-criteria`
- routed source package `04-quyen244-ai-evaluator`

The following compressed distinctions are operational guidance, not new official
bands:

### Academic Task 1: Task Achievement

- Band 9: fully satisfies the task; overview is clear and fully developed; key
  features are accurate and fully extended.
- Band 8: covers all requirements sufficiently; overview is clear; key features
  are well selected and highlighted.
- Band 7: covers the requirements; overview is clear; key features are selected
  and highlighted, though detail may be less complete or occasionally irrelevant.
- Band 6: addresses the requirements; an overview is attempted; some key features
  are covered, but detail may be incomplete, inappropriate or inaccurate.

### Task 2: Task Response

- Band 9: fully addresses all parts; position is fully developed; ideas are
  relevant, fully extended and well supported.
- Band 8: sufficiently addresses all parts; response is well developed; ideas
  are relevant, extended and supported.
- Band 7: addresses all parts; position is clear; main ideas are extended and
  supported, though some may be general or less focused.
- Band 6: addresses the main parts; position is relevant; some main ideas may be
  inadequately developed or unclear.

## Mandatory scoring procedure

1. Identify the task type and list the task requirements before assigning a band.
2. Mark each requirement `met`, `partial` or `missing`, with exact content
   evidence from the response.
3. Separate `blocking_defects` from `optional_gaps`.
4. Select the highest band supported by the content evidence.
5. Lower that candidate only when a specific blocking defect contradicts the
   positive descriptor of the selected band.
6. If there is no blocking defect, keep the candidate band. Do not subtract a
   numeric penalty for optional gaps.

## Task 1 rules

- An overview must summarise the dominant pattern, comparison or stages. It does
  not need to list every category, year or trend.
- The body can establish that a feature is covered; do not treat the absence of
  a repeated detail in the overview as a severe omission.
- An isolated inaccuracy in one secondary detail is a limited lapse, not a
  blocking defect, when the dominant direction and key comparisons remain clear.
- Approximate chart values do not block a high TA when the categories, directions,
  rankings and comparisons are correct. Do not lower TA solely for minor rounding
  or approximate wording of a number.
- Do not lower TA merely because the overview could be more detailed, elegant or
  closer to a model answer.
- Ignore wording, units, spelling and grammar unless the meaning of a key trend
  or comparison cannot be determined.

## Task 2 rules

- A specific personal or concrete example is optional, not a mandatory condition
  for Band 8 or Band 9.
- Explanation, cause, consequence, comparison or mechanism counts as development
  and support.
- Do not lower TR merely because an example could have been added.
- Mark an idea as insufficiently developed only when it is substantially asserted
  without relevant explanation or support.
- If both views are addressed, the position is consistent, and each main idea has
  relevant explanation or mechanism, general framing alone does not block Band 9.
  Do not require concrete real-world specificity to distinguish Band 9 from Band 8.

## Blocking-defect policy

The following can block a high band when material to the prompt:

- a required part of the question is not answered;
- the position is unclear or materially inconsistent in Task 2;
- Task 1 has no genuine overview;
- a dominant trend, comparison or stage is absent or materially reversed rather
  than merely omitted from a brief overview;
- multiple key features are materially inaccurate, or one inaccuracy obscures the
  dominant pattern;
- the response is largely a list of assertions with no relevant development.

The following are optional gaps and cannot alone lower the band:

- a more specific example could be added;
- an overview could mention one more trend;
- a comparison could be made more detailed;
- a reason could be expanded further;
- the response could be more sophisticated or elegant.

## Required output

Return JSON only:

```json
{
  "criterion": "TA or TR",
  "requirements": [
    {"id": "short requirement id", "status": "met|partial|missing", "evidence": "exact content evidence"}
  ],
  "blocking_defects": [
    {"defect": "specific defect", "evidence": "exact content evidence", "impact": "major|moderate"}
  ],
  "optional_gaps": [
    {"gap": "possible improvement", "evidence": "exact content evidence"}
  ],
  "candidate_band": 8.0,
  "final_band": 8.0,
  "downgrade_reason": null,
  "justification": "Content-only explanation of why the final band fits."
}
```

`downgrade_reason` must be `null` when `blocking_defects` is empty. Never lower a
score solely because an optional gap exists. Do not average the criteria and do
not output LR, GRA or CC scores.
