# LR V4 locked six-anchor panel calibration v15

The candidate already has a locked final Lexical Resource score produced by V4. Do not rescore the response from scratch and do not alter the V4 score directly.

Compare the candidate independently with every supplied same-task anchor. Each anchor's LR score is locked by the program. Return one relation for every anchor:

- `above`: the candidate's complete LR performance is clearly stronger;
- `comparable`: the candidate is at approximately the same LR boundary;
- `below`: the candidate's complete LR performance is clearly weaker.

Judge the complete LR construct across the whole response:

- range and flexibility for the meanings required by this task;
- precision and successful collocational control;
- successful control of less-common vocabulary;
- objective word-choice, collocation, spelling and word-formation errors;
- stability across the response.

Necessary repetition of prompt terms, chart categories, named entities and central argument terms is neutral. Do not reward topic sophistication, specialist terminology density or idiom density. Compare Academic Task 1 language only with Academic Task 1 anchors, and Task 2 language only with Task 2 anchors.

A half-band boundary panel contains three anchors at the lower whole band and three at the upper whole band. It does not claim those essays have a half-band LR label. Compare each locked anchor at its published score; the program uses the six relations to decide whether the candidate sits below, around or above the boundary.

Return comparisons only. Do not output a score, adjustment or rewritten anchor score.
