"""Editor widget component."""

from PyQt6.QtWidgets import QPlainTextEdit


class EditorWidget(QPlainTextEdit):
    """Main text editor widget."""

    def __init__(self, parent=None):
        """Initialize the editor widget."""
        super().__init__(parent)
        self.setPlaceholderText("Start typing...")
