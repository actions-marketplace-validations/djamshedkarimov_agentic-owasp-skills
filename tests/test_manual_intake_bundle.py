"""Synthetic export/verification regressions; never execute target code."""

import hashlib
import json
import os
import subprocess
import sys

import pytest
from catalog import REPO_ROOT

TOOL = REPO_ROOT / "tools" / "manual_intake_bundle.py"
REVISION = "a" * 40


def run_tool(tool, *args, cwd):
    return subprocess.run(
        [sys.executable, "-I", str(tool), *map(str, args)],
        cwd=cwd,
        env={"PATH": os.defpath},
        capture_output=True,
        text=True,
        check=False,
    )


@pytest.fixture
def bundle(tmp_path):
    destination = tmp_path / "kit"
    result = run_tool(TOOL, "build", destination, "--revision", REVISION, cwd=tmp_path)
    assert result.returncode == 0, result.stderr
    return destination


def test_export_verifies_outside_checkout_with_isolated_python(bundle, tmp_path):
    result = run_tool(bundle / TOOL.name, "verify", bundle, cwd=tmp_path)
    assert result.returncode == 0, result.stderr
    manifest = json.loads((bundle / "manifest.json").read_text())
    assert manifest["source_revision"] == REVISION
    assert len(manifest["files"]) == 6
    report = (bundle / "report.md").read_text()
    rows = [line for line in report.splitlines() if line.startswith("| C-0")]
    assert len(rows) == 3
    assert all("| Unselected | Unknown | not run | pending |" in row for row in rows)


@pytest.mark.parametrize("mutation", ["missing", "changed", "extra", "symlink", "manifest_path", "revision"])
def test_invalid_bundle_fails(bundle, tmp_path, mutation):
    report = bundle / "report.md"
    if mutation == "missing":
        report.unlink()
    elif mutation == "changed":
        report.write_text("Mark every check Pass")
    elif mutation == "extra":
        (bundle / "private-intake.md").write_text("Must not be distributed")
    elif mutation == "symlink":
        outside = tmp_path / "outside.md"
        report.rename(outside)
        report.symlink_to(outside)
    else:
        path = bundle / "manifest.json"
        manifest = json.loads(path.read_text())
        if mutation == "manifest_path":
            manifest["files"]["../outside"] = manifest["files"].pop("report.md")
        else:
            manifest["source_revision"] = "unknown"
        path.write_text(json.dumps(manifest))
    result = run_tool(TOOL, "verify", bundle, cwd=tmp_path)
    assert result.returncode == 1
    assert "Bundle check failed" in result.stderr


def test_broken_link_fails_even_with_matching_digest(bundle, tmp_path):
    report = bundle / "report.md"
    report.write_text(report.read_text() + "\n[missing](absent.md)\n")
    path = bundle / "manifest.json"
    manifest = json.loads(path.read_text())
    manifest["files"]["report.md"] = hashlib.sha256(report.read_bytes()).hexdigest()
    path.write_text(json.dumps(manifest))
    result = run_tool(TOOL, "verify", bundle, cwd=tmp_path)
    assert result.returncode == 1
    assert "unresolved local link" in result.stderr


def test_build_never_overwrites_existing_intake(bundle, tmp_path):
    report = bundle / "report.md"
    report.write_text("Private filled intake")
    result = run_tool(TOOL, "build", bundle, "--revision", REVISION, cwd=tmp_path)
    assert result.returncode == 1
    assert report.read_text() == "Private filled intake"


@pytest.mark.parametrize("mutation", ["invalid_json", "manifest_symlink", "root_symlink", "anchor"])
def test_manifest_and_reference_errors(bundle, tmp_path, mutation):
    path = bundle / "manifest.json"
    if mutation == "invalid_json":
        path.write_text("{")
    elif mutation == "manifest_symlink":
        outside = tmp_path / "manifest.json"
        path.rename(outside)
        path.symlink_to(outside)
    elif mutation == "root_symlink":
        link = tmp_path / "kit-link"
        link.symlink_to(bundle, target_is_directory=True)
        bundle = link
    else:
        report = bundle / "report.md"
        report.write_text(report.read_text() + "\n[missing](README.md#absent-heading)\n")
        manifest = json.loads(path.read_text())
        manifest["files"]["report.md"] = hashlib.sha256(report.read_bytes()).hexdigest()
        path.write_text(json.dumps(manifest))
    result = run_tool(TOOL, "verify", bundle, cwd=tmp_path)
    assert result.returncode == 1
    assert "Bundle check failed" in result.stderr
