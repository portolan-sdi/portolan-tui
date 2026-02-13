<div align="center">
  <img src="https://raw.githubusercontent.com/portolan-sdi/portolan-cli/main/docs/assets/images/cover.png" alt="Portolan" width="600"/>
</div>

<div align="center">

[![CI](https://github.com/portolan-sdi/portolan-tui/actions/workflows/ci.yml/badge.svg)](https://github.com/portolan-sdi/portolan-tui/actions/workflows/ci.yml)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![PyPI version](https://badge.fury.io/py/portolan-tui.svg)](https://badge.fury.io/py/portolan-tui)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

</div>

---

Interactive terminal UI plugin for [Portolan](https://github.com/portolan-sdi/portolan-cli).

Portolan TUI provides an interactive terminal user interface for resolving manual issues identified by the `portolan scan` command without leaving the terminal environment.

## Purpose

The `portolan scan` command categorizes findings into three tiers:

| Tier | Description | Resolution |
|------|-------------|------------|
| **Ready** | Fully automatable | Handled automatically |
| **Safe fix** | Low-risk fixes | Apply with `--fix` flag |
| **Manual** | Requires human judgment | **Use this TUI plugin** |

**Portolan TUI** focuses on the **Manual** tier — issues that require human decision-making, such as:

- **Ambiguous sidecar relationships** — When it's unclear which main file a sidecar belongs to
- **Multi-asset directory splitting** — When multiple assets need to be separated into distinct directories

## Status

**Pre-release** — API and implementation in progress.

## Installation

### Recommended: pipx (for global use)

```bash
pipx install portolan-tui
```

This installs `portolan-tui` in an isolated environment while making it available as a Portolan plugin.

If you don't have pipx installed:
```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

### Alternative: pip

```bash
pip install portolan-tui
```

**Note:** This installs into your global or user site-packages and may conflict with other packages.

### For Development

Use [uv](https://github.com/astral-sh/uv) for local development:

```bash
git clone https://github.com/portolan-sdi/portolan-tui.git
cd portolan-tui
uv sync --all-extras
```

### Developing with portolan-cli

To test portolan-tui as a plugin alongside portolan-cli:

```bash
# From your portolan-cli directory
cd path/to/portolan-cli
uv pip install -e path/to/portolan-tui

# Verify integration
portolan tui --help
```

Editable mode (`-e`) means changes to portolan-tui take effect immediately.

See [Contributing Guide](docs/contributing.md) for full development setup.

## Usage

```bash
# Launch TUI to resolve manual issues in a directory
portolan tui resolve /data

# See available TUI commands
portolan tui --help
```

## Key Features

- **Interactive Resolution** — Navigate and resolve issues using keyboard shortcuts
- **File Operations** — Execute file moves directly from the TUI based on your decisions
- **Non-destructive** — Preview changes before applying; all operations are reversible
- **Textual-based** — Modern terminal UI with mouse support

## Documentation

- [Contributing Guide](docs/contributing.md)

## Related

- [portolan-cli](https://github.com/portolan-sdi/portolan-cli) — Main CLI (required)
- [portolake](https://github.com/portolan-sdi/portolake) — Lakehouse versioning plugin
- [Issue #68](https://github.com/portolan-sdi/portolan-cli/issues/68) — Original specification

## License

Apache 2.0 — see [LICENSE](LICENSE)
