"""File explorer widget component."""

from PyQt6.QtWidgets import QTreeWidget, QTreeWidgetItem


class FileExplorer(QTreeWidget):
    """File explorer widget for browsing project files."""

    def __init__(self, parent=None):
        """Initialize the file explorer."""
        super().__init__(parent)
        self.setHeaderLabel("Files")
