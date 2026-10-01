# LR V4-capped recurrence deduction v8

Check Lexical Resource errors independently. Do not see or use anchor essays. The calibrated base is locked and cannot be reconsidered.

Classify genuine lexical problems as follows:

- `valid_or_isolated`: acceptable wording, necessary topic repetition, stylistic preference, or one/two isolated genuine slips. Candidate deduction 0.
- `recurrent_clear`: the same or closely related genuine lexical pattern occurs at least three times or in at least two paragraphs, while meaning remains immediately clear. Candidate deduction 0.5.
- `restricting`: the same or closely related genuine lexical pattern occurs at least four times or across at least two paragraphs and repeatedly restricts expression or causes difficulty in understanding. Candidate deduction 1.0.

Do not combine unrelated isolated errors merely to reach the frequency threshold. Do not count grammar errors as lexical errors. Do not count a phrase merely because a more elegant alternative exists.

The supplied `v4_max_deduction` is a hard ceiling inherited from V4. It cannot be increased by a new classification. Calculate:

`applied_deduction = min(candidate_deduction, v4_max_deduction)`

`final_score = calibrated_base - applied_deduction`

Quote the repeated lexical pattern that qualifies. If no related pattern reaches the threshold, apply zero deduction.
