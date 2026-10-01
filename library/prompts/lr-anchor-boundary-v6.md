# LR anchor boundary comparison v6

Assess only the candidate's successfully used vocabulary. Genuine errors and deductions are handled by a separate locked V4 stage and must not affect these comparisons.

For every supplied anchor, compare the candidate with that anchor on:

- breadth of vocabulary successfully used across the complete response;
- flexibility in expressing the task's meanings;
- precision of successfully used words and phrases;
- natural control of less-common vocabulary and collocation;
- ability to express concrete or abstract distinctions appropriate to the task.

The anchor's human LR score is a calibration boundary, not an answer to copy. Topic-specific terminology is not automatically better than ordinary precise language. Task 1 naturally uses a narrower reporting vocabulary than Task 2, so compare control relative to the task. A response does not need constant rare vocabulary to equal an LR 8 or LR 9 anchor.

For each anchor, return exactly one decision:

- `below`: the candidate's successful lexical performance is clearly weaker;
- `comparable`: it is at the same practical boundary despite differences in topic or style;
- `above`: it is clearly stronger.

Do not use lexical mistakes, repetition, spelling, awkward expressions or possible rewrites to select `below`; those belong to the later V4 deduction stage. Base every decision on positive performance and quote evidence from both texts. Compare every supplied anchor independently.
