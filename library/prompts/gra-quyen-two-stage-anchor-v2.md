# GRA quyen two-stage overall-band anchor calibration v2

Stage 1 independently scores GRA with the selected quyen244 GRA rubric. The score and evidence are locked before any reference is shown.

Stage 2 selects six same-task reference essays at each local half-band overall score around the locked score: minus 1.0, minus 0.5, plus 0.5, and plus 1.0. The overall score is only a retrieval bin; it is never treated as the anchor's GRA score. The model compares the candidate prose with the six-essay group on structural range, error-free sentence frequency, grammar and punctuation control, and communication impact.

A proposed half-band movement needs at least two GRA dimensions pointing the same way across the relevant group. A full-band movement needs at least three dimensions and a clear boundary crossing. A target group with fewer than six eligible same-task references, conflicting evidence, or weak boundary evidence retains the locked Stage 1 score. The maximum movement is one band.

Reference eligibility is `status=verified`, `split=reference`, reliable individual human scoring, and no unresolved quality issue. The original eight test essays, their prompt groups, duplicate texts, and holdout material are excluded from anchor selection.

This is a development workflow. It is not an official IELTS scoring rule and does not establish accuracy on new candidates.
