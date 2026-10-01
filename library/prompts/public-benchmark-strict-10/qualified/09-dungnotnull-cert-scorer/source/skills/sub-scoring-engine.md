---
name: sub-scoring-engine
description: Score a writing or speaking sample against the official band descriptors, quote evidence per criterion, aggregate to an estimated band/level, and map to CEFR. Every estimate is labeled unofficial.
---

## Purpose
Produce a criterion-by-criterion band estimate that is grounded in the actual
sample text/transcript. No criterion may be scored without quoted evidence.

## Inputs
- `profile` (from `sub-profile-intake`): exam, variant, target, sample, current_level.
- `descriptor_set` (from `sub-framework-selector`): the loaded rubric for exam/variant/skill.

## Process

### 1. Branch on exam family

**IELTS (Writing)** uses four equally-weighted criteria:
Task Achievement/Response, Coherence & Cohesion, Lexical Resource,
Grammatical Range & Accuracy.

**IELTS (Speaking)** uses four equally-weighted criteria:
Fluency & Coherence, Lexical Resource, Grammatical Range & Accuracy,
Pronunciation.

**TOEIC** is item-scored, not rubric-scored. For a sample, estimate the
equivalent L&R/SW score band and map to ETS proficiency can-do statements.

**HSK** estimate the CEFR-equivalent from complexity, vocabulary breadth, and
grammar control, then map to HSK level (legacy or 3.0).

### 2. For each criterion, quote evidence
- Select a specific span of the sample (quote the exact words, or for speaking
  cite a transcript span/timestamp).
- Match the observed features to the descriptor row whose band best fits.
- Record: `criterion`, `band`, `evidence` (quoted span), `rationale` (1-2 lines).

### 3. Score each criterion to a band
- IELTS: integer or half bands 0.0-9.0 per the descriptor table in
  `SECOND-KNOWLEDGE-BRAIN.md` sections 1.2 / 2.2.
- If a criterion has no observable evidence in the sample, score it at the
  lowest defensible band and flag `evidence_missing`.

### 4. Aggregate to overall estimate
- IELTS Writing/Speaking overall = mean of four criteria, rounded to nearest
  0.5 using the IELTS convention:
    - raw fractional part < 0.25  -> round down to whole
    - 0.25 <= frac < 0.75          -> round to nearest .5
    - frac >= 0.75                 -> round up to next whole
  (equivalently: round(raw*2)/2 then to .5 grid).
- TOEIC: report the estimated score band and proficiency level.
- HSK: report the estimated CEFR level and the corresponding HSK level.

### 5. Map to CEFR
- Use the cross-exam table (`SECOND-KNOWLEDGE-BRAIN.md` section 5.2).
- Always note the mapping is approximate.

### 6. Label unofficial
Every estimate output MUST carry the literal label `unofficial estimate`.
Official scores require accredited examiners.

### 7. No-sample branch
If `profile.sample` is null, do NOT emit criterion bands. Instead output a
general skill assessment from `current_level` and flag `banding_deferred`;
request a sample.

## Outputs
```json
{
  "exam": "IELTS",
  "skill": "writing",
  "overall_band": 6.5,
  "cefr": "B2",
  "official_label": "unofficial estimate",
  "criteria": [
    {"name": "Task Achievement", "band": 7.0,
     "evidence": "...quoted span...", "rationale": "..."},
    {"name": "Coherence & Cohesion", "band": 6.0, "evidence": "...", "rationale": "..."},
    {"name": "Lexical Resource", "band": 6.5, "evidence": "...", "rationale": "..."},
    {"name": "Grammatical Range & Accuracy", "band": 6.5, "evidence": "...", "rationale": "..."}
  ],
  "flags": {"banding_deferred": false, "evidence_missing": false}
}
```

## Quality Gate
- [ ] Every criterion has quoted evidence from the sample.
- [ ] Each criterion band matches a descriptor row with a 1-2 line rationale.
- [ ] Overall band aggregated per the exam rounding convention.
- [ ] CEFR mapping present and marked approximate.
- [ ] Output carries the `unofficial estimate` label.
- [ ] No-sample case defers banding and requests a sample.
