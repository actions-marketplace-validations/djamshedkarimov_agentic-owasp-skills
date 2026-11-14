# Contributing

## Setup

```sh
make install   # uv env, pinned Semgrep, TypeScript example deps
make check     # ruff, tsc, Semgrep rule tests, pytest
```

The scanner's security overrides are in `docker/security-overrides.in`. Semgrep
currently declares older MCP and OpenTelemetry versions; these overrides select
patched releases while keeping the OpenTelemetry packages in sync. `make install`
applies the same overrides to the local scanner. After changing them, run
`make relock` to regenerate the complete hashed dependency list for Python 3.14,
then run `make check` and the Action and Docker CI checks to verify compatibility.

The Action and image install that complete list with `--no-deps` so pip does not
reapply Semgrep's vulnerable dependency pins. Hash verification and wheel-only
installation remain enabled. Remove the overrides when Semgrep's requirements
accept the patched versions. The Docker build also refreshes the pinned base's
packages and requires updated glibc and Python builds; vulnerability scanning
continues to gate the resulting image.

## Pull requests

| Rule | Detail |
|---|---|
| Branch from `main`, one concern per PR | `main` only moves by PR, after the required checks pass and one approval. Same-repo PRs by the owner or Dependabot are approved by a workflow once the required checks pass; anything else gets a human review |
| `make check` passes before you push | CI runs the same, plus CodeQL, zizmor, TruffleHog, dependency review, and a Grype image scan |
| Behaviour changes ship with tests | CLI and Action changes get a pytest case; rule changes get fixtures (below) |
| Leave versions alone | Releases are separate PRs; see Versioning in the README |

## Rules

Rules live in `skills/mcp-security/rules/<language>/<topic>.yaml`, each with a fixture
`<topic>.py` or `<topic>.ts` beside it.

- Mark what must fire with `# ruleid: <id>` and what must not with `# ok: <id>`;
  `semgrep --test` fails on any mismatch.
- Give every rule `cheat-sheet-control`, `owasp-mcp`, `owasp-agentic`, `cwe`, and `confidence`
  metadata that agrees with [crosswalk.md](skills/mcp-security/crosswalk.md). A rule present in
  both languages carries the same classification in each; `tests/test_rules.py` checks all of it.
- List the rule in the [skill checklist](skills/mcp-security/SKILL.md) under its control;
  `tests/test_skill.py` checks.
- If you add an example under `examples/`, annotate the vulnerable one and give it a safe
  counterpart; `tests/test_examples.py` checks both.
- Rule IDs are stable. Renaming or removing one is a major version bump; a rule that can add
  findings is a minor bump.

## Security

Report vulnerabilities as described in [SECURITY.md](SECURITY.md), not in an issue.

Contributions are licensed under [Apache-2.0](LICENSE).
