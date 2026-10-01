# GRA provisional plus same-task anchor v1

Date: 2026-09-24

Status: development candidate. This is a project adaptation, not an official IELTS prompt and not a calibrated accuracy claim.

## Purpose

This criterion-only workflow addresses the observed GRA failure mode in which a mostly correct provisional band is reduced again by a second error-counting pass. The provisional band is therefore the final candidate by default. A same-task anchor comparison is allowed only when the provisional judgement is uncertain between adjacent bands.

The workflow is informed by the official IELTS descriptors and key assessment criteria, plus the project's LR V4 and GRA deduction-cap development reports. Those reports are diagnostic evidence, not scoring rules.

## Scope and sources

Use the following project standards:

- `library/standards/ielts-writing-band-descriptors-reading.txt`
- `library/standards/ielts-writing-key-assessment-criteria-reading.txt`

Assess GRA only. Do not move lexical awkwardness, collocation, register, or content problems into GRA unless there is a specific grammatical rule violation.

For Task 1, inspect the supplied chart or verified chart facts. For Task 2, inspect the complete essay. Do not infer GRA from the overall score or from another criterion.

## Required procedure

### 1. Sentence-level evidence ledger

Segment the response into sentences without silently correcting it. For each sentence, record:

- whether it is grammatically controlled;
- the genuine GRA issue, if any;
- the issue family: verb form/tense, agreement, article/determiner, pronoun, clause construction, sentence boundary, punctuation, or another explicit grammar rule;
- whether the same pattern appears elsewhere;
- whether the issue affects understanding or requires rereading.

Group repeated instances of the same error pattern. Record the occurrence count, but do not subtract once per occurrence. Repetition can show a systematic weakness; it is not permission for automatic additive penalties.

Do not count these as GRA by themselves:

- ordinary or repetitive vocabulary;
- unnatural collocation without a grammar violation;
- a possible stylistic improvement;
- a less sophisticated but grammatical sentence;
- a punctuation preference that does not change sentence structure or clarity.

### 2. Four GRA components

Judge the following separately before choosing a band:

1. **Structural range:** simple and complex forms, including subordinate, relative, conditional, concessive, participial, passive, and coordinated structures where genuinely present.
2. **Error-free sentence frequency:** whether error-free sentences are occasional, frequent, or the majority. Do not use a raw error count without considering the total number of sentences.
3. **Grammar and punctuation control:** whether errors are isolated, recurring, or systematic, and whether complex structures remain controlled.
4. **Communication impact:** whether errors are harmless, require rereading, obscure meaning, or disrupt logical relations.

Successful structures and clear communication must be recorded alongside weaknesses. Do not let one visible error erase the rest of the response.

### 3. Provisional band

Choose a provisional band from the official descriptors using the four components. Explain why it fits the chosen band rather than the adjacent lower and higher bands.

The provisional band is the final score by default. There is no general deduction pass and no subtraction for each listed error.

### 4. Same-task anchor gate

Use anchors only when all conditions hold:

- the provisional judgement is genuinely uncertain between adjacent bands;
- the anchor is for the same task type (Task 1 with Task 1, Task 2 with Task 2);
- the anchor has a verified GRA score and usable original response or criterion evidence;
- the anchor comparison is based on the four GRA components, not vocabulary complexity or surface sophistication.

Compare the response with at least one adjacent-band anchor when available. If the anchors conflict, report the uncertainty instead of forcing a change. An anchor can move the provisional score by one adjacent half-band only when the component-level comparison supports it.

Do not borrow a Task 2 anchor for a Task 1 boundary. Do not use an anchor to trigger a new deduction pass. Do not use target labels, post-hoc results, or the expected answer to select a favourable anchor.

### 5. Final score

Set `final_band = provisional_band` unless the same-task anchor gate produces a documented adjacent-boundary correction. After an anchor correction, do not subtract again for the same evidence.

Report uncertainty when high-band evidence is incomplete. A short response that meets the task minimum is not by itself a reason to lower GRA; judge the structures and control that are actually present.

## Required output

Return:

- `provisional_band`
- `final_band`
- `component_evidence` for structural range, error-free sentence frequency, grammar/punctuation control, and communication impact
- `error_ledger` with grouped patterns, counts, and impact
- `anchor_used` (none or the same-task anchor ids)
- `anchor_decision` and the exact boundary evidence if the score changed
- `confidence`
- `limitations`

This version is for development and ablation testing. It must be compared against provisional-only and prior capped versions on new, label-hidden Task 1 and Task 2 samples before adoption.

