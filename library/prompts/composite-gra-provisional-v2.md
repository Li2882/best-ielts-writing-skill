# Composite with GRA provisional plus lenient-up/strict-down anchors v2

Date: 2026-09-24

Status: development candidate. This is a project adaptation, not an official IELTS prompt and not a calibrated accuracy claim.

## Routing

Use the existing development routes for three criteria:

- TR/TA: quyen244 IELTS AI Evaluator
- CC: Gishguo IELTS Examiner Claude Skill
- LR: dungnotnull Language Cert Prep Scorer
- GRA: `library/prompts/gra-provisional-anchor-v2.md`

Return the four criteria independently. Do not average one criterion into another. Do not apply fixed offsets or a universal compensation.

## GRA route

Follow `gra-provisional-anchor-v2.md` exactly. Preserve the provisional score unless the same-task anchor gate supports a boundary decision. Between integer bands, round upward when the higher-band core is substantially present and no material disqualifying weakness is established; round downward only with positive evidence of recurring or systematic weakness. The final GRA band must be an integer when a rounding direction is declared.

This is development-only and must be evaluated on a new label-hidden holdout before replacing the existing composite route.
