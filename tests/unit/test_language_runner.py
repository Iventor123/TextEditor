"""Tests for language runner."""

import pytest
from src.core.language_runner import LanguageRunner


def test_run_python_code():
    """Test running Python code."""
    runner = LanguageRunner()
    stdout, stderr = runner.run_code("print('test')", 'python')
    assert "test" in stdout
