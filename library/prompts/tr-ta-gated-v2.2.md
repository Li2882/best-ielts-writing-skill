# TR/TA task-fulfilment gate v2.2

Date: 2026-09-24

This project adaptation scores Task Achievement (Academic Task 1) or Task
Response (Task 2) only. It does not score LR, GRA or CC.

## Scope

Ignore vocabulary, grammar, spelling, collocation, punctuation, fluency and
style. A language problem belongs to TR/TA only when the content, position,
trend or comparison cannot be determined.

Use the official IELTS descriptors identified by `ielts-descriptors-2023-05` and
`ielts-key-criteria`, with the routed Task Response/Task Achievement source
package `04-quyen244-ai-evaluator`.

## Mandatory two-gate procedure

### Gate 1: requirement coverage

List every material requirement in the question and mark it `met`, `partial` or
`missing`. A requirement is material when omitting it would leave a question
part, major trend, major comparison or required position unanswered.

### Gate 2: development sufficiency

For every material requirement, judge whether the response provides enough
relevant content to satisfy the band descriptor. For a main idea or trend,
`developed` requires more than naming it:

- Task 1: the major feature is reported and supported by relevant comparison or
  data. Approximate values are acceptable; exact rounding is not the issue.
- Task 2: the main idea has a relevant explanation, cause, consequence,
  comparison or mechanism. A bare assertion is not developed.

Do not confuse `addressed` with `developed`: mentioning every part of the prompt
does not automatically qualify for Band 8 or Band 9.

## Band ceiling rules

Apply the ceiling before any anchor comparison:

```text
material requirement missing                  -> maximum Band 6
material requirement partial                  -> maximum Band 7
major trend/comparison or main idea underdeveloped -> maximum Band 7
all material requirements met and sufficiently developed -> Band 8 possible
all material requirements fully and balancedly developed -> Band 9 possible
```

These are operational ceilings for deciding whether the positive descriptor is
supported. They are not numeric deductions and do not replace the official
descriptors.

## Task 1 rules

- A clear overview must summarise the dominant pattern, comparison or stages.
  It need not repeat every category or year.
- If the body clearly reports a major trend, its absence from a short overview
  is not by itself a severe omission. However, an overview that only gives a
  ranking while omitting the dominant opposing trends limits the overview gate
  when those trends are not otherwise clearly highlighted.
- Every major series or major grouped feature must be covered. If several major
  categories lack the comparisons needed by the task, mark comparison coverage
  `partial` and cap the score at Band 7.
- One secondary detail error or approximate number does not impose a ceiling
  when the dominant patterns and key comparisons remain clear.

## Task 2 rules

- All requested views/questions and the writer's position are material
  requirements. A view that is only named but not explained is `partial`.
- A specific personal or real-world example is optional. Explanation, cause,
  consequence, comparison or mechanism is valid support.
- If a main idea is merely asserted, or its support is too unclear to establish
  relevance, mark development `partial` and cap the score at Band 7.
- If both views are addressed with relevant, sufficiently developed reasons, the
  response can reach Band 8. Band 9 additionally requires full, balanced and
  well-supported development of all material parts; the absence of a concrete
  example alone is not a reason to reject Band 9.
- If a prompt names distinct dimensions (for example family **and** local
  community), treating one as a passing mention does not count as full coverage.

## Optional gaps

Only classify a point as `optional_gap` when the response would still satisfy the
same band descriptor without it. Examples include an additional example, an
extra comparison after the required comparisons are already present, or a more
elegant overview. A missing material comparison, a superficial prompt dimension
or insufficient development is a `blocking_defect` because it imposes a band
ceiling.

## Anchors

Use same-task, same-type anchors only after applying the two gates. Anchors may
choose among bands permitted by the ceiling; they may not raise a response above
the coverage or development ceiling.

## Required JSON

Return JSON only:

```json
{
  "criterion": "TA or TR",
  "requirements": [
    {"id": "requirement", "status": "met|partial|missing", "development": "sufficient|partial|missing", "evidence": "exact content evidence"}
  ],
  "blocking_defects": [
    {"defect": "specific coverage or development defect", "evidence": "exact content evidence", "impact": "major|moderate", "band_ceiling": 7.0}
  ],
  "optional_gaps": [
    {"gap": "possible improvement", "evidence": "exact content evidence"}
  ],
  "coverage_ceiling": 9.0,
  "development_ceiling": 9.0,
  "candidate_band": 8.0,
  "final_band": 8.0,
  "downgrade_reason": null,
  "justification": "Content-only explanation."
}
```

If a blocking defect exists, set the relevant ceiling to 6.0 or 7.0 and do not
return a final band above it. `downgrade_reason` must name the defect. If no
blocking defect exists, it must be `null`.
