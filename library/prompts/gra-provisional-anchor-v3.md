# GRA provisional plus one-way upward anchor rounding v3

Date: 2026-09-24

Status: development candidate. This is a project adaptation, not an official IELTS prompt or a calibrated accuracy claim.

Use the v1 provisional GRA evidence ledger and same-task anchor comparison. Do not run a general deduction pass. If the provisional result is an integer, retain it. If it is an `x.5` boundary and an anchor decision is needed, the only permitted adjustment is upward to the next integer. Downward rounding is disabled. The final band must therefore be an integer whenever an anchor adjustment is applied.

Do not treat repeated errors as additive deductions. Use them to explain the evidence and confidence, while preserving the one-way upward rule. If the evidence does not support promotion, retain the provisional `x.5` rather than rounding down.

Task 1 and Task 2 anchors must remain separate. Return the provisional band, final band, component evidence, grouped error ledger, anchor information, rounding direction (`up` or `none`), confidence, and limitations.
