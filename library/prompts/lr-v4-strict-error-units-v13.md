# LR V4-centred strict-error units v13

The V4 base score is fixed. A same-task anchor adjustment is a separate calibration value. If the anchor adjustment is non-zero, the anchor stage has already corrected the overall lexical level; do not apply an independent deduction.

When the anchor adjustment is zero, audit lexical problems in two stages.

## Error status

`strict_error`: an objective lexical error that a competent IELTS examiner would clearly mark as wrong, such as a wrong meaning, wrong word form, wrong category/measure, a collocation that is objectively unacceptable, or spelling that creates the wrong lexical item. It must be more than an alternative that sounds less elegant.

`nonstandard_but_acceptable`: understandable wording, an uncommon but valid collocation, an awkward expression, a stylistic preference, or a phrase that can be improved without changing correctness. Do not count it as a separate error.

Grammar-only errors belong to GRA. Necessary repetition of topic terms, chart categories, named entities, or argument terms is valid and is never an LR error.

## Strict-error units

- Count each independent `strict_error` as one unit.
- Any number of nonstandard-but-acceptable expressions together count as at most **one** strict-error-equivalent unit, and only when they show a coherent recurring weakness. They must never be counted one by one.
- Do not upgrade a nonstandard expression to a strict error merely to reach a threshold.
- Do not count one wording problem twice as both a strict error and a nonstandard cluster.

## Deduction threshold

- `valid_or_isolated`: fewer than two strict-error units, or the units are confined to one paragraph. Candidate deduction 0.
- `recurrent_clear`: at least two strict-error units across at least two paragraphs, while meaning remains immediately clear. Candidate deduction 0.5.
- `restricting`: at least three strict-error units across at least two paragraphs and repeated difficulty or restriction of expression. Candidate deduction 1.0.

The supplied `v4_max_deduction` remains a hard ceiling:

`applied_deduction = min(candidate_deduction, v4_max_deduction)`

`final_score = calibrated_base - applied_deduction`

Quote every strict error, separately list nonstandard-but-acceptable items, and explain why each was not counted as a strict error. If the anchor adjustment is non-zero, return zero deduction.
