# LR/GRA capped composite v2

Date: 2026-09-24

Score only Lexical Resource and Grammatical Range and Accuracy.

## Mandatory score procedure

### Lexical Resource

1. First determine the provisional LR band from the successful vocabulary range, flexibility, precision and ability to express the task's meanings.
2. Then consider repetition, awkward collocation, word choice, spelling and word formation.
3. Necessary repetition of topic words is not a fault.
4. Repetition or an unnatural collocation that remains immediately understandable may lower the provisional LR score by **no more than 0.5 band in total**.
5. These issues may lower LR by as much as **1.0 band only when they form a repeated pattern that clearly restricts expression or repeatedly causes difficulty in understanding**.
6. A phrase that could merely be made more elegant does not lower LR.

### Grammatical Range and Accuracy

1. First determine the provisional GRA band from successful sentence-range evidence and the control shown in the response.
2. Then consider actual grammar and punctuation errors.
3. Grammar errors that do not affect understanding may lower the provisional GRA score by **no more than 0.5 band in total**, regardless of their raw count.
4. Grammar errors may lower GRA by as much as **1.0 band only when the same weakness is clearly systematic or errors repeatedly affect understanding**.
5. Do not infer a low error-free-sentence rate merely because several correctable errors can be found. Judge the response sentence by sentence and across the whole essay.

### No double counting

An issue has one primary home. Collocation, word choice and lexical naturalness belong to LR. Count an issue under GRA only when a specific grammar or punctuation rule is violated. Never lower both scores for the same issue.

Return both the provisional score and the final capped score. The final score must be on the IELTS half-band scale.

## LR source package: dungnotnull

Use the source below only for LR, subject to the mandatory cap above.


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


## GRA source package: quyen244

Use the source below only for GRA, subject to the mandatory cap above.


### Original file: `library/prompts/public-benchmark-strict-10/qualified/04-quyen244-ai-evaluator/source/src/llm/prompts/builders.py`

```text
"""Prompt construction for every LLM node.

See docs/02-technical/prompt-engineering.md for the reasoning behind each element.
Bump PROMPT_VERSION on any content change, then re-run the benchmark.
"""

from __future__ import annotations

from src.core.schemas import CRITERION_NAMES, ExamItem, ScoredCriterion, TextFeatures
from src.llm.rubrics.rubrics import get_rubric

PROMPT_VERSION = "prompt-v1.0"

TASK_LABEL = {
    "task1": "IELTS Academic Writing Task 1 (data/process report)",
    "task2": "IELTS Writing Task 2 (argumentative essay)",
}


def format_features(f: TextFeatures) -> str:
    repeated = (
        ", ".join(f"{w}({n})" for w, n in f.repeated_content_words) or "none detected"
    )
    devices = ", ".join(f.cohesive_devices_found) or "none detected"
    length_flag = "MEETS minimum" if f.meets_min_words else "BELOW minimum"
    return (
        f"- Word count: {f.word_count} (minimum required: {f.min_words_required}) — {length_flag}\n"
        f"- Paragraphs: {f.paragraph_count} | Sentences: {f.sentence_count} | "
        f"Average sentence length: {f.avg_sentence_length:.1f} words\n"
        f"- Unique words: {f.unique_words} | Type-token ratio: {f.type_token_ratio:.2f}\n"
        f"- Most repeated content words: {repeated}\n"
        f"- Cohesive devices detected: {devices}"
    )


# --------------------------------------------------------------------------- #
# Criterion evaluation
# --------------------------------------------------------------------------- #
CRITERION_SYSTEM = (
    "You are a certified IELTS Writing examiner with over ten years of experience "
    "assessing {task_label}. You apply the official band descriptors strictly and "
    "consistently. You are neither lenient nor harsh — you are accurate. You are "
    "willing to award low bands to weak work and high bands to strong work; "
    "defaulting everything to the middle of the scale is the worst mistake an "
    "examiner can make."
)

CRITERION_USER = """## CRITERION UNDER ASSESSMENT
{criterion_name} ({criterion_code}) — assess THIS CRITERION ONLY.

## OFFICIAL BAND DESCRIPTORS
{rubric}

## EXAM PROMPT
{exam_prompt}
{chart_block}
## STUDENT ESSAY
<<<ESSAY
{essay}
ESSAY

## OBJECTIVE TEXT STATISTICS
These were computed programmatically. Treat them as ground truth and do not re-count.
{features}

## WHAT TO PRODUCE
1. `justification` — 3 to 5 sentences in English. Name the band descriptor the essay
   matches and explain why it matches that one rather than the band above or below.
   Write this BEFORE you decide on a number.
2. `band` — a number from 1.0 to 9.0 in steps of 0.5, consistent with your justification.
3. `evidence` — 2 to 4 items. Each `quote` MUST be copied character-for-character from
   between the ESSAY markers above.
4. `strengths`, `weaknesses`, `improvements` — concise English bullet points.
5. `confidence` — 0.0 to 1.0.

## RULES
- Never invent a quote. If you cannot find an exact supporting quote, leave that
  evidence item out rather than paraphrasing or correcting the student's words.
- Assess {criterion_code} only. Ignore problems that belong to other criteria.
- Use the word count given above; do not count words yourself.
{length_rule}"""

LENGTH_RULE_SCORED = (
    "- Do NOT deduct marks for the essay being under the word limit. Length is "
    "handled separately by the scoring system, and deducting here would penalise "
    "the student twice."
)
LENGTH_RULE_OTHER = (
    "- Ignore essay length entirely; it is not part of this criterion."
)


def build_criterion_messages(
    exam: ExamItem, criterion: str, features: TextFeatures
) -> list[dict[str, str]]:
    chart_block = ""
    if exam.task_type == "task1" and exam.chart_description:
        chart_block = (
            "\n## SOURCE DATA SHOWN IN THE VISUAL\n"
            "Use this to check whether the student reported the figures accurately.\n"
            f"{exam.chart_description}\n"
        )

    is_task_criterion = criterion in ("TA", "TR")
    return [
        {
            "role": "system",
            "content": CRITERION_SYSTEM.format(task_label=TASK_LABEL[exam.task_type]),
        },
        {
            "role": "user",
            "content": CRITERION_USER.format(
                criterion_name=CRITERION_NAMES[criterion],
                criterion_code=criterion,
                rubric=get_rubric(exam.task_type, criterion),
                exam_prompt=exam.prompt.strip(),
                chart_block=chart_block,
                essay=exam.essay.strip(),
                features=format_features(features),
                length_rule=LENGTH_RULE_SCORED if is_task_criterion else LENGTH_RULE_OTHER,
            ),
        },
    ]


# --------------------------------------------------------------------------- #
# Sentence corrector
# --------------------------------------------------------------------------- #
CORRECTOR_SYSTEM = (
    "You are an IELTS writing tutor who corrects student work. Your corrections are "
    "minimal and surgical: you fix what is wrong and leave the student's own voice "
    "and ideas intact. You explain in Vietnamese because your students are Vietnamese."
)

CORRECTOR_USER = """## STUDENT ESSAY
<<<ESSAY
{essay}
ESSAY

## TASK
Identify at most {max_issues} sentence-level problems, ordered by how much each one
damages the band score — most damaging first.

For each issue:
- `original`: the problematic text, copied character-for-character from between the
  ESSAY markers. Never paraphrase it.
- `corrected`: the same text with the problem fixed and nothing else changed.
- `error_types`: one or more of grammar, agreement, tense, article, word choice,
  collocation, word form, spelling, punctuation, capitalisation.
- `impact`: negligible / minor / moderate / major / critical.
- `explanation_vi`: a short explanation IN VIETNAMESE of what was wrong and why the
  correction is better.

## RULES
- Prioritise errors that affect accuracy or meaning over matters of style.
- If the same error pattern recurs, report it at most twice and raise its `impact`
  instead of listing every instance.
- If the essay has fewer than {max_issues} genuine problems, return fewer items.
  Do not invent errors to fill the list."""


def build_corrector_messages(essay: str, max_issues: int) -> list[dict[str, str]]:
    return [
        {"role": "system", "content": CORRECTOR_SYSTEM},
        {
            "role": "user",
            "content": CORRECTOR_USER.format(essay=essay.strip(), max_issues=max_issues),
        },
    ]


# --------------------------------------------------------------------------- #
# Feedback synthesiser
# --------------------------------------------------------------------------- #
SYNTH_SYSTEM = (
    "You are an IELTS coach writing to a Vietnamese student. You are direct, "
    "specific and encouraging. You never give vague advice such as 'improve your "
    "vocabulary' — you say exactly which words, which sentences, and what to do instead."
)

SYNTH_USER = """## ASSESSMENT ALREADY COMPLETED
Overall band: {overall}

{criteria_block}

## TOP SENTENCE-LEVEL ISSUES
{issues_block}

## TASK
Write the student's feedback in VIETNAMESE.

- `summary_vi`: 3 to 5 sentences. State honestly where the student stands, what is
  genuinely working, and what is holding the score down.
- `priority_actions`: EXACTLY 3 actions, ordered by how much band improvement each
  would produce. Each needs `action` (imperative, specific), `criterion` (the code
  it targets), `expected_gain` (e.g. "+0.5 LR"), and `example` — a concrete example
  taken from the analysis above, not a generic one.
- `next_band_gap`: what specifically stands between this student and the next half band.

## RULES
- Base everything on the analysis above. Do not invent new errors or new quotes.
- Do not contradict the bands that have already been awarded."""


def build_synthesizer_messages(
    overall: float,
    criteria: dict[str, ScoredCriterion],
    issues: list,
) -> list[dict[str, str]]:
    parts = []
    for code, c in criteria.items():
        band = "n/a" if c.band is None else f"{c.band}"
        parts.append(
            f"### {code} — Band {band}\n"
            f"Justification: {c.justification}\n"
            f"Strengths: {'; '.join(c.strengths) or 'none recorded'}\n"
            f"Weaknesses: {'; '.join(c.weaknesses) or 'none recorded'}\n"
            f"Suggested improvements: {'; '.join(c.improvements) or 'none recorded'}"
        )
    criteria_block = "\n\n".join(parts)

    if issues:
        issues_block = "\n".join(
            f"- [{i.impact}] \"{i.original}\" -> \"{i.corrected}\" ({', '.join(i.error_types)})"
            for i in issues[:6]
        )
    else:
        issues_block = "None recorded."

    return [
        {"role": "system", "content": SYNTH_SYSTEM},
        {
            "role": "user",
            "content": SYNTH_USER.format(
                overall=overall,
                criteria_block=criteria_block,
                issues_block=issues_block,
            ),
        },
    ]

```

### Original file: `library/prompts/public-benchmark-strict-10/qualified/04-quyen244-ai-evaluator/source/src/llm/rubrics/rubrics.py`

```text
"""Compressed IELTS band descriptors, bands 4-9.

These are paraphrased and condensed from the public IELTS Writing band descriptors.
Compression preserves the *discriminating keywords* between adjacent bands, because
those are what let the model tell a 6 from a 7. Compressing those away is how you
end up with a model that scores everything 6.5.

This file is DATA. Editing it should not require touching pipeline code, and every
edit must be followed by a benchmark run (see docs/03-evaluation/evaluation-protocol.md).
"""

from __future__ import annotations

RUBRIC_VERSION = "rubric-v1.0"

TASK1_TA = """\
Band 9: Fully satisfies all requirements. Presents a clear, fully developed overview and accurate key features.
Band 8: Covers all requirements sufficiently. Presents a clear overview; key features are well selected and highlighted.
Band 7: Covers the requirements. Presents a CLEAR OVERVIEW of main trends/differences/stages. Key features are highlighted, but details may be inadequate or occasionally irrelevant.
Band 6: Addresses the requirements. Presents an overview WITH INFORMATION APPROPRIATELY SELECTED. Some key features are covered but details may be irrelevant, inappropriate or inaccurate.
Band 5: Generally addresses the task but format may be inappropriate. RECOUNTS DETAIL MECHANICALLY WITH NO CLEAR OVERVIEW. There may be no data to support the description.
Band 4: Attempts the task but does not cover all key features; format may be inappropriate. May confuse key features with detail; parts may be unclear, irrelevant, repetitive or inaccurate.

DISCRIMINATOR: the single strongest signal separating Band 5 from Band 6+ is the
presence of a genuine OVERVIEW that summarises main features, rather than a
mechanical recount of every data point."""

TASK2_TR = """\
Band 9: Fully addresses all parts. Presents a fully developed position with relevant, fully extended, well-supported ideas.
Band 8: Sufficiently addresses all parts. Presents a well-developed response with relevant, extended and supported ideas.
Band 7: Addresses all parts, though some parts may be more fully covered than others. Presents a CLEAR POSITION THROUGHOUT. Presents, extends and supports main ideas, but there may be a tendency to over-generalise or supporting ideas may lack focus.
Band 6: Addresses all parts although some parts may be more fully covered than others. Presents a RELEVANT POSITION although conclusions may become unclear or repetitive. Presents relevant main ideas but some may be inadequately developed or unclear.
Band 5: Addresses the task only PARTIALLY; format may be inappropriate in places. Expresses a position but the development is not always clear. Presents some main ideas but these are limited and not sufficiently developed; there may be irrelevant detail.
Band 4: Responds to the task only in a minimal way or the answer is tangential; format may be inappropriate. Presents a position but this is unclear. Presents some main ideas but these are difficult to identify and may be repetitive, irrelevant or not well supported.

DISCRIMINATOR: Band 6 vs 7 turns on whether the position is CLEAR AND CONSISTENT
throughout, and whether main ideas are EXTENDED (developed with reasoning/examples)
rather than merely stated."""

CC = """\
Band 9: Uses cohesion in such a way that it attracts no attention. Skilfully manages paragraphing.
Band 8: Sequences information and ideas logically. Manages all aspects of cohesion well. Uses paragraphing sufficiently and appropriately.
Band 7: Logically organises information and ideas; there is CLEAR PROGRESSION throughout. Uses a range of cohesive devices appropriately although there may be some under-/over-use. Presents a clear central topic within each paragraph.
Band 6: Arranges information and ideas coherently and there is a clear overall progression. Uses cohesive devices EFFECTIVELY, but cohesion within and/or between sentences may be faulty or MECHANICAL. May not always use referencing clearly or appropriately.
Band 5: Presents information with some organisation but there may be a LACK OF OVERALL PROGRESSION. Makes INADEQUATE, INACCURATE OR OVER-USE of cohesive devices. May be repetitive because of lack of referencing and substitution.
Band 4: Presents information and ideas but these are not arranged coherently and there is no clear progression. Uses some basic cohesive devices but these may be inaccurate or repetitive. May not write in paragraphs or paragraphing may be inadequate.

DISCRIMINATOR: Band 6 typically shows MECHANICAL connectors (Firstly/Secondly/
Finally used as scaffolding). Band 7+ shows cohesion arising from logical sequencing
and referencing, with connectors used selectively rather than formulaically."""

LR = """\
Band 9: Uses a wide range of vocabulary with very natural and sophisticated control of lexical features; rare minor errors occur only as slips.
Band 8: Uses a WIDE RANGE of vocabulary fluently and flexibly to convey precise meanings. Skilfully uses uncommon lexical items but there may be occasional inaccuracies in word choice and collocation.
Band 7: Uses a SUFFICIENT RANGE of vocabulary to allow some FLEXIBILITY AND PRECISION. Uses less common lexical items with some awareness of style and collocation. May produce occasional errors in word choice, spelling and/or word formation.
Band 6: Uses an ADEQUATE range of vocabulary for the task. ATTEMPTS to use less common vocabulary but WITH SOME INACCURACY. Makes some errors in spelling and/or word formation, but they do not impede communication.
Band 5: Uses a LIMITED range of vocabulary, but this is minimally adequate for the task. May make noticeable errors in spelling and/or word formation that may cause SOME DIFFICULTY for the reader.
Band 4: Uses only BASIC vocabulary which may be used repetitively or which may be inappropriate for the task. Has limited control of word formation and/or spelling; errors may cause strain for the reader.

DISCRIMINATOR: Band 6 ATTEMPTS less common vocabulary and gets it partly wrong.
Band 7 USES less common vocabulary with awareness of collocation. Band 8 uses it
with PRECISION and natural style. Heavy repetition of content words is a Band 5-6 signal."""

GRA = """\
Band 9: Uses a wide range of structures with full flexibility and accuracy; rare minor errors occur only as slips.
Band 8: Uses a WIDE RANGE of structures. The MAJORITY OF SENTENCES ARE ERROR-FREE. Makes only very occasional errors or inappropriacies.
Band 7: Uses a VARIETY OF COMPLEX STRUCTURES. Produces FREQUENT ERROR-FREE SENTENCES. Has good control of grammar and punctuation but may make a few errors.
Band 6: Uses a MIX of simple and complex sentence forms. Makes SOME ERRORS IN GRAMMAR AND PUNCTUATION but they RARELY REDUCE COMMUNICATION.
Band 5: Uses only a LIMITED RANGE of structures. ATTEMPTS complex sentences but these tend to be less accurate than simple sentences. May make frequent grammatical errors and punctuation may be faulty; errors CAN CAUSE SOME DIFFICULTY for the reader.
Band 4: Uses only a very limited range of structures with only rare use of subordinate clauses. Some structures are accurate but errors PREDOMINATE, and punctuation is often faulty.

DISCRIMINATOR: count error-free sentences. Band 6 = errors are frequent but harmless.
Band 7 = frequent error-free sentences with a few slips. Band 8 = the MAJORITY of
sentences are completely error-free. Systematic subject-verb agreement or tense
failures across the whole text indicate Band 5 or below."""

_RUBRICS: dict[tuple[str, str], str] = {
    ("task1", "TA"): TASK1_TA,
    ("task2", "TR"): TASK2_TR,
    ("task1", "CC"): CC,
    ("task2", "CC"): CC,
    ("task1", "LR"): LR,
    ("task2", "LR"): LR,
    ("task1", "GRA"): GRA,
    ("task2", "GRA"): GRA,
}


def get_rubric(task_type: str, criterion: str) -> str:
    try:
        return _RUBRICS[(task_type, criterion)]
    except KeyError as exc:
        raise KeyError(f"No rubric for {task_type}/{criterion}") from exc

```

### Original file: `library/prompts/public-benchmark-strict-10/qualified/04-quyen244-ai-evaluator/source/docs/02-technical/prompt-engineering.md`

```text
# Prompt Engineering Specification

---

## 1. Bảy nguyên tắc

### P1 — Một prompt, một nhiệm vụ
Không có prompt nào chấm quá một tiêu chí. Prompt gộp làm ba việc tệ cùng lúc: tràn context, không đo được lỗi thuộc tiêu chí nào, và khiến model "kéo" điểm các tiêu chí về giống nhau (halo effect).

### P2 — Bằng chứng khách quan đi trước phán xét
Mọi prompt chấm điểm đều được inject `TextFeatures` đã tính bằng code:
```
OBJECTIVE TEXT STATISTICS (computed programmatically — treat as ground truth):
- Word count: 287 (minimum required: 250) ✓
- Paragraphs: 4 | Sentences: 16 | Avg sentence length: 17.9 words
- Type-token ratio: 0.58 | Unique words: 166
- Most repeated content words: exploration(6), government(5), money(4)
- Cohesive devices found: however, as a result, on the one hand, in conclusion
```
Model 4B đếm từ sai thường xuyên. Đưa sẵn số đếm đúng loại bỏ hẳn một lớp lỗi thay vì hy vọng model làm đúng.

### P3 — Rubric anchoring hiển ngôn
Prompt chứa band descriptor của **đúng tiêu chí đang chấm**, band 4 → 9, viết ngắn gọn để không nuốt context. Không có neo, model 4B dồn mọi bài về band 6–6.5 (central tendency bias). Rubric là **dữ liệu** trong `src/llm/rubrics/`, không phải chuỗi hardcode trong Python.

### P4 — `justification` trước `band`
Xem [data-schemas.md § 3](data-schemas.md#3-llm-output-contract). Đây là cơ chế thay thế cho `think=True` đã tắt.

### P5 — Trích dẫn nguyên văn, không diễn giải
```
Every `quote` MUST be copied character-for-character from the essay.
Do NOT paraphrase, correct, or shorten it. If you cannot find an exact
supporting quote, omit that evidence item rather than inventing one.
```
Bổ trợ bằng `QuoteVerifier` phía code — chỉ dặn trong prompt là không đủ.

### P6 — Ngôn ngữ có chủ đích
Phân tích kỹ thuật bằng **tiếng Anh** (thuật ngữ IELTS chuẩn, model quen hơn). Giải thích cho học viên bằng **tiếng Việt**. Đánh dấu rõ trong prompt field nào dùng ngôn ngữ nào, nếu không model sẽ trộn lẫn.

### P7 — Structured output là tầng runtime, không phải lời cầu xin trong prompt
Ta truyền JSON Schema qua tham số `format` của Ollama (constrained decoding). Prompt vẫn nhắc ngắn gọn về ngữ nghĩa các field, nhưng **không** phải viết "Return ONLY valid JSON, no markdown, no prose!!!" — runtime đã lo hình dạng; prompt chỉ lo nội dung.

---

## 2. Cấu trúc chuẩn của một prompt chấm tiêu chí

```text
[SYSTEM]
You are a certified IELTS Writing examiner with 10+ years of experience
assessing {task_label}. You apply the official band descriptors strictly
and consistently. You are neither lenient nor harsh — you are accurate.

[USER]
## CRITERION UNDER ASSESSMENT
{criterion_full_name} ({criterion_code})

## OFFICIAL BAND DESCRIPTORS
{rubric_text}                       ← từ src/llm/rubrics/

## EXAM PROMPT
{exam_prompt}
{chart_description}                 ← chỉ Task 1

## STUDENT ESSAY
<<<ESSAY
{essay}
ESSAY

## OBJECTIVE TEXT STATISTICS (computed programmatically — ground truth)
{features_block}

## YOUR TASK
1. Write `justification`: 3–5 sentences in English explaining which band
   descriptor the essay matches and why. Reference the descriptors explicitly.
2. Then assign `band` (1.0–9.0, multiples of 0.5) consistent with (1).
3. Provide 2–4 `evidence` items. Each `quote` MUST be copied verbatim
   from the essay between the ESSAY markers.
4. List `strengths`, `weaknesses`, and `improvements` (English, concise).
5. `confidence`: 0.0–1.0, how certain you are of this band.

## CRITICAL RULES
- Never invent a quote. Omit an evidence item rather than fabricate it.
- Do not assess other criteria — only {criterion_code}.
- Use the word count given above; do not re-count.
```

**Dấu phân định `<<<ESSAY … ESSAY`** không phải trang trí: nó ngăn nội dung bài viết của học viên bị đọc như chỉ dẫn (prompt injection ngẫu nhiên — thí sinh hoàn toàn có thể viết một câu trông giống mệnh lệnh) và cho model một mốc rõ ràng để trích dẫn nguyên văn.

---

## 3. Rubric compression

Band descriptor chính thức của IELTS rất dài. Nhồi cả bốn tiêu chí × 9 band vào prompt sẽ ngốn ~4000 token. Chiến lược:

| Cách | Token | Dùng khi |
| --- | --- | --- |
| Full official text | ~1000/tiêu chí | Không dùng ở P0 |
| **Compressed band 4–9, 2–3 dòng/band** | **~250/tiêu chí** | **P0 hiện tại** |
| Compressed + 2 few-shot anchor essay | ~900/tiêu chí | P1 |

Bản nén giữ đúng **các từ khoá phân biệt band** (ví dụ LR: *"limited"* B4 → *"adequate but limited"* B5 → *"sufficient, some less common"* B6 → *"sufficient flexibility and precision"* B7 → *"wide resource, skilful"* B8). Nén sai các từ khoá này là làm hỏng khả năng phân biệt band của model.

---

## 4. Prompt versioning

Mỗi prompt module khai báo:
```python
PROMPT_VERSION = "criterion-v1.0"
```
`PROMPT_VERSION` đi vào `RunTelemetry` và (P1) vào cột `prompt_version` của DB. Quy tắc: **đổi nội dung prompt → bump version → chạy lại `run_eval` → so `metrics.json`.** Không có ngoại lệ. Sửa prompt mà không đo là thay đổi mù.

| Version | Thay đổi | MAE_overall |
| --- | --- | --- |
| `criterion-v1.0` | Baseline P0: rubric nén + features + justification-first | xem [Baseline Report](../03-evaluation/mvp-baseline-report.md) |

---

## 5. Anti-pattern đã loại bỏ khỏi codebase cũ

| Anti-pattern (bản cũ) | Vấn đề | Đã thay bằng |
| --- | --- | --- |
| `[PASTE ESSAY HERE]` trong `synonyms_paraphrase.py` | Placeholder thủ công, không phải template variable → prompt gửi đi với chữ literal đó | `{essay}` template variable |
| Ví dụ JSON dùng nháy đơn (`'correct sentence'`) trong `vocab_suggestion.py` | Không phải JSON hợp lệ; dạy model sinh JSON sai | JSON Schema qua `format=` |
| Tên field có khoảng trắng: `'level_impact '` | Trailing space → parse ra key sai | Pydantic field name |
| Output là **Markdown table** trong string (`vocab_table_analysis`) | Không parse được về dữ liệu; không tính metric được; không lưu DB được | `list[Evidence]` có cấu trúc |
| Rubric tiếng Việt trộn tiếng Anh trong cùng band descriptor | Model phải dịch trước khi so khớp → nhiễu | Rubric tiếng Anh, giải thích tiếng Việt tách riêng |
| Không có neo rubric (chỉ "act as examiner") | Central tendency bias, mọi bài ~6.0 | Band descriptor 4–9 hiển ngôn |
| Không kiểm chứng trích dẫn | Feedback bịa đặt không bị phát hiện | `QuoteVerifier` + metric |

---

## 6. Prompt cho Sentence Corrector

Điểm khác biệt: cần **giới hạn số lượng** và **ưu tiên theo tác động**.

```text
Identify at most {max_issues} sentence-level problems, ordered by how much
they damage the band score (most damaging first). Prefer errors that affect
meaning or accuracy over stylistic preferences. Do not list the same error
pattern more than twice — instead note it once and mark impact accordingly.
```

Không có giới hạn này, bài band 4 sinh ra 40 issue và người học không biết bắt đầu từ đâu — feedback quá tải cũng vô dụng như không có feedback.

---

## 7. Prompt cho Feedback Synthesizer

Node này **không nhận lại essay gốc**. Nó chỉ nhận `CriterionResult` đã cấu trúc + `SentenceIssue` đã lọc. Ba lý do:
1. Tiết kiệm ~400 token/call.
2. Ép model tổng hợp từ phân tích đã có thay vì chấm lại từ đầu (sẽ mâu thuẫn với band đã chốt).
3. Không thể bịa quote mới vì không có văn bản gốc để bịa từ đó.

Yêu cầu đầu ra: đúng **3** `priority_actions`, sắp theo `expected_gain` giảm dần, mỗi action phải có `example` lấy từ `weaknesses`/`sentence_issues` đã có.

```

