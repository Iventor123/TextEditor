"""Code execution and language running functionality."""

import subprocess
from typing import Tuple


class LanguageRunner:
    """Execute code in various programming languages."""

    def __init__(self):
        """Initialize language runner."""
        self.supported_languages = {
            'python': 'python',
            'javascript': 'node',
            'bash': 'bash',
        }

    def run_code(self, code: str, language: str = 'python') -> Tuple[str, str]:
        """Execute code and return stdout and stderr."""
        try:
            result = subprocess.run(
                [self.supported_languages.get(language, 'python'), '-c', code],
                capture_output=True,
                text=True,
                timeout=10
            )
            return result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            return "", "Error: Code execution timed out"
        except Exception as e:
            return "", f"Error: {str(e)}"
