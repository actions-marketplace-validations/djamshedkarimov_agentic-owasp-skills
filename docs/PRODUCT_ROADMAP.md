# AI Security Skills Suite roadmap

Our direction is a suite of OWASP-aligned security skills for AI applications, agents, MCP
integrations, and the systems running them. Assessments will connect security requirements to
source and runtime evidence, actionable remediation, and repeatable verification.

## Available today

The MCP source-review skill combines a manual checklist with deterministic source scanning.
The CLI, Docker image, and GitHub Action support local reviews and CI checks. See the
[README](../README.md) for supported stacks and current limitations.

## Next

- Establish shared control mappings and assessment reports across skills.
- Add AI application threat modeling and reviews of input, output, and data-access boundaries.
- Extend agent reviews to tool permissions, delegation, approvals, and execution limits,
  including agents that do not use MCP.

## Planned coverage

| Area | Focus |
|---|---|
| AI applications | Prompt injection, output handling, sensitive data exposure, resource limits |
| RAG and memory | Retrieval permissions, tenant isolation, ingestion integrity, memory lifecycle |
| Agents | Tool authority, identity propagation, delegation, approvals, action boundaries |
| MCP integrations | Server/client boundaries, schemas, credentials, transports, tool interactions |
| AI systems | Deployment configuration, service identities, secrets, isolation, monitoring |
| Model supply chains | Provenance, artifact integrity, dependencies, loading and release changes |
| Release reviews | Consolidated evidence, unresolved risks, change tracking, regression checks |

## OWASP alignment

Planned verification will draw on
[OWASP AISVS](https://owasp.github.io/www-project-artificial-intelligence-security-verification-standard-aisvs-docs/)
and [ASVS](https://asvs.owasp.org/), with separate mappings to applicable LLM, agentic, MCP,
and API security guidance. Reports will identify the guidance versions and assessed scope.
OWASP alignment does not imply certification or endorsement.

## Delivery approach

Release capabilities progressively with documented support, worked examples, and validation.
Keep missing evidence and unsupported checks visible, and distinguish source review from
runtime verification. Future items are exploratory; scope and ordering may change as we learn
from users. No release dates are committed.

Suggest a use case or request coverage through the repository's
[issue tracker](https://github.com/djamshedkarimov/agentic-owasp-skills/issues).
