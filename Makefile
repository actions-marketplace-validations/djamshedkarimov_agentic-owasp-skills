SEMGREP_VERSION := $(shell sed -n 's/^semgrep==//p' docker/requirements.in)
SEMGREP ?= semgrep==$(SEMGREP_VERSION)
TS_EXAMPLES := examples/typescript
RULES := skills/mcp-security/rules
COMPILE := uv pip compile --universal --python-version 3.13 --generate-hashes --exclude-newer $(shell date -u +%Y-%m-%d)

.PHONY: install lint format test check relock

install:
	uv sync --locked
	uv tool install --force $(SEMGREP)
	semgrep --version
	npm ci --prefix $(TS_EXAMPLES)

lint:
	uv run ruff check .
	uv run ruff format --check .
	npm run --prefix $(TS_EXAMPLES) typecheck

format:
	uv run ruff check --fix .
	uv run ruff format .

test:
	semgrep scan --test --metrics=off --disable-version-check $(RULES)
	uv run pytest

check: lint test

relock:
	$(COMPILE) docker/requirements.in -o docker/requirements.txt
	$(COMPILE) docker/build-requirements.in -o docker/build-requirements.txt
