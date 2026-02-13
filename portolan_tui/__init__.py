"""Portolan TUI: Interactive terminal UI for resolving manual scan issues.

This package provides an interactive terminal user interface for resolving
manual issues identified by the `portolan scan` command. It handles cases
that require human judgment, such as:

- Ambiguous sidecar file relationships
- Multi-asset directory splitting

It integrates with portolan-cli as a plugin, adding the `tui` command group.

See: https://github.com/portolan-sdi/portolan-cli/issues/68
"""

from __future__ import annotations

import click

__version__ = "0.1.0"


@click.group(name="tui")
def tui_command_group() -> None:
    """Interactive TUI for resolving manual scan issues.

    This command group provides an interactive terminal interface for
    resolving issues that require human decision-making.
    """


@tui_command_group.command(name="resolve")
@click.argument("path", type=click.Path(exists=True))
def resolve_command(path: str) -> None:
    """Launch interactive resolution interface for manual issues.

    PATH is the directory containing scan results to resolve.

    Example:
        portolan tui resolve /data
    """
    # TODO: Implement TUI launch using `path`
    # Will launch a Textual app showing manual-fix items
    _ = path  # Will be used when implementation is complete
    raise NotImplementedError("TUI resolve command not yet implemented")


__all__ = ["__version__", "tui_command_group", "resolve_command"]
