# SPDX-FileCopyrightText: © 2025 Romain Brault <mail@romainbrault.com>
#
# SPDX-License-Identifier: MIT OR Apache-2.0

"""CLI runner fixture."""

import pytest
from click import testing


@pytest.fixture(scope="class")
def cli_runner() -> testing.CliRunner:
    """CLI Runner Fixture.

    Returns:
        A CliRunner instance.
    """
    return testing.CliRunner(mix_stderr=False)
