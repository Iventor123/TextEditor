"""Tests for file manager."""

import pytest
from src.core.file_manager import FileManager


def test_open_file(sample_file):
    """Test opening a file."""
    manager = FileManager()
    content = manager.open_file(sample_file)
    assert "Hello, World!" in content


def test_save_file(tmp_path):
    """Test saving a file."""
    manager = FileManager()
    test_file = tmp_path / "output.py"
    content = "print('Test')"
    
    assert manager.save_file(str(test_file), content)
    assert test_file.read_text() == content
