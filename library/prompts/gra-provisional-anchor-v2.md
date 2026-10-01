# GRA provisional plus same-task anchor v2

Date: 2026-09-24

Status: development candidate. This is a project adaptation, not an official IELTS prompt and not a calibrated accuracy claim.

## Purpose

This version keeps the v1 provisional-only rule and changes only the adjacent-band anchor decision. When the candidate lies between two integer-band anchors, do not default to the lower half-band. Use a lenient upward rounding rule and a strict downward rule.

## Core method

1. Build a sentence-level GRA evidence ledger without silently correcting the original.
2. Separate structural range, error-free sentence frequency, grammar/punctuation control, and communication impact.
3. Produce a provisional GRA band from the official descriptors.
4. Do not run a general deduction pass. The provisional band is the final candidate unless the anchor gate below changes it.

Group repeated instances of the same error pattern. Repetition is evidence of a possible systematic weakness, not an additive subtraction. Do not count lexical awkwardness, collocation, register, or stylistic improvement as GRA without an explicit grammar-rule violation.

## Same-task anchor gate

Use only verified same-task anchors and only at a genuinely uncertain adjacent-band boundary. Compare the four GRA components, not vocabulary complexity, essay topic, or visible sophistication.

### Lenient upward rounding

When the candidate is between a lower and higher integer anchor, round up to the higher band if the higher-band core requirements are substantially present and the evidence does not establish a disqualifying weakness. The following are compatible with upward rounding when meaning remains clear:

- isolated errors or a small number of repeated minor errors;
- punctuation or determiner slips that do not change sentence relations;
- occasional awkwardness that belongs to LR rather than GRA;
- one weak sentence surrounded by controlled sentences;
- absence of an additional advanced structure that was not required by the task.

Do not demand near-perfect accuracy merely because the higher anchor is cleaner. A cleaner anchor is evidence of the upper boundary, not a requirement to reproduce every sentence pattern.

### Strict downward rounding

Round down only when there is positive evidence that the higher band is not met. At least one of the following must be documented, and the evidence must be material rather than a single isolated slip:

- a recurring grammar pattern across multiple sentences;
- complex structures are repeatedly attempted but uncontrolled;
- error-free sentences are not frequent enough for the higher band;
- errors repeatedly require rereading, obscure meaning, or disrupt logical relations;
- a basic grammar weakness is systematic rather than occasional.

If the evidence is genuinely ambiguous between these outcomes, choose the higher integer band and report the uncertainty. Do not retain an `x.5` score solely because the response is imperfect.

An anchor correction may move the score by one adjacent half-band or to the higher/lower integer boundary under this rounding rule. After correction, never run another deduction pass for the same evidence.

## Task separation and limitations

Task 1 and Task 2 anchors must not be mixed. A short response that meets the task minimum is not automatically downgraded for length. Public teacher labels are development evidence, not official exam results. This version must be tested on new label-hidden samples before adoption.

## Required output

Return `provisional_band`, `final_band`, the four component evidence fields, grouped `error_ledger`, `anchor_used`, `anchor_decision`, `rounding_direction` (`up`, `down`, or `none`), `confidence`, and `limitations`.

