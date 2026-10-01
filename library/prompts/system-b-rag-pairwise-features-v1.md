# System B: System A + lexical and grammar feature report

Run the same blind rubric and pairwise procedure as System A. In addition, use
the machine-generated feature report as descriptive evidence. Features are
diagnostic signals, never automatic band rules: a high type-token ratio does not
prove Band 8 vocabulary, and a grammar-tool flag does not prove an error.

## Additional checks

- Check length, sentence count, sentence-length distribution, repeated words,
  lexical diversity, and discourse/connective markers.
- Check repeated n-grams, article/subject-verb patterns, punctuation patterns,
  and clause markers. Inspect every flagged example in context.
- Distinguish a real error from an uncommon but acceptable construction,
  spelling variation, a task-specific term, and a stylistic choice.
- Report tool availability. If no parser or grammar checker is installed, do not
  invent a grammatical error count; use the heuristic report only to select text
  for manual inspection.

The final JSON must contain the System A fields plus:

```json
{
  "feature_report": {
    "word_count": 0,
    "sentence_count": 0,
    "avg_sentence_length": 0.0,
    "lexical_ttr": 0.0,
    "repeated_content_words": [],
    "connective_markers": {},
    "clause_marker_count": 0,
    "heuristic_flags": [],
    "grammar_tool": {"name": "none", "available": false, "flags": []}
  },
  "feature_use_notes": []
}
```
