import re

import pytest
from catalog import REPO_ROOT

from agentic_owasp.scanner import SEMGREP_MIN, semgrep_supported

MAJOR, MINOR, PATCH = (int(part) for part in SEMGREP_MIN.split("."))


def test_image_pin_satisfies_the_floor() -> None:
    requirements = (REPO_ROOT / "docker" / "requirements.in").read_text()
    [pinned] = re.findall(r"^semgrep==(\S+)$", requirements, re.MULTILINE)
    assert semgrep_supported(pinned)


@pytest.mark.parametrize(
    ("version", "supported"),
    [
        (SEMGREP_MIN, True),
        (f"{MAJOR}.{MINOR}.{PATCH + 1}", True),
        (f"{MAJOR}.{MINOR + 1}.0", True),
        (f"{MAJOR}.{MINOR - 1}.{PATCH}", False),
        (f"{MAJOR + 1}.0.0", False),
        (f"{MAJOR}.{MINOR + 1}.0rc1", False),
        ("", False),
    ],
)
def test_supported_is_floor_and_same_major(version: str, supported: bool) -> None:
    assert semgrep_supported(version) is supported
