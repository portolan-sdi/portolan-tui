# Portolan TUI - Development Guide

## What is Portolan TUI?

Portolan TUI is a **plugin for [Portolan CLI](https://github.com/portolan-sdi/portolan-cli)** that provides an interactive terminal user interface for resolving manual issues identified by `portolan scan`. It's the TUI companion described in [Issue #68](https://github.com/portolan-sdi/portolan-cli/issues/68).

**Key concepts:**
- **Textual** — Modern TUI framework for Python providing rich terminal interfaces
- **Manual Issues** — Scan findings that require human decision-making (ambiguous relationships, multi-asset directories)
- **Portolan** — The parent CLI that orchestrates format conversion and catalog management

**What Portolan TUI provides:**
- Interactive resolution of ambiguous sidecar file relationships
- Multi-asset directory splitting interface
- File operation execution based on user decisions
- Non-destructive preview mode before applying changes

**Target users:** Anyone working with complex geospatial data directories where automated resolution isn't sufficient.

## Guiding Principle

AI agents will write most of the code. Human review does not scale to match AI output volume. Therefore: every quality gate must be automated, every convention must be enforceable, and tests must be verified to actually test something.

## Quick Reference

| Resource | Location |
|----------|----------|
| Parent project | [portolan-cli](https://github.com/portolan-sdi/portolan-cli) |
| Architecture decisions | [portolan-cli ADRs](https://github.com/portolan-sdi/portolan-cli/tree/main/context/shared/adr) |
| Plugin architecture | [ADR-0003](https://github.com/portolan-sdi/portolan-cli/blob/main/context/shared/adr/0003-plugin-architecture.md) |
| Scan triage output | [Issue #66](https://github.com/portolan-sdi/portolan-cli/issues/66) |
| TUI specification | [Issue #68](https://github.com/portolan-sdi/portolan-cli/issues/68) |

**Target Python version:** 3.11+ (matches portolan-cli requirements)

## Common Commands

```bash
# Environment setup
uv sync --all-extras                    # Install all dependencies
uv run pre-commit install               # Install git hooks

# Development
uv run pytest                           # Run tests
uv run pytest -m unit                   # Run only unit tests
uv run pytest --cov-report=html         # Coverage report
uv run ruff check .                     # Lint
uv run ruff format .                    # Format
uv run vulture portolan_tui tests       # Dead code
uv run xenon --max-absolute=C portolan_tui # Complexity

# Commits (use commitizen for conventional commits)
uv run cz commit                        # Interactive commit
uv run cz bump --dry-run                # Preview version bump

# Running the TUI locally
uv run textual run portolan_tui:app     # Run TUI directly for testing
```

## Project Structure

```
portolan-tui/
├── portolan_tui/          # Source code
│   ├── __init__.py        # CLI entry point and exports
│   ├── app.py             # Main Textual application
│   ├── screens/           # TUI screens (resolve, preview, etc.)
│   ├── widgets/           # Custom Textual widgets
│   └── models/            # Data models for issues and resolutions
├── tests/                 # Test suite
└── .github/workflows/     # CI/CD pipelines
```

## Test-Driven Development (MANDATORY)

**YOU MUST USE TDD. NO EXCEPTIONS.** Unless the user explicitly says "skip tests":

1. **WRITE TESTS FIRST** — Before ANY implementation code
2. **RUN TESTS** — Verify they fail with `uv run pytest`
3. **IMPLEMENT** — Minimal code to pass tests
4. **RUN TESTS AGAIN** — Verify they pass
5. **ADD EDGE CASES** — Test error conditions

### Test Markers

```python
@pytest.mark.unit        # Fast, isolated, no I/O (< 100ms)
@pytest.mark.integration # Multi-component, may touch filesystem
@pytest.mark.network     # Requires network (mocked locally, live in nightly)
@pytest.mark.benchmark   # Performance measurement
@pytest.mark.slow        # Takes > 5 seconds
```

## CI Pipeline

| Tier | When | What |
|------|------|------|
| Tier 1 | Pre-commit | ruff, vulture, xenon, fast tests |
| Tier 2 | Every PR | lint, security, full tests, dead-code, build |

**All checks are strict** — no `continue-on-error`. Fix issues or they block.

## Code Quality

- **ruff** — Linting and formatting
- **vulture** — Dead code detection
- **xenon** — Complexity monitoring (max C function, B module, A average)
- **pip-audit** — Dependency vulnerabilities

## Git Workflow

### Branch Naming

```
feature/description    # New features
fix/description        # Bug fixes
docs/description       # Documentation
refactor/description   # Code restructuring
```

### Conventional Commits

Use `uv run cz commit` for interactive commit creation:

```
feat(scope): add new feature      # Minor version bump
fix(scope): fix bug               # Patch version bump
docs(scope): update documentation
refactor(scope): restructure code
test(scope): add tests
BREAKING CHANGE: ...              # Major version bump
```

### Merge Policy

**Squash-merge** all PRs to main. This ensures:
- Clean history (one commit per PR)
- PR title becomes the commit message (enforce conventional format)
- Commitizen can analyze commits cleanly for versioning

### Release Automation

Portolan TUI uses a **tag-based release workflow**. See `.github/workflows/release.yml`.

**To release:**
1. Create a PR that runs `uv run cz bump --changelog`
2. Merge the bump PR
3. Release workflow detects the bump commit and creates tag + publishes

## Development Rules

- **ALL** new features require tests FIRST (TDD)
- **NO** new dependencies without discussion

## Key Dependencies

| Library | Purpose | Docs |
|---------|---------|------|
| [Textual](https://textual.textualize.io/) | TUI framework | [Docs](https://textual.textualize.io/) |
| [Click](https://click.palletsprojects.com/) | CLI integration | [Docs](https://click.palletsprojects.com/) |

## Design Principles

| Principle | Meaning |
|-----------|---------|
| **Plugin, not standalone** | Portolan TUI extends Portolan; it doesn't replace it |
| **Interactive complement** | Handles what `--fix` cannot automate |
| **Non-destructive by default** | Preview changes before applying |
| **Keyboard-first** | Full keyboard navigation for efficiency |
| **YAGNI** | No speculative features; complexity is expensive |

## Textual Development Notes

### Testing TUI Components

Textual provides a testing framework using `pilot`:

```python
from textual.pilot import Pilot

async def test_app_startup():
    async with App().run_test() as pilot:
        # Test interactions
        await pilot.press("q")  # Quit
```

### Common Patterns

- **Screens** — Use `Screen` classes for distinct views (resolve, preview)
- **Widgets** — Custom widgets for issue display, file trees
- **Actions** — Define actions with `@on` decorators
- **CSS** — Textual uses CSS for styling (put in `.tcss` files)
