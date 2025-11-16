"""Output panel widget component."""

from PyQt6.QtWidgets import QPlainTextEdit


class OutputPanel(QPlainTextEdit):
    """Output panel for displaying code execution results."""

    def __init__(self, parent=None):
        """Initialize the output panel."""
        super().__init__(parent)
        self.setReadOnly(True)
        self.setPlaceholderText("Output will appear here...")
