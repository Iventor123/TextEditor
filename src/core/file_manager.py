"""File management functionality."""

import os
from pathlib import Path


class FileManager:
    """Handle file operations like opening, saving, and managing projects."""

    def __init__(self):
        """Initialize the file manager."""
        self.current_project = None
        self.open_files = []

    def open_file(self, filepath: str) -> str:
        """Open and read a file."""
        path = Path(filepath)
        if path.exists():
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        return ""

    def save_file(self, filepath: str, content: str) -> bool:
        """Save content to a file."""
        try:
            path = Path(filepath)
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        except Exception as e:
            print(f"Error saving file: {e}")
            return False
