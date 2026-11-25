FROM cgr.dev/chainguard/wolfi-base@sha256:28c39be5a5e1e9b85081c10740e8495f6518a865b23bc6a486637c4b21e74b43 AS python
# Refresh packages inherited from the pinned base, including the glibc fixes.
RUN apk upgrade --no-cache \
    && apk add --no-cache 'glibc-2.44>=2.44-r19' 'python-3.14>=3.14.10_git20261111-r0'

FROM python AS builder

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 PIP_NO_CACHE_DIR=1
WORKDIR /build
COPY docker/*.txt docker/
RUN python3.14 -m venv /opt/build \
    && /opt/build/bin/pip install --require-hashes --only-binary :all: -r docker/build-requirements.txt \
    && python3.14 -m venv /opt/venv \
    && /opt/venv/bin/pip install --require-hashes --only-binary :all: --no-deps -r docker/requirements.txt
COPY pyproject.toml hatch_build.py README.md LICENSE ./
COPY src src
COPY skills skills
RUN /opt/build/bin/pip wheel --no-deps --no-build-isolation --wheel-dir dist . \
    && /opt/venv/bin/pip install --no-deps dist/*.whl

FROM python

COPY --from=builder /opt/venv /opt/venv
ENV PATH=/opt/venv/bin:$PATH PYTHONDONTWRITEBYTECODE=1
# wolfi-base's built-in nonroot user.
USER 65532
WORKDIR /src
ENTRYPOINT ["agentic-owasp"]
CMD ["scan", "."]
