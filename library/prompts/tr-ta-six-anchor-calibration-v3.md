# TR/TA staged six-anchor calibration v3

Date: 2026-09-25

This is a development calibration layer applied after the selected original
TR/TA prompt has independently produced and locked a score. It does not replace
that prompt.

## Evidence before score

First build a criterion-only evidence card without using the locked score,
original rationale, anchor labels, or human label.

For Academic Task 1 TA, record:

- whether the main trends, dominant differences, major stages and turning
  points can be understood from the response as a whole;
- coverage of the principal series, categories or stages;
- key comparisons and sufficient supporting figures;
- inaccuracies classified as dominant-feature, key-feature or detail-level.

An overview is judged across the whole response. A missing phrase in the
labelled `Overall` sentence is not by itself a band ceiling when the response
clearly groups and reports the main contrasting trends elsewhere. A wrong
dominant trend, omitted major series/stage or serious misstatement of the main
relationship is a blocking defect. One minor datum/detail problem is not a
blocking defect; two independent minor datum/detail problems together can
support at most a 0.5 lower location. Repeated manifestations of one content
problem count once.

For Task 2 TR, record:

- coverage of every prompt part and clarity/consistency of position;
- each core claim separately;
- for each core claim, whether the why/how link can be followed and whether it
  has explanation, mechanism, consequence, comparison or example;
- unclear, irrelevant or unsupported core reasoning.

Addressing the prompt, stating a position, listing two reasons or mentioning an
opposing view are necessary evidence only. They do not by themselves prove a
higher band. A formal rebuttal cannot compensate for two unclear or
insufficiently supported core arguments. To cross from 6.0 to 6.5, most core
arguments must be adequately developed and no two core arguments may both have
materially unclear why/how links.

## Anchor cells

Each tested score position contains exactly six same-task references.

- Integer positions contain six references with an explicit human TA/TR score
  at that integer.
- Because the official public descriptors define integer criterion bands, a
  half-band position is an operational boundary cell: three explicit lower
  integer anchors and three explicit upper integer anchors. It is not described
  as an official half-band descriptor.
- A teacher's explicit half-band TA/TR rating may be retained as supplementary
  evidence, but an overall score never substitutes for a TA/TR rating.
- Test essays, duplicates and interval-only ratings are excluded.

Compare the candidate with every anchor independently on TA/TR content only.
Ignore CC, LR and GRA. Do not average scores, take a median or let a single
anchor decide the result.

For Task 2 cells at 8.5 or 9.0, absence of a concrete example, shorter response
length, fewer supporting points, or less elaboration than an anchor is not by
itself a TR content defect and cannot by itself justify `below`. A `below`
judgment in those cells must identify a specific candidate-side deficiency in
prompt coverage, position, relevance, or a core claim's why/how reasoning,
mechanism, consequence, support or evaluation. Words such as `general`,
`example-free`, `shorter` or `less detailed` do not identify such a deficiency
on their own. This restriction does not alter the ordinary comparison standard
for cells from 6.0 through 8.0.

## Cell decision

For each six-anchor cell, output candidate `below`, `comparable` or `above`
relative to every reference.

- The candidate passes a cell when at least four of six comparisons are
  `comparable` or `above`.
- A cell cannot pass if the same material blocking defect is confirmed in at
  least two comparisons.
- The candidate clearly exceeds a cell when at least five of six comparisons
  are `comparable` or `above`, including at least three `above`.
- Cell results must be monotonic from low to high. Recheck only conflicting
  comparisons once. If the conflict remains, retain the locked score.

## Staged search range

The first stage tests only positions within 1.0 of the locked original score.
The initial upper boundary is expanded by one 0.5 cell when at least five of its
six comparisons are `comparable` or `above` and it has no blocking defect.
After expansion, a passing new cell may become the final score. Continue to the
next higher 0.5 cell only when the current new cell again has at least five of
six `comparable` or `above` and no blocking defect. Stop at the first failed
cell, at the first cell with fewer than five `comparable` or `above`, at Band
9.0, or at +2.0 from the locked score.

Use the symmetric rule for downward expansion: at least five of six comparisons
must be `below` and the cell must have no blocking defect. Stop at Band 6.0 or
at -2.0 from the locked score. A later stage receives only the newly opened
cell; higher or lower anchors must not influence the initial comparisons.

Moves remain sequential. A candidate cannot cross a failed intermediate cell.
If the candidate clearly exceeds the locked-score cell and passes the +0.5
cell, it must move at least +0.5 rather than defaulting to the centre.

The locked evidence card also applies these movement and eligibility gates:

- Task 1 cannot move upward when it repeatedly misidentifies the measured
  outcome, unit, time period or a principal category, even if four anchor
  comparisons otherwise pass.
- Task 2 cannot move upward when the evidence card contains two or more
  independent key content defects in prompt coverage, position or core-argument
  development. Merely mentioning the relevant topics does not clear this gate.
- A Task 2 candidate with zero blocking defects, zero key defects and no more
  than one detail defect is eligible to enter the 8.5 and 9.0 cells. This is an
  eligibility rule, not an automatic pass. Absence of examples or relative
  brevity cannot be promoted to a key defect by itself.
