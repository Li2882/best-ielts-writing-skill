# GRA quyen two-stage local-anchor calibration v1

Date: 2026-09-25

Status: development candidate. This is a project workflow, not an official IELTS scoring rule or an accuracy claim.

## Stage 1: independent base score

Use the GRA criterion prompt and compressed GRA rubric from the selected `quyen244 IELTS AI Evaluator` package. Score the candidate independently. Do not supply reference essays, anchor scores, candidate labels, teacher comments, or historical predictions.

Lock the resulting half-band `base_band`, justification, quoted evidence, strengths, weaknesses, improvements, and confidence before any anchor is selected.

## Stage 2: local anchor comparison

After Stage 1 is locked, select same-task anchors mechanically at the four local target bands:

- `base_band - 1.0`
- `base_band - 0.5`
- `base_band + 0.5`
- `base_band + 1.0`

Do not choose anchors using the candidate's human label or the desired result. If an exact target band has no eligible same-task anchor, record that band as missing; do not substitute a different task or infer a trait score from an overall score.

Stage 2 does not rescore the essay from scratch. It compares the locked Stage 1 judgement with the supplied anchors on only four GRA dimensions:

1. structural range and flexibility;
2. frequency of error-free sentences;
3. grammar and punctuation control;
4. communication impact of errors.

Lexical naturalness, task achievement/response, cohesion, topic sophistication, and overall score are excluded.

## Adjustment gate

The proposed adjustment must be one of `-1.0`, `-0.5`, `0`, `+0.5`, or `+1.0`.

- A non-zero adjustment requires an eligible anchor at the proposed final band.
- A half-band adjustment requires at least two of the four GRA dimensions to support the same direction.
- A full-band adjustment requires at least three dimensions and evidence that the candidate crosses the intervening half-band boundary.
- Conflicting, weak, or incomplete comparisons retain the locked base score.
- The final score may never differ from the locked base score by more than one band.

The program validates these conditions mechanically and preserves both the proposed and applied adjustment.
