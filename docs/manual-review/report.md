# Sanitized report template — preparation v1

Assessment ID/date: pending. Workflow commit: pending. Target alias/revision: pending.
Host/version/OS: pending. Scope/intake revision: pending. Assessor/engineer: pending.
Model/configuration: pending, or explain why no model was used. Source-only review; runtime
effectiveness unverified. Evidence collection conditions and alteration permissions: pending.

## Verdict rules

Record control outcome separately from execution. Outcomes are Pass, Fail, Unknown, N/A.
Execution states are completed, not run, unsupported, error. Applicability is applicable, pending,
or not applicable with a reason. A completed review can yield Unknown; missing required evidence
cannot yield Pass. N/A requires a supported applicability reason. A review/tool error is not itself
a target security failure. A confirmed Fail requires an applicable requirement and evidence.

Do not convert a legacy MCP scanner's Not scanned or scan health into a control outcome here.
No importer is provided. One passing check does not pass requirements it did not assess.

## Three check slots

These are placeholders, not selected checks. Unknown/not run/pending are the initial values.
Once the intake is ready, replace each slot with one agreed target-specific check and complete its
detail record. Never omit a required slot because evidence is missing.

| Slot | Selected check / requirement | Outcome | Execution | Applicability | Evidence or named gap | Rationale | Limitations | Next verification step |
|---|---|---|---|---|---|---|---|---|
| C-01 | Unselected | Unknown | not run | pending | G-01: target and host absent | Cannot select a target check | No target reviewed | Resolve intake with engineer |
| C-02 | Unselected | Unknown | not run | pending | G-01 | Cannot select a target check | No target reviewed | Resolve intake with engineer |
| C-03 | Unselected | Unknown | not run | pending | G-01 | Cannot select a target check | No target reviewed | Resolve intake with engineer |

### Detail record (repeat for each selected check)

- Check ID, boundary, requirement, exact original standard version/section and mapping rationale:
- Applicability and supported source/host/profile; excluded components:
- Procedure and predefined expected conclusion; known-defect/corrected source pair revisions:
- Evidence IDs, resolvable locator/selectors, artifact revision/representation/digest if available:
- Collector/method/date, alteration permissions, collection limitations and configuration:
- Target assertion vs assessor observation vs independently corroborated effect:
- Expected/observed behavior, attempts, deviations, uncertainty and outcome rationale:
- Outcome, execution state, named missing evidence and evidence owner:
- Remediation, source retest evidence/link and next verification step:
- Runtime effectiveness: unverified unless separately authorized and observed with evidence.

## Gaps, cases and corrections

| Gap ID | Missing prerequisite/evidence | Effect on conclusion | Owner / next action |
|---|---|---|---|
| G-01 | Target, source revision, host/version and agreed scope | Checks unselected; all Unknown/not run | Engineer completes intake |

| Case / corpus revision | Expected behavior | Host/model/settings | Attempts | Observed result/deviation and evidence | Limitations |
|---|---|---|---|---|---|
| Pending | Define before review | Pending | 0 | Not run | No model-resistance claim |

Treat instruction-like evidence contextually. Record a benign fixture as benign, a reviewer override
attempt as an attempt, and a confirmed requirement failure only with supporting evidence. Preserve
scope and verdict rules; record any observed deviation. These are bounded observations, not proof
of general injection resistance.

Second reviewer/date: pending. Resolved artifacts and reproduced reasoning: pending.
Engineer corrections, reproduction steps, review effort and fix/retest links: pending.
Next recommended slice and prerequisites: pending. Keep unresolved failures and gaps visible.
