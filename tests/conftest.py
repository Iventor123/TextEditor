"""Pytest configuration and fixtures."""

import pytest
from pathlib import Path


@pytest.fixture
def temp_project_dir(tmp_path):
    """Create a temporary project directory for testing."""
    return tmp_path


@pytest.fixture
def sample_file(tmp_path):
    """Create a sample file for testing."""
    test_file = tmp_path / "test.py"
    test_file.write_text("print('Hello, World!')")
    return str(test_file)
