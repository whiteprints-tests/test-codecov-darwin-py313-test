# SPDX-FileCopyrightText: © 2025 Romain Brault <mail@romainbrault.com>
#
# SPDX-License-Identifier: MIT OR Apache-2.0

"""Manage a global rich console."""

from typing import Final

from rich import console


__all__: Final = ["STDERR", "STDOUT"]
"""Public module attributes."""


STDOUT: Final = console.Console()
"""A high level console interface instance.

Print on the standard output.

See Also:
    https://rich.readthedocs.io/en/stable/reference/console.html
"""

STDERR: Final = console.Console(stderr=True)
"""A high level console interface instance.

Print on the standard error.

See Also:
    https://rich.readthedocs.io/en/stable/reference/console.html
"""
