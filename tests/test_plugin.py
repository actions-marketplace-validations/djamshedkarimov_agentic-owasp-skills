import json
import tomllib

from catalog import REPO_ROOT

PLUGIN_DIR = REPO_ROOT / ".claude-plugin"


def test_plugin_version_matches_package() -> None:
    plugin = json.loads((PLUGIN_DIR / "plugin.json").read_text())
    package = tomllib.loads((REPO_ROOT / "pyproject.toml").read_text())["project"]
    assert plugin["version"] == package["version"]


def test_marketplace_lists_the_repo_root_plugin() -> None:
    plugin = json.loads((PLUGIN_DIR / "plugin.json").read_text())
    [entry] = json.loads((PLUGIN_DIR / "marketplace.json").read_text())["plugins"]
    assert entry["name"] == plugin["name"]
    assert entry["source"] == "./"
    assert "version" not in entry


def test_plugin_icon_is_a_png_inside_the_plugin() -> None:
    plugin = json.loads((PLUGIN_DIR / "plugin.json").read_text())
    icon = (REPO_ROOT / plugin["icon"]).resolve()
    assert icon.is_relative_to(REPO_ROOT)
    assert icon.read_bytes().startswith(b"\x89PNG\r\n\x1a\n")
