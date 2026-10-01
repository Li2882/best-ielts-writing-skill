# LR V4-locked collective-error deduction v9

Score Lexical Resource only. The supplied V4 base score is locked. Do not change or reconsider the base score and do not use anchor essays.

Identify genuine lexical-resource problems: wrong word choice, wrong collocation, wrong word form, spelling that changes the lexical item, or an unnatural lexical construction. Grammar errors belong to GRA and must not be counted here.

Count different genuine lexical problems collectively when deciding whether the response has a recurrent LR weakness. They do not have to be the same word or identical pattern. A deduction requires at least three genuine lexical problems distributed across the response, or a clearly repeated lexical tendency across at least two paragraphs. Do not manufacture a pattern from stylistic preferences.

Do not penalise repetition when the word is:

- a necessary topic term from the question or visual;
- the name of a category, person, place, object, or process that must be referred to repeatedly;
- needed to keep the argument precise and replacing it would reduce accuracy;
- repeated only because the candidate is comparing the same required entities.

For example, repeated words such as `research`, `spending`, `health`, `film`, `cinema`, or named chart categories are not automatically LR errors. Penalise them only when the repetition is avoidable and contributes to a genuine lexical weakness.

Classify the result:

- `valid_or_isolated`: fewer than three genuine lexical problems after necessary topic repetition is excluded. Candidate deduction 0.
- `recurrent_clear`: at least three genuine lexical problems or a recurrent tendency across two paragraphs, while meaning remains immediately clear. Candidate deduction 0.5.
- `restricting`: at least four genuine lexical problems or a recurrent tendency across two paragraphs that repeatedly restricts expression or causes difficulty understanding. Candidate deduction 1.0.

The supplied `v4_max_deduction` is a hard ceiling. It cannot be increased. Calculate:

`applied_deduction = min(candidate_deduction, v4_max_deduction)`

`final_score = v4_base - applied_deduction`

Quote every lexical error counted and state why necessary topic repetition was excluded. Do not double-count one error, and do not use a possible stylistic improvement as an error.
