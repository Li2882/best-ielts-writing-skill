# TR/TA local-anchor calibration v1

Date: 2026-09-25

This layer calibrates, but does not replace, the locked score produced by the
selected original TR/TA prompt (`composite-best-traits-v1`, routed to
`04-quyen244-ai-evaluator`).

## Method

1. Treat the locked original score and reason as the centre of judgement.
2. Compare the candidate only with local reference positions at centre -1.0,
   centre -0.5, centre +0.5 and centre +1.0, where available.
3. Score only TA/TR content. Ignore LR, GRA and CC.
4. Do not average anchor scores, take a median, count votes, or let a distant
   anchor independently re-score the candidate.
5. Select only one of: centre -1.0, centre -0.5, centre, centre +0.5, centre
   +1.0. Prefer the centre unless the local comparisons clearly locate the
   candidate elsewhere.

For a real anchor, compare against its locked human TA/TR score. If an exact
half-band anchor is unavailable, a `boundary_proxy` contains one lower and one
upper integer anchor. Use it only to judge whether the candidate lies near or
across that boundary; do not invent a half-band label for either essay.

Task 1 comparison: overview, dominant features/stages, coverage, key
comparisons and accuracy of information supporting the main trends.

Task 2 comparison: prompt coverage, position, relevance, and whether main
claims have sufficient reasoning, explanation, mechanism, consequence,
comparison or example.

## Local positioning

- Keep the centre when the candidate is clearly between the lower-half and
  upper-half positions or when comparisons conflict.
- Move +0.5 when the candidate is broadly comparable to the +0.5 position but
  remains weaker than +1.0.
- Move +1.0 only when it is broadly comparable to the +1.0 position.
- Move -0.5 when it is weaker than the -0.5 position but stronger than -1.0.
- Move -1.0 only when it is broadly comparable to, or weaker than, -1.0.
- A possible extra example, extra detail or more elegant overview cannot by
  itself justify movement.
- A material missing prompt part, wrong dominant trend, unclear position, or
  genuinely insufficient main-idea development can justify downward location.

Each slot includes a primary reference and may include a backup. Judge the
primary first. Consult the backup only when the primary comparisons produce a
non-monotonic or genuinely ambiguous location. If the backup does not resolve
the conflict, keep the locked centre.

Return JSON only. Explain the local comparisons, but do not reproduce an
independent full-band scoring process.
