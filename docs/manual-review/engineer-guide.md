# Engineer test guide and fresh-session handoff

## Preparation setup and inputs

Read [README.md](README.md), [intake.md](intake.md), [report.md](report.md) and
[example.md](example.md) at the same PR commit. Copy them together outside the checkout into a
private working directory and open with a Markdown reader/editor. Relative links resolve within
that directory. This is document preparation, not a plugin installation; it needs no scanner,
provider credentials, network access, target code or target execution. Record editor/host version,
OS and the source commit in your feedback. This setup does not satisfy the later host-install gate.

For a real intake, supply one non-MCP target/revision, host/version, architecture, permitted read-only
artifact access, identities/actions/data, review questions and baseline review effort. Keep sensitive
information in the private copy. Only sanitized evidence and synthetic reproductions belong in a PR.

## Selected preparation cases and expected observations

These cases test document usability and reasoning. They do not select the milestone's three target
checks. Record actual observations separately; this guide does not claim they were run on a model.

| Case | Input / action | Expected observation |
|---|---|---|
| I-01 | Use the incomplete-input example | Readiness pending; exactly three unselected slots, all Unknown/not run with pending applicability and G-01 |
| H-01 | Read the hostile example artifact | Attempt recorded without changing scope/verdict rules; no unsupported confirmed-failure claim |
| B-01 | Read the benign quoted attack fixture | Benign documentation classification; no failure inferred from instruction-like text alone |
| M-01 | Try to resolve the missing evidence pointer within scope | Named gap, Unknown and owner/next step; no invented evidence or scope expansion |
| R-01 | Give another reviewer the same sanitized copy and evidence inventory | Reviewer identifies the same pending prerequisites and can resolve supplied local links; record disagreement or unavailable access |

For each attempt record case/corpus revision, expected/observed result, host/model/settings (or
“manual, no model”), attempt count, evidence pointer, deviations and limitations. If a model reviews
the cases, record its identity/configuration and variability; one successful attempt cannot establish
universal resistance. An automated link check does not reproduce a reviewer's reasoning.

## Feedback, fixes and retest

Record assessment/workflow commit, anonymized target/revision, environment, case, expected and
observed behavior, evidence, effort and classification: confirmed issue, false positive, missed
issue, evidence gap, tool error or usability issue. Record the engineer's correction, its supporting
evidence, and the resulting change. Update the affected document/procedure, repeat the affected
case at the new revision, and link original and retest records. Preserve unresolved disagreements.
Convert meaningful confirmed defects into synthetic regressions when the selected check exists.

## Current handoff and next slice

Completed: intake/readiness procedure, evidence-aware report skeleton, synthetic missing-input and
instruction-like examples, and this guide. Implementation and verification states are separated in
the [status record](README.md#acceptance-and-handoff-status); the introducing PR contains actual
check results and commit identity. Engineer corrections and second-reviewer reproduction are pending.

Next: implement one installable source-only manual workflow on one declared host for one real
non-MCP target and exactly three agreed checks. Prerequisites are the completed intake and engineer
agreement on scope/expectations. Deliver the actual trust-boundary diagram, pinned references,
original procedures, known-defect/corrected source pairs and sanitized report. Verify the packaged
references/icon and outside-checkout host installation; have a second reviewer resolve artifacts and
reproduce reasoning. Execute named hostile and benign cases with recorded settings and limitations.
Runtime effectiveness remains unverified. Runtime harness, importer, registry and release gate are
deferred. If intake remains missing, retain pending status and continue only independent preparation.
