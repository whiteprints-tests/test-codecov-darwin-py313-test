# SPDX-FileCopyrightText: © 2025 Romain Brault <mail@romainbrault.com>
#
# SPDX-License-Identifier: MIT OR Apache-2.0

"""Test the exception module."""

import re
from typing import Final

import pytest
from hypothesis import given
from hypothesis import strategies as st

from test_codecov_darwin_py313_test.cli import exception


SLUG_REGEX: Final = r"^[a-z0-9]+(?:-[a-z0-9]+)*$"


@given(st.from_regex(SLUG_REGEX))
def test_is_valid_slug(slug: str) -> None:
    """Check if the slug is valid."""
    is_valid = exception.is_valid_slug(slug)

    if is_valid:
        assert re.fullmatch(SLUG_REGEX, slug) is not None, (
            f"A valid slug should match the regular expression '{SLUG_REGEX}'."
        )
    else:
        with pytest.raises(exception.InvalidAppNameError):
            exception.check_app_name(slug)
