"""Basic import tests to verify package structure."""

import pytest


@pytest.mark.unit
def test_import_portolan_tui():
    """Verify the portolan_tui package can be imported."""
    import portolan_tui

    assert portolan_tui.__version__ == "0.1.0"


@pytest.mark.unit
def test_import_dependencies():
    """Verify core dependencies are importable."""
    import click

    assert click is not None
