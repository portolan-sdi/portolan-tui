"""Tests for portolan-tui entry point registration and command group discoverability.

These tests verify that portolan-tui correctly registers as a portolan-cli command
plugin via Python's entry_points mechanism.

See: https://github.com/portolan-sdi/portolan-cli/issues/68
"""

from importlib.metadata import entry_points

import pytest
from click.testing import CliRunner


@pytest.mark.unit
def test_command_is_discoverable():
    """Verify portolan-tui registers correctly as a portolan command.

    The entry point must be registered under the 'portolan.commands' group
    with the name 'tui'.
    """
    eps = entry_points(group="portolan.commands")
    names = [ep.name for ep in eps]

    assert "tui" in names, f"Expected 'tui' in {names}"


@pytest.mark.unit
def test_command_loads():
    """Verify the command group can be loaded from the entry point."""
    eps = entry_points(group="portolan.commands")
    tui_ep = next((ep for ep in eps if ep.name == "tui"), None)

    assert tui_ep is not None, "Entry point 'tui' not found"

    command_group = tui_ep.load()
    assert command_group.name == "tui"


@pytest.mark.unit
def test_tui_command_group_importable():
    """Verify tui_command_group can be imported directly from portolan_tui."""
    from portolan_tui import tui_command_group

    assert tui_command_group is not None
    assert tui_command_group.name == "tui"


@pytest.mark.unit
def test_tui_command_group_has_resolve():
    """Verify the tui command group has the resolve subcommand."""
    from portolan_tui import tui_command_group

    command_names = list(tui_command_group.commands)
    assert "resolve" in command_names


@pytest.mark.unit
def test_resolve_command_help():
    """Verify the resolve command shows help text."""
    from portolan_tui import tui_command_group

    runner = CliRunner()
    result = runner.invoke(tui_command_group, ["resolve", "--help"])

    assert result.exit_code == 0
    assert "Launch interactive resolution interface" in result.output
    assert "PATH" in result.output


@pytest.mark.unit
def test_resolve_command_requires_path():
    """Verify the resolve command requires a path argument."""
    from portolan_tui import tui_command_group

    runner = CliRunner()
    result = runner.invoke(tui_command_group, ["resolve"])

    assert result.exit_code != 0
    assert "Missing argument" in result.output


@pytest.mark.unit
def test_resolve_command_not_implemented(tmp_path):
    """Verify the resolve command raises NotImplementedError (stub behavior)."""
    from portolan_tui import tui_command_group

    runner = CliRunner()
    result = runner.invoke(tui_command_group, ["resolve", str(tmp_path)])

    # NotImplementedError should cause non-zero exit
    assert result.exit_code != 0
    # The exception is stored in result.exception, not output
    assert isinstance(result.exception, NotImplementedError)
    assert "not yet implemented" in str(result.exception)
