# GRA locked-base panel6 short contract v4

This is a Stage 2 comparison method. Stage 1 has already independently scored
GRA and its score is immutable. Stage 2 may retain that score or move it upward
by 0.5 or 1.0; it may never lower it or move it by more than one band.

Assess GRA only across four dimensions:

1. structural range and flexibility;
2. frequency of error-free sentences;
3. grammar and punctuation control;
4. impact of errors on communication.

Use the IELTS Writing GRA integer-band descriptors as the standard. A half
band is only an operational boundary: its panel contains three same-task
essays from the lower integer and three from the upper integer. An integer
panel contains six same-task essays at that integer GRA label. Compare the
candidate with the pattern across all six essays, not with one convenient
anchor.

Repeated instances of one underlying error are evidence of its frequency, not
independent reasons to deduct repeatedly. Do not count lexical awkwardness,
task fulfilment, cohesion, topic sophistication, teacher identity, source
reputation, or any overall score as GRA evidence.

Retain when evidence is mixed or insufficient. A +0.5 proposal requires at
least two of the four dimensions to cross the next half-band boundary. A +1.0
proposal requires at least three dimensions to match the full-band target and
explicit confirmation that the intervening boundary is crossed.

The output contract is intentionally comparison-only. For each panel, return
its overall relation and the relation plus concise evidence for all four GRA
dimensions. Do not return candidate identifiers, the locked base, target
panel bands, anchor identifiers, an adjustment, a boundary flag,
supporting-dimension lists, or a final score. The runner binds and derives all
of those values after strict validation.

The deterministic runner gate is: the first panel passes with an overall
`matches`/`above` relation and at least two dimensions at `matches`/`above`;
the second passes with an overall `matches`/`above` relation, at least three
such dimensions, and the first panel must also pass its own gate. The highest
passing panel determines the upward adjustment. The scorer does not choose the
adjustment.
