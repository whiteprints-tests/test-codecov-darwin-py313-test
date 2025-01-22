# SPDX-FileCopyrightText: © 2025 Romain Brault <mail@romainbrault.com>
#
# SPDX-License-Identifier: MIT OR Apache-2.0

"""Test the console module."""

from rich import console as rich_console

from test_codecov_darwin_py313_test import console as whiteprint_console


def test_default_stdout_console() -> None:
    """Check that the STDOUT console is a rich console instance."""
    assert isinstance(whiteprint_console.STDOUT, rich_console.Console)


def test_default_stderr_console() -> None:
    """Check that the STDERR console is a rich console instance."""
    assert isinstance(whiteprint_console.STDERR, rich_console.Console)
