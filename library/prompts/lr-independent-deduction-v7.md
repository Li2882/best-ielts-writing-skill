# LR independent deduction v7

The candidate has a locked half-band `base_band` from a task-specific successful-vocabulary comparison. Do not change or reconsider that base. This stage is independent: it receives no anchor essays, anchor scores or anchor rationales.

## Deduction threshold

First classify every suspected lexical issue as `valid`, `isolated`, `recurrent_clear`, or `restricting`.

- `valid`: acceptable in context, necessary topic wording, or merely less elegant than an alternative. Deduction 0.
- `isolated`: one or two genuine slips with immediately clear meaning and no repeated pattern. Deduction 0.
- `recurrent_clear`: use this category only when the same or closely related genuine pattern appears at least three times or in at least two paragraphs, while meaning remains immediately clear. Its maximum deduction is 0.5.
- `restricting`: use this category only when a genuine pattern appears at least four times or across at least two paragraphs and it repeatedly restricts expression or causes difficulty understanding. Its maximum deduction is 1.0.

The higher frequency threshold is deliberate. Do not convert a few isolated collocation preferences into a score deduction. Do not count necessary repetition of topic words. A phrase that can be made more elegant is not automatically an error.

Apply the original LR judgement to the locked base and state `original_deduction`. Independently set `cap_deduction` from the categories above, then calculate:

`applied_deduction = min(original_deduction, cap_deduction)`

`final_score = base_band - applied_deduction`

Use IELTS half bands. Quote each issue that actually supports a deduction. Do not double-count the same issue.
