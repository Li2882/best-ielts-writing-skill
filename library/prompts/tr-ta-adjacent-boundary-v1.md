# TR/TA adjacent-boundary correction v1

Date: 2026-09-24

This is a second-stage correction after the original selected TR/TA prompt has
produced a locked `base_band`. It does not replace the original score and does
not use a global anchor average.

## Locked base

- Copy `base_band` exactly from the supplied original result.
- Do not score LR, GRA or CC.
- Do not use the candidate's hidden human label.
- Do not convert an anchor median into a candidate score.
- Only one adjacent half-band change is allowed in this pass.

## Stage A: content evidence ledger (no score)

Extract task-specific evidence before judging the boundary:

Task 1: overview, dominant trends/stages, major series or groups, required
comparisons, and data support. Distinguish a secondary detail lapse from a
wrong or missing dominant trend.

Task 2: each prompt part, position, main claims, reasons, explanation/mechanism,
consequence/comparison/example, and relevance of the support. A concrete
example is optional when the reasoning itself is relevant and clear.

For every original deduction reason, classify it once:

- `unsupported`: the essay evidence does not support the criticism;
- `overstated`: a weakness exists but is not enough to block the higher band;
- `limiting`: the weakness matches a limiting feature of the next band;
- `material`: a major prompt part, trend, comparison or position is missing or
  materially wrong.

The official descriptors are positive-fit descriptors: a script must fully fit
the positive features of a band. Use the content ledger to decide that fit;
do not count omissions mechanically.

## Stage B: adjacent boundary comparison

The supplied anchors contain exactly three essays at `lower_band` and three at
`upper_band`, with the same task and criterion. Each anchor is shown twice in
the requested comparison list, once with the candidate first and once with the
anchor first. Return one decision for each of the 12 comparisons:

- `candidate_stronger`: candidate's TR/TA content is stronger;
- `comparable`: candidate and anchor are at the same practical level for this
  criterion;
- `anchor_stronger`: anchor's TR/TA content is stronger.

Judge content only. Ignore vocabulary, grammar, spelling and cohesion.
Reversing the presentation order must not change the decision.

## Program-controlled boundary rule

The program, not the model, computes the correction:

```text
upper_support = (candidate_stronger + comparable) / 6
lower_support = (candidate_stronger + comparable) / 6

if upper_support >= 0.75 and no limiting/material defect:
    correction = +0.5
elif lower_support < 0.25 and a limiting/material defect is evidenced:
    correction = -0.5
else:
    correction = 0.0
```

For the upper boundary, `upper_support` uses only the six comparisons against
`upper_band`; for the lower boundary, `lower_support` uses only the six
comparisons against `lower_band`. A correction cannot skip a boundary. If the
two reversed presentations of an anchor disagree, that anchor is not counted
as support; the program will not infer a score from the disagreement.

## Required JSON

Return JSON only:

```json
{
  "criterion": "TA or TR",
  "content_ledger": {
    "requirements": [{"id": "requirement", "status": "met|partial|missing", "evidence": "exact content evidence"}],
    "development": [{"id": "main idea or trend", "level": "none|limited|adequate|full", "evidence": "exact content evidence"}]
  },
  "original_reason_review": [{"reason": "original reason", "classification": "unsupported|overstated|limiting|material", "evidence": "exact content evidence"}],
  "comparisons": [{"comparison_id": "a1-forward", "anchor_id": "anchor", "order": "candidate_first|anchor_first", "decision": "candidate_stronger|comparable|anchor_stronger", "rationale": "content-only comparison"}],
  "correction_recommendation": "up|down|hold",
  "correction_reason": "content-only explanation"
}
```

The model must not output any numeric candidate score. The runner keeps the
locked base and calculates the correction from the adjacent-boundary decisions.
