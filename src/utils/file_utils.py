"""File utility functions."""

from pathlib import Path
from typing import List


def get_file_extension(filepath: str) -> str:
    """Get the file extension."""
    return Path(filepath).suffix


def is_valid_file(filepath: str) -> bool:
    """Check if a file exists and is readable."""
    path = Path(filepath)
    return path.exists() and path.is_file()


def get_files_in_directory(directory: str, recursive: bool = True) -> List[str]:
    """Get all files in a directory."""
    path = Path(directory)
    if not path.exists():
        return []
    
    pattern = "**/*" if recursive else "*"
    return [str(f) for f in path.glob(pattern) if f.is_file()]
