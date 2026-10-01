# LR V4-centred anchor-aware strict deduction v12

The V4 base score is fixed. A same-task anchor adjustment is a separate calibration value. If the anchor adjustment is non-zero, the anchor stage has already corrected the relevant overall lexical level; do not apply an independent deduction in that case.

If and only if the anchor adjustment is zero, inspect the response for genuine LR problems. Count different errors collectively, but exclude necessary topic/category repetition. A genuine problem must be an incorrect word choice, collocation, word form, spelling that changes the lexical item, or unnatural lexical construction. Grammar-only errors do not count.

Strict deduction threshold when anchor adjustment is zero:

- `valid_or_isolated`: fewer than four distinct genuine LR problems, or the problems are confined to one paragraph. Candidate deduction 0.
- `recurrent_clear`: at least four distinct genuine LR problems distributed across at least two paragraphs, but meaning remains immediately clear. Candidate deduction 0.5.
- `restricting`: at least five distinct genuine LR problems distributed across at least two paragraphs and repeatedly restricting expression or causing difficulty understanding. Candidate deduction 1.0.

Do not count necessary repetition of prompt terms, chart categories, entities, or argument terms required for precise comparison. Do not count a stylistic preference. Do not double-count the same error. The supplied V4 maximum deduction is a hard ceiling:

`applied_deduction = min(candidate_deduction, v4_max_deduction)`

`final_score = calibrated_base - applied_deduction`

Quote every counted error and identify its paragraph. If anchor adjustment is non-zero, return zero deduction and state that the issue is already accounted for by the anchor adjustment.
