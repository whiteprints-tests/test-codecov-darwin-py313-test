# SPDX-FileCopyrightText: © 2025 Romain Brault <mail@romainbrault.com>
#
# SPDX-License-Identifier: MIT OR Apache-2.0

"""Test the loc module."""

from pathlib import Path

from test_codecov_darwin_py313_test import loc


class TestLocalVariables:
    """Test the localization variables."""

    @staticmethod
    def test_locale_directory_is_a_valid_path() -> None:
        """Test whether the LOCALE_DIRECTORY is a valid Path."""
        assert isinstance(loc.LOCALE_DIRECTORY, Path), (
            "LOCALE_DIRECTORY is not an instance of `Path`"
        )

    @staticmethod
    def test_translation_functions_are_available() -> None:
        """Test whether the translation functions exists.

        The translation functions are `TRANSLATION` and `_`.
        """
        assert hasattr(loc, "TRANSLATION"), (
            "Translation function `TRANSLATION` not found."
        )
        assert hasattr(loc, "_"), "Translation function `_` not found."
