# Portable preparation bundle — v1

This developer utility exports the intake preparation documents as one fixed, verifiable directory.
It is not an installable assessment skill or a host plugin. It does not select checks, validate report
verdicts, inspect target files, or establish runtime effectiveness. The supported profile is a trusted
repository checkout and Python 3.12+ with its standard library; recipient verification needs only
Python and the exported directory. No scanner, model, provider, package installation or network is
required. Recorded test environments and untested combinations belong in the PR.

## Export and recipient verification

From a clean checkout of the revision being distributed:

```sh
git rev-parse HEAD
python3 tools/manual_intake_bundle.py build /tmp/manual-intake-kit --revision FULL_COMMIT_ID
python3 /tmp/manual-intake-kit/manual_intake_bundle.py verify /tmp/manual-intake-kit
```

Replace `FULL_COMMIT_ID` with the full commit ID printed above. The collector supplies this label;
the utility does not authenticate it or prove that the checkout is clean. Record collection method,
collector/date, alteration permissions and trusted source commit separately. The output path must
not exist; the utility refuses to overwrite private work. Distribute only a fresh template export,
never a filled intake. The fixed inventory excludes private planning, target evidence and other
repository files. An I/O failure may leave partial output: do not distribute it; retry at a new path.

The output contains the five documents named in the engineer guide, the verifier and `manifest.json`.
The manifest records a format, supplied source revision, and SHA-256 of each payload file. The guide
you are reading is repository development documentation, outside that fixed payload. The verifier
rejects missing, extra, changed and symlinked files, invalid inventory/revision labels, and unresolved
local file/heading references used by these documents. It never fetches external links. This is a
simple Markdown reference check for this kit, not a general Markdown parser.

Copy the directory to a location outside the checkout. Run the copied verifier from another working
directory with isolated Python, for example:

```sh
cd /tmp
python3 -I /tmp/manual-intake-kit/manual_intake_bundle.py verify /tmp/manual-intake-kit
```

Expected: exit 0 and a preparation-only success message. Nonzero means bundle verification failed,
not a target security failure. Review the diagnostic and obtain a fresh export from the trusted
revision. Hashes detect changed bytes relative to the supplied manifest; they provide no signature,
trusted collection, source authenticity, or execution proof. A party able to replace the payload and
manifest can make them agree. Run the copied Python tool only when obtained from a trusted source;
for an untrusted kit, use a separately trusted checkout's verifier against that directory instead.
This tool is not a sandbox for concurrent hostile filesystem mutations.

Verify before filling templates. Editing an intake/report intentionally changes the template hashes.
Preserve the original kit separately and keep working copies/evidence private under the intake's
sharing rules. A filled report needs human evidence review, not a matching template manifest.

## Engineer cases and correction procedure

First run the five preparation cases in the exported `engineer-guide.md`. I-01 still leaves exactly
three unselected Unknown/not run/pending slots. H-01 and B-01 are manual reasoning cases, not checks
performed by the bundle verifier. M-01 must retain a named evidence gap. Record reviewer, host/editor,
model/settings or manual/no model, corpus/revision, attempts, observations, deviations and limitations.
A second reviewer must separately resolve artifacts and reproduce reasoning (R-01).

Then, on disposable copies of the kit, remove a document, change its bytes, add an extra file, replace
a document with a symlink, and break a local reference. Expected: verifier exit 1. Restore a fresh
export before each case. Attempt export to an existing directory containing a filled intake;
expected: exit 1 and existing bytes preserved. The automated regressions cover these mutations,
including a broken reference whose manifest hash was updated. Run them from the repository with:

```sh
uv run pytest tests/test_manual_intake_bundle.py
make check
```

Capture only sanitized command, revision, environment, exit status and diagnostic in shared evidence.
Never commit the filled kit or real target material. For a confirmed defect, record expected/observed
behavior, correction and evidence, add a synthetic regression, rebuild from the corrected revision,
and repeat affected cases. Link original and retest records; retain unresolved disagreements.

## Handoff

Slice: portable preparation bundle v1, following PR #66 at base `faad645`. Completed: fixed-inventory
export, manifest, standalone verification, mutation regressions and this test guide. The introducing
PR records actual acceptance evidence and revision. No engineer correction, real target observation,
host installation, model behavior or second-reviewer reasoning reproduction is claimed.

Next recommended slice remains one installable manual workflow for one non-MCP target and exactly
three engineer-agreed checks. Prerequisites: completed intake with target/revision, declared host and
version, authorized artifacts, actual boundaries and expected behavior. Deliver target-specific
procedures, pinned original references, actual diagram, defect/corrected pairs and sanitized report;
verify host installation and all package references, named cases and second-reviewer reasoning.
The bundle is an independent preparation aid, not a substitute for those gates. Runtime harness,
scanner importer, registry and consolidated release gates remain deferred.
