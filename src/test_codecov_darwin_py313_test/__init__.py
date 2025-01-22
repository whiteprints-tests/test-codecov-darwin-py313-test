# SPDX-FileCopyrightText: © 2025 Romain Brault <mail@romainbrault.com>
#
# SPDX-License-Identifier: MIT OR Apache-2.0

"""Top-level module."""

import importlib
from typing import Final

from test_codecov_darwin_py313_test.environment import (
    ENVIRONMENT_FILE,
    load_dotenv,
)
from test_codecov_darwin_py313_test.package_metadata import __version__


__all__: Final = ["__version__"]
"""Public module attributes."""


if __debug__:
    beartype = importlib.import_module("beartype")
    beartype_claw = importlib.import_module("beartype.claw")
    beartype_claw.beartype_this_package(
        conf=beartype.BeartypeConf(is_color=False),
    )

load_dotenv(ENVIRONMENT_FILE)
