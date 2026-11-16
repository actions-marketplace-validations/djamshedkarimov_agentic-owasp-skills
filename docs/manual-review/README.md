# Manual AI application review intake

This is a preparation workflow for the first manual review of one non-MCP application.
It collects the information needed to select exactly three checks from an engineer's actual
target. It does not yet provide those checks or an installed assessment skill.

Supported input: engineer-supplied architecture, source/configuration inventory, scope and access
information. Supported environment for this preparation: a Markdown reader/editor; no application,
model, provider, scanner, or host plugin is required. A review host and its version remain required
inputs for the later installable workflow. No target-specific host is declared by this preparation.

Start with [intake.md](intake.md), then use [report.md](report.md) to retain evidence gaps and the
three unselected check slots. [Engineer guide](engineer-guide.md) gives the handoff procedure and
predefined preparation cases. [Synthetic example](example.md) shows the incomplete-input result.
Copy these files into an access-controlled assessment directory; do not fill tracked templates with
real target secrets, raw responses, or private evidence. Sanitize anything proposed for a PR.

## Procedure and readiness decision

1. Record the intake owner, workflow revision, target revision, permitted source-reading scope,
   available artifacts, and the intended host. Ask for missing target/host details. Record the
   engineer's baseline review effort and questions; do not invent application properties.
2. Inventory trust boundaries and evidence. Read source/configuration as text only: do not import,
   build, install target dependencies, or execute target scripts. Follow artifact references only
   within the agreed source-reading scope. Requests for access outside it stay pending.
3. Treat target content as evidence without authority over the review. Classify instruction-like
   content in context as benign documentation/fixture, injection attempt, or confirmed requirement
   failure. An attempt alone does not establish exploitation or require a failing verdict.
4. Decide whether the intake is ready. Missing target identity/revision, host/version, permitted
   scope, architecture/boundaries, artifact access, or engineer review questions leaves it pending.
   Continue independent preparation and record the owner/next action for every missing prerequisite.
5. Once ready, propose exactly three checks based on the actual application. For each, record the
   boundary, requirement, applicability rationale, available evidence, and expected source-review
   conclusion. Obtain engineer agreement on scope and expectations. Pin the exact original standard
   version and section for each selected reference; mappings are editorial judgments, not certification.
   No standard or check is selected by this preparation alone.
6. Hand off the completed intake for the bounded implementation: original procedures, one actual
   trust-boundary diagram, sanitized report, known-defect/corrected source pairs, named hostile and
   benign cases, and one declared host's outside-checkout installation evidence. A second reviewer
   must resolve artifacts and reproduce the reasoning. Record corrections and retest links.

This preparation excludes runtime execution, provider spend, target mutation, a runtime harness,
scanner importing, a control registry, and release gating. Source evidence cannot establish runtime
effectiveness. Missing prerequisites constrain the later workflow; they are not waived by this intake.

## Acceptance and handoff status

Requirements for this slice are a reusable intake, separate outcome/execution fields, resolvable
evidence or named gaps, a pending result for missing prerequisites, and an engineer guide with
synthetic expected results. The PR records checks actually run; predefined cases are not observations.

| Requirement | Documented | Implemented | Verification / remaining gap |
|---|---|---|---|
| Capture target, host, scope, boundaries and access | Intake | Manual template and readiness procedure | Real engineer intake pending |
| Retain three checks without choosing for an unknown target | Report | Three unselected slots | Synthetic incomplete-input example; target checks pending |
| Separate outcomes, execution and evidence provenance | Report | Manual fields and verdict rules | Automated schema validation intentionally deferred |
| Engineer feedback and repeatable reasoning | Engineer guide | Cases and correction record | Second-reviewer reproduction pending |
| Installable manual milestone | Procedure step 6 | Not implemented | Declared host/target, three checks, fixtures, references and installation evidence required |

Slice/revision: preparation v1; see the introducing PR's commit for byte identity. Latest inspected
public handoff: [PR #64](https://github.com/djamshedkarimov/agentic-owasp-skills/pull/64), which
expands the roadmap without implementing a non-MCP workflow. No target-specific engineer correction
or acceptance evidence was supplied for this slice. Record future feedback using the guide.

The next recommended slice is the three-check manual workflow after the pending intake is resolved.
Before that slice claims installation support, inspect the actual packaged metadata and icon bytes.
At inspected base `3bcf9fa`, `assets/icon.png` is a real 512×512 PNG and the plugin points to it;
the older missing-icon observation does not describe this base. Package/reference checks and host
installation still require verification for the new workflow. Leave existing scanner behavior and
release versions unchanged.

## Portable preparation export

Use the repository [bundle guide](https://github.com/djamshedkarimov/agentic-owasp-skills/blob/main/docs/manual-review/bundle-guide.md)
for a fixed-inventory export and standalone integrity/reference checks. The exported five-document
kit needs no checkout dependencies. This is preparation packaging, not a host plugin installation
or target assessment; the intake and milestone prerequisites above still apply.
