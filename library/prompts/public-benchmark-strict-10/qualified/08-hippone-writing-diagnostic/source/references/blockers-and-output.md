# Blockers and Output

## Concrete blocker families

Use plain learner-facing labels. Select the closest concrete pattern instead of saying only “logic,” “coherence,” “vocabulary,” or “grammar problem.”

### Task 1

- Overview missing or unclear.
- Overview misses the most important features.
- Key data comparison is absent or inaccurate.
- Trend or comparison language is imprecise.
- Data prepositions are repeatedly inaccurate.
- Tense control does not match the chart period.

### Task 2 argument and coverage

- Position drifts or becomes unclear between sections.
- One part of the prompt is not answered.
- Main idea is stated but not developed.
- Explanation repeats the claim instead of giving a reason.
- Example appears without explaining its consequence for the argument.
- Supporting example is too general to prove the point.

### Task 2 organisation

- Topic sentence does not answer the question.
- Paragraph role is unclear.
- Progression jumps between ideas.
- Connectors stack up without clarifying the relationship.
- Referencing is unclear.

### Language control

- Repeated vocabulary restricts precision.
- Collocations or word choices repeatedly distort meaning.
- Register is inappropriate for an academic response.
- Sentence-boundary errors repeatedly disrupt reading.
- Complex sentences repeatedly lose grammatical control.
- Agreement, article, preposition, or tense errors form a recurring pattern.

## Evidence rule

Every primary blocker needs at least one exact quote of 3–15 whitespace-separated words from the learner's response. Quote the smallest span that proves the pattern. Never manufacture or silently correct the quotation.

## Repair-action rule

A repair action must specify what the learner changes and the success condition, without supplying the finished wording.

Good actions:

- “Rewrite the second body paragraph's topic sentence so it directly answers the question and predicts the paragraph's reason.”
- “Add one causal step after the quoted claim: explain how it produces the stated social effect.”
- “Write a one-sentence overview naming the two largest changes without listing every number.”

Do not provide model sentences, a replacement paragraph, or a full essay.

## Optional machine-readable payload

Use this shape when deterministic validation is needed:

```json
{
  "taskNumber": 2,
  "promptProvided": true,
  "essay": "learner text",
  "wordCount": 278,
  "scores": {
    "estimatedBand": 6.5,
    "taskResponse": 6.0,
    "coherence": 6.5,
    "lexical": 6.5,
    "grammar": 6.5
  },
  "blockers": [
    {
      "criterion": "taskResponse",
      "evidenceQuote": "exact words from the learner response",
      "label": "Explanation repeats the claim",
      "learnerAction": "Describe the bounded repair the learner must write."
    }
  ]
}
```

For Task 1 use `taskAchievement` instead of `taskResponse`. Use `null` for an unassessed task criterion.
