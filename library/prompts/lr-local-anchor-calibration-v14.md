# LR local anchor calibration v14

This is the second stage of IELTS Lexical Resource scoring. The candidate has already received an independent initial LR score from the selected LR scoring prompt. Do not redo that scoring from scratch.

Compare the candidate separately with every supplied anchor. All anchors are from the same IELTS Writing task type. Their scores are locked by the program and must not be copied, changed, inferred, or re-labelled in the output.

For each anchor, output one decision describing the candidate relative to that anchor:

- `above`: the candidate's overall LR performance is clearly stronger;
- `comparable`: the candidate belongs at approximately the same LR boundary;
- `below`: the candidate's overall LR performance is clearly weaker.

Judge the complete LR construct:

- vocabulary range across the whole response;
- flexibility for the meanings required by this task;
- precision and successful collocational control;
- successful control of less-common vocabulary;
- frequency and seriousness of objective word-choice, collocation, spelling, and word-formation errors;
- stability across the response.

Do not compare topic sophistication, specialist terminology density, idiom density, or how intellectually complex the subject is. Task 1 graph/process/map language and Task 2 argument language are task-relative. A medical essay is not automatically lexically stronger than a film essay merely because its topic contains technical terms.

Necessary repetition of prompt terms, chart categories, named entities, and central argument terms is not a weakness. Distinguish objective lexical errors from wording that is merely nonstandard, awkward, or capable of stylistic improvement.

Return one comparison for every supplied anchor ID. The program, not the model, will combine the comparisons by score band and calculate any adjustment. Do not output a final score or adjustment.
