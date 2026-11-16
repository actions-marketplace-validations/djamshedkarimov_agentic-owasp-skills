"""Export and verify the documentation-only manual intake kit (standard library only)."""

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path

DOCUMENTS = ("README.md", "intake.md", "report.md", "example.md", "engineer-guide.md")
PAYLOAD = (*DOCUMENTS, "manual_intake_bundle.py")
FORMAT = "manual-intake-preparation-v1"


def digest(path: Path) -> str:
    if path.is_symlink() or not path.is_file():
        raise ValueError(f"Expected a regular, non-symlink file: {path.name}")
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_links(directory: Path) -> None:
    """Check this kit's simple relative Markdown file references; never fetch URLs."""
    for name in DOCUMENTS:
        for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", (directory / name).read_text()):
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", link):
                continue
            file_name, _, anchor = link.partition("#")
            if file_name not in DOCUMENTS:
                raise ValueError(f"Unsupported or unresolved local link in {name}: {link}")
            if anchor:
                headings = re.findall(r"^#+ (.+)$", (directory / file_name).read_text(), re.MULTILINE)
                anchors = {re.sub(r"[^\w -]", "", heading.lower()).replace(" ", "-") for heading in headings}
                if anchor not in anchors:
                    raise ValueError(f"Unresolved anchor in {name}: {link}")


def verify(directory: Path) -> dict:
    if directory.is_symlink() or not directory.is_dir():
        raise ValueError("Bundle must be a non-symlink directory")
    if {path.name for path in directory.iterdir()} != {*PAYLOAD, "manifest.json"}:
        raise ValueError("Bundle must contain exactly the five documents, verifier and manifest")
    digest(directory / "manifest.json")
    manifest = json.loads((directory / "manifest.json").read_text())
    if not isinstance(manifest, dict) or set(manifest) != {"format", "source_revision", "files"}:
        raise ValueError("Invalid manifest fields")
    if manifest["format"] != FORMAT or not re.fullmatch(r"[0-9a-f]{40}", str(manifest["source_revision"])):
        raise ValueError("Unsupported format or invalid source revision")
    files = manifest["files"]
    if not isinstance(files, dict) or set(files) != set(PAYLOAD):
        raise ValueError("Invalid manifest file inventory")
    for name in PAYLOAD:
        if files[name] != digest(directory / name):
            raise ValueError(f"Digest mismatch: {name}")
    check_links(directory)
    return manifest


def build(destination: Path, revision: str) -> None:
    if not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise ValueError("Use the full 40-character source commit ID")
    source = Path(__file__).resolve().parents[1] / "docs" / "manual-review"
    check_links(source)
    # Reject symlinks before copying. The export contains only this fixed inventory.
    for name in DOCUMENTS:
        digest(source / name)
    destination.mkdir()  # Never overwrite an existing directory or private filled intake.
    for name in DOCUMENTS:
        shutil.copyfile(source / name, destination / name)
    shutil.copyfile(Path(__file__), destination / "manual_intake_bundle.py")
    manifest = {
        "format": FORMAT,
        "source_revision": revision,
        "files": {name: digest(destination / name) for name in PAYLOAD},
    }
    (destination / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    verify(destination)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    export = commands.add_parser("build", help="Export from a trusted checkout into a new directory")
    export.add_argument("directory", type=Path)
    export.add_argument("--revision", required=True, help="Full source commit ID, supplied by the collector")
    inspect = commands.add_parser("verify", help="Check inventory, bytes and local links; no assessment verdict")
    inspect.add_argument("directory", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "build":
            build(args.directory, args.revision)
        else:
            verify(args.directory)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Bundle check failed: {error}\n")
    print("Bundle checks passed (documentation preparation only; no host or assessment acceptance).")


if __name__ == "__main__":
    main()
