# LR original judgement, then one-way deduction cap v3

Date: 2026-09-24

Score Lexical Resource only.

## Mandatory order

### Step 1: preserve the locked original judgement

The candidate data includes a locked `original_score` and `original_rationale` produced by the original LR scorer. Treat them as immutable. Do not re-score the essay and do not change the original score. Use the complete original LR source package below only to interpret whether the cited weaknesses were tolerated or actually limited the band.

### Step 2: decide whether the original judgement already tolerated the weaknesses

Classify the repetition, collocation, word-choice, spelling and word-formation weaknesses as one of:

- `isolated_or_tolerated`: the issues are occasional, rare, immediately understandable, optional improvements, or already compatible with the original band;
- `recurrent_but_clear`: a repeated pattern exists, but meaning remains immediately clear and expression is not substantially restricted;
- `restricting_or_difficult`: the repeated pattern clearly restricts expression or repeatedly causes difficulty in understanding.

If the classification is `isolated_or_tolerated`, or if the original rationale did not actually use a lexical weakness to limit the band, set `final_score = original_score`.

### Step 3: apply the cap only if the original score was actually limited by these weaknesses

Only when the original rationale says that repetition, collocation or related lexical errors lowered or limited the band:

- identify the `successful_range_band`: the band supported by the successfully used vocabulary range, flexibility and precision before that limitation;
- for `recurrent_but_clear`, the final score may be no lower than `successful_range_band - 0.5`;
- for `restricting_or_difficult`, the final score may be no lower than `successful_range_band - 1.0`.

Then set:

`final_score = max(original_score, the applicable capped floor)`

This is a one-way correction. **The final score must never be lower than the locked original score.** Necessary repetition of topic words is not a fault. A phrase that could merely be more elegant is not an error.

## Original LR source package


### Original file: `library/prompts/public-benchmark-strict-10/qualified/09-dungnotnull-cert-scorer/source/skills/sub-scoring-engine.md`

```text
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

```

### Original file: `library/prompts/public-benchmark-strict-10/qualified/09-dungnotnull-cert-scorer/source/SECOND-KNOWLEDGE-BRAIN.md`

```text
# SECOND-KNOWLEDGE-BRAIN.md — Language Certification Prep & Scorer (Idea 61)

Grown weekly by `tools/knowledge_updater.py` (dedupe by 12-char SHA-1 hash).
This file is the canonical, offline-fallback knowledge base. Every scoring
decision in `sub-scoring-engine` MUST be traceable to a descriptor row below.

---

## 1. IELTS — Writing (Academic & General)

### 1.1 Criteria & Weights
| Criterion | Weight | Applies to |
|-----------|--------|------------|
| Task Achievement (TA) / Task Response (TR) | 25% | Academic & General |
| Coherence & Cohesion (CC) | 25% | Academic & General |
| Lexical Resource (LR) | 25% | Academic & General |
| Grammatical Range & Accuracy (GRA) | 25% | Academic & General |

Overall Writing band = mean of the four criterion bands, rounded to nearest
0.5 (IELTS rounding convention: x.25→x.5, x.75→next whole).

### 1.2 Public Band Descriptors (summary of official rubric)
| Band | Task Achievement/Response | Coherence & Cohesion | Lexical Resource | Grammatical Range & Accuracy |
|------|---------------------------|----------------------|------------------|------------------------------|
| 9 | fully addresses all parts; fully developed position; relevant, extended, supported ideas | uses cohesion skilfully; paragraphing seamless; logical management | wide range, precise, natural, rare errors | full flexible accurate; rare minor slips |
| 8 | sufficiently addresses all parts; well developed, relevant | logical; good progression; cohesive devices effective; paragraphing appropriate | wide range fluent; occasional inaccuracies; rare errors in word choice/collocation | wide range; majority error-free; occasional slips |
| 7 | addresses all parts; presents clear position throughout; supports main ideas but may be over-/under-supported | logically organized; clear progression; range of cohesive devices (some over/under-use); paragraphing present | sufficient range for some precision; some awareness of style/collocation; occasional errors | various complex forms; frequent error-free sentences; some errors in grammar but rarely impede |
| 6 | addresses all parts (some more than others); relevant position but conclusions may be unclear; ideas relevant but not fully developed | arranges info coherently; overall progression; cohesive devices effective but mechanical; paragraphing may be illogical | adequate range; attempts less common items but with inaccuracy; errors in word choice/spelling but not impeding | mix of simple/complex; makes some errors in grammar/punctuation but rarely impede |
| 5 | addresses task only partially; format may be inappropriate; position stated but unclear; ideas limited/not developed; detail may be irrelevant | presents info with some organization; progression evident; inadequate cohesive devices; repetitive; paragraphing inadequate | limited range; adequate for basic tasks; attempts less common items with limited success; noticeable errors in spelling/word choice | limited range; attempts complex forms with limited success; frequent errors in grammar/punctuation; some impede |
| 4 | responds to task minimally; format inappropriate; position unclear; ideas hard to follow | presents info/ideas but hard to follow; no clear progression; limited cohesive devices; repetitive | limited range; word forms/spelling errors frequent; errors impede | limited range; frequent errors in grammar/punctuation impede |
| 3 | does not address task; ideas irrelevant; minimal response | no clear organization; no cohesive devices | vocabulary very limited; word forms/spelling errors severe | sentence forms limited/rare; frequent errors impede |
| 2 | barely responds; no position; few relevant ideas | no organization; minimal cohesive devices | vocabulary extremely limited; errors severe | sentence forms rare; frequent errors severe |
| 1 | answer completely irrelevant | no communication of ideas | vocabulary insufficient | no rateable language |
| 0 | does not attend; no usable response | — | — | — |

> Source: IELTS public band descriptors (ielts.org / Cambridge). Summarized for
> offline use; always verify currency via `sub-framework-selector`.

---

## 2. IELTS — Speaking

### 2.1 Criteria & Weights
| Criterion | Weight |
|-----------|--------|
| Fluency & Coherence (FC) | 25% |
| Lexical Resource (LR) | 25% |
| Grammatical Range & Accuracy (GRA) | 25% |
| Pronunciation (PR) | 25% |

### 2.2 Public Band Descriptors (summary)
| Band | Fluency & Coherence | Lexical Resource | Grammatical Range & Accuracy | Pronunciation |
|------|---------------------|------------------|------------------------------|---------------|
| 9 | speaks at length without effort; appropriate topics; develops fully coherently | precise, flexible; idiomatic, low-frequency items | accurate/flexible; errors rare | effortless; flexible; subtle features |
| 8 | fluent; develops topics relevantly, coherently, appropriately | wide range, flexible; conveys precise meaning; rare inaccuracies | wide flexible; frequent error-free; slips rare | easy to understand; effective use of features; occasional lapses |
| 7 | speaks at length without noticeable effort; some loss of coherence; topic relevant, develops coherently | flexible; some precision; awareness of collocation/style; some inappropriate items | various complex forms; frequent error-free; some persistent errors | shows features but not sustained; generally clear; occasional lapses |
| 6 | willing at length; some repetition/loss of coherence; topics relevant; uses range of connectors but not always appropriately | adequate range; attempts less common items with some inaccuracy; meaning clear | mix simple/complex; complex forms limited; errors in grammar/punctuation frequent but not impeding | uses range of features with mixed control; generally clear; mispronunciations not impeding |
| 5 | usually maintains flow but relies on repetition/self-correction; links simple sentences but repeats; speech may be slow | limited range; adequate for topics; attempts less common items limited; errors noticeable | limited range; attempts complex forms limited; frequent errors but not impeding | shows some features but limited control; generally intelligible; some mispronunciations impede |
| 4 | cannot respond without noticeable effort; speech cannot keep going without repetition; links simple; no complex attempts | limited range; sufficient for familiar topics only; frequent word form/spelling errors | limited range; repetitive; frequent errors impede | limited; errors frequent; some unintelligible |
| 3 | simple speech; frequent pauses/repetition; links simple sentences; limited coherence | vocabulary very limited; frequent errors impede | sentence forms limited/rare; frequent errors impede | severely limited; frequent errors; often unintelligible |
| 2 | pauses before most words; little communication | vocabulary insufficient | rare sentence forms; severe errors | very limited; severe |
| 1 | no communication; no rateable language | insufficient | no rateable | no rateable |
| 0 | does not attend | — | — | — |

---

## 3. TOEIC — Listening & Reading (L&R)

### 3.1 Scale
- Score range: 10–990 (in 5-point increments).
- Reported per section (Listening 5–495, Reading 5–495) plus total.
- Proficiency levels (ETS descriptors):
  | Level | Total Score | Proficiency |
  |-------|-------------|-------------|
  | 5 | 905–990 | Advanced / International communication |
  | 4A | 785–900 | Advanced working proficiency |
  | 4 | 605–780 | High intermediate |
  | 3 | 405–600 | Intermediate |
  | 2 | 505–? (L) / — | Low intermediate |
  | 1 | 10–100 | Basic |
  | 0 | — | No score |

### 3.2 TOEIC Speaking & Writing
- Speaking: 0–200 (score bands 0–200, proficiency levels 1–8 by score ranges).
- Writing: 0–200 (score bands 0–200, proficiency levels 1–9 by score ranges).
- Can-do statements describe what test takers can do at each proficiency.

---

## 4. HSK (Hanyu Shuiping Kaoshi)

### 4.1 HSK 1–6 (legacy/current)
| Level | Vocabulary | Approx. CEFR | Approx. hours of study |
|-------|------------|--------------|------------------------|
| 1 | 150 words | A1 | 40–80 |
| 2 | 300 words | A2 | 80–160 |
| 3 | 600 words | B1 | 160–320 |
| 4 | 1,200 words | B2 | 320–480 |
| 5 | 2,500 words | C1 | 480–640 |
| 6 | 5,000+ words | C2 | 640–960 |

### 4.2 HSK 3.0 reform (rolled out from 2021)
- Reorganizes levels into "Three Steps, Nine Levels" (初等/中等/高级, 1.0–9.0).
- Vocabulary targets expand significantly (e.g., level 6.0 ≈ 5,453 words; level 9.0 ≈ 11,092 words).
- Writing & speaking integrated from mid-levels; reform timelines vary by region.
- Always flag currency: confirm which HSK version applies to the user's target.

---

## 5. CEFR — Common European Framework of Reference

### 5.1 Level descriptions (Council of Europe, 2020 Companion Volume)
| Level | Name | Can-do (global) |
|-------|------|------------------|
| A1 | Breakthrough | Recognizes basic phrases; introduces self; asks/answers simple personal questions |
| A2 | Waystage | Understands sentences/frequent expressions on familiar matters; simple direct exchange |
| B1 | Threshold | Deals with most travel situations; produces simple connected text; describes experiences |
| B2 | Vantage | Interacts with fluency/spontaneity; produces detailed text; presents viewpoints |
| C1 | Effective Operational Proficiency | Flexible/effective language use; clear well-structured detailed text; recognizes implicit meaning |
| C2 | Mastery | Understands virtually everything; summarizes from sources; expresses precisely, differentiating finer meaning |

### 5.2 Cross-exam mapping (approximate, for comparability only)
| CEFR | IELTS (approx) | TOEIC L&R (approx) | HSK (legacy) |
|------|----------------|--------------------|--------------|
| A1 | 2.0–2.5 | 60–150 | 1 |
| A2 | 3.0–3.5 | 150–300 | 2 |
| B1 | 4.0–4.5 | 300–500 | 3 |
| B2 | 5.5–6.5 | 500–780 | 4 |
| C1 | 7.0–8.0 | 785–945 | 5 |
| C2 | 8.5–9.0 | 950–990 | 6 |

> Mappings are approximate and not endorsed by the exam bodies. Always cite
> the source exam's official conversion where one exists.

---

## 6. Scoring Criteria Summary (all exams)

### IELTS Writing
See §1.1. Evidence rule: quote the specific sample span (word range or transcript
timestamp) supporting each criterion band.

### IELTS Speaking
See §2.1. Pronunciation is judged on intelligibility + use of features
(stress/intonation/rhythm), not accent.

### TOEIC
Score is item-based, not rubric-based; "scoring" here means estimating the
equivalent score band from a sample and mapping to proficiency can-do statements.

### HSK
Level is determined by passing threshold on standardized items; for samples we
estimate CEFR-equivalent level from complexity, vocabulary breadth, and grammar
control, then map to HSK level.

---

## 7. Authoritative Data Sources
| Source | URL | Use |
|--------|-----|-----|
| IELTS (Cambridge/BC/IDP) | https://www.ielts.org | Band descriptors, format |
| ETS TOEIC | https://www.ets.org/toeic | Proficiency levels, can-do |
| Chinese Testing International (HSK) | http://www.chinesetest.cn | HSK levels, 3.0 reform |
| Council of Europe CEFR | https://www.coe.int/en/web/common-european-framework-reference-languages | Level reference |
| ERIC (applied linguistics) | https://eric.ed.gov | Research on assessment |

---

## 8. Analytical Frameworks
- IELTS four-criterion rubric (Writing & Speaking) with equal weights.
- TOEIC item-score → proficiency-level → can-do statements.
- HSK vocabulary/grammar bands → CEFR → level.
- CEFR global can-do as the common comparability layer.

---

## 9. Self-Update Protocol
- **Queries:** "IELTS band descriptors update", "HSK 3.0 reform",
  "TOEIC format change", "CEFR mapping", "language assessment validity".
- **Sources:** official exam sites, CEFR, ERIC.
- **Frequency:** weekly (cron: see `tools/cron.example`).
- **Append format:** `- [DATE] Title — Source — URL <!--h:hash-->`
- **Dedupe:** 12-char SHA-1 of (url + title); skip if hash present.
- **Score & rank:** relevance-weighted by keyword overlap; keep top-N.

---

## 10. Knowledge Update Log
- [2026-06-18] Seed entry — full descriptor catalogs documented (IELTS Writing & Speaking, TOEIC, HSK 1–6 + 3.0, CEFR A1–C2, cross-exam mapping).
<!--h:seed00000000-->

```

