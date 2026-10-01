# Composite with GRA provisional plus same-task anchors v1

Date: 2026-09-24

Status: development candidate. This is not the active scorer and has no new accuracy result.

## Routing

Use the existing development routes for three criteria:

- TR/TA: quyen244 IELTS AI Evaluator
- CC: Gishguo IELTS Examiner Claude Skill
- LR: dungnotnull Language Cert Prep Scorer
- GRA: `library/prompts/gra-provisional-anchor-v1.md`

Return the four criteria independently. Do not average one criterion into another. Do not apply fixed offsets or a universal compensation.

## GRA route

Follow `gra-provisional-anchor-v1.md` exactly:

1. Build a sentence-level GRA evidence ledger.
2. Separate structural range, error-free sentence frequency, grammar/punctuation control, and communication impact.
3. Produce a provisional GRA band.
4. Treat the provisional band as the final candidate by default. Do not run a general deduction pass.
5. Use only same-task anchors for a genuinely uncertain adjacent-band boundary.
6. If an anchor changes the provisional band, document the component-level reason and do not deduct again.

This candidate exists to test whether removing GRA's second deduction pass reduces under-scoring before adding any broader calibration. It must be compared with `composite-best-traits-v1.md` and the provisional-only GRA ablation on new label-hidden Task 1 and Task 2 samples.

