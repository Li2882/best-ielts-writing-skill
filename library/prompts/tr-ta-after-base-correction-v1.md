# TR/TA correction after locked original base v1

Date: 2026-09-24

This is a correction layer applied **after** the original selected TR/TA
prompt has produced a locked `base_band`. It does not replace or rerun the
original scorer. The original prompt is
`library/prompts/composite-best-traits-v1.md`, routed to the original
`04-quyen244-ai-evaluator` TR/TA rubric.

## Locked-base rule

- Treat `base_band` as the original prompt's first-pass result.
- Do not assign a new independent TR/TA band.
- Do not score LR, GRA or CC.
- Do not use a fixed upward or downward compensation.
- Inspect only the original prompt's stated content-related reasons and the
  supplied same-task, same-type anchors.

## Defect classification and caps

Classify each original deduction reason exactly once:

| Classification | Examples | Maximum effect |
|---|---|---:|
| `optional_gap` | extra example, more elegant overview, extra detail after the required content is already present | 0.0 |
| `minor_omission` | one secondary data point or secondary detail is absent or slightly incomplete | 0.5 each, at most 2 counted, total 1.0 |
| `material_single_gap` | one major comparison, major trend, or one independent prompt part is materially missing | 1.0 |
| `multiple_material_gaps` | at least two independently evidenced major requirements are missing | 1.5 maximum |

Rules:

1. A `minor_omission` may be counted twice. The first and second distinct
   secondary omissions may each contribute at most 0.5. A third secondary
   omission is not counted separately.
2. The same omission cannot be counted as both a minor omission and a material
   gap, or under coverage and development.
3. Repeating the same defect in several sentences counts once.
4. A concrete example is optional in Task 2 when the idea has relevant
   explanation, cause, consequence, comparison or mechanism.
5. A Task 1 overview need not repeat every category, year or secondary number
   when the dominant patterns and required comparisons are clear.

## Anchor correction

Use only anchors with the same task and criterion: Task 1/TA with Task 1/TA,
Task 2/TR with Task 2/TR. Compare content fulfilment, not vocabulary or
grammar.

Set `anchor_reference` to the median band of the supplied comparable anchors.
Then choose one correction delta:

```text
base_band is within 0.5 of anchor_reference -> delta = 0.0
base_band is 0.5 below anchor_reference     -> delta = +0.5 at most
base_band is at least 1.0 below anchor_reference
  and no material_single_gap is evidenced   -> delta = +1.0 at most
base_band is above anchor_reference         -> no automatic downward delta
```

The anchor delta cannot be used to override a clearly evidenced material gap.
Do not jump directly from Band 6 to Band 8. The largest upward or downward
change caused by one content issue is 1.0 band.

## Calculation

The correction layer must report both the original deduction and the bounded
correction. Use:

```text
applied_defect_effect = min(original_defect_effect, defect_cap)
corrected_band = clamp(base_band + anchor_delta, 4.0, 9.0)
```

The defect cap is used to audit whether the original prompt over-penalised a
reason; it is not added a second time to `base_band`. Never double-count a
defect by subtracting it again after the base score.

## Required JSON

Return JSON only:

```json
{
  "criterion": "TA or TR",
  "base_band": 6.0,
  "original_reasons": [
    {"reason": "original prompt reason", "classification": "optional_gap|minor_omission|material_single_gap|multiple_material_gaps", "evidence": "exact content evidence"}
  ],
  "minor_omission_count": 0,
  "original_defect_effect": 0.0,
  "defect_cap": 0.0,
  "applied_defect_effect": 0.0,
  "anchor_reference": 6.0,
  "anchor_delta": 0.0,
  "corrected_band": 6.0,
  "correction_reason": "why the bounded correction was or was not applied"
}
```

`minor_omission_count` must be an integer from 0 to 2. For two counted minor
omissions, `defect_cap` must be 1.0. `corrected_band` must equal
`clamp(base_band + anchor_delta, 4.0, 9.0)`.
