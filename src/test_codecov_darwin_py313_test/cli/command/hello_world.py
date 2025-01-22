# SPDX-FileCopyrightText: © 2025 Romain Brault <mail@romainbrault.com>
#
# SPDX-License-Identifier: MIT OR Apache-2.0

"""The 'Hello world' command."""

import importlib

import rich_click as click

from test_codecov_darwin_py313_test.loc import _


@click.command(name=_("hello-world"), help=_("Say 'Hello, World!'."))
def hello_world() -> None:
    """This is a demonstration command.

    Print "Hello, World!" on the standard output.

    Remove or edit this function to build your own CLI!
    """
    console = importlib.import_module(
        "test_codecov_darwin_py313_test.console", __package__
    )
    console.STDOUT.print("Hello, World!")
