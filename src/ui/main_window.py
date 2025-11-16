"""Main application window."""

import sys
from pathlib import Path
from PyQt6.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QSplitter
from PyQt6.QtCore import Qt

# Add project root to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from src.ui.widgets.editor_widget import EditorWidget
from src.ui.widgets.file_explorer import FileExplorer


class MainWindow(QMainWindow):
    """Main application window."""

    def __init__(self):
        """Initialize the main window."""
        super().__init__()
        self.setWindowTitle("TextEditor")
        self.setGeometry(100, 100, 1200, 800)
        
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout (horizontal: file explorer on left, editor on right)
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)
        
        # File explorer (left panel)
        self.file_explorer = FileExplorer()
        
        # Editor (right panel)
        self.editor = EditorWidget()
        
        # Add splitter to make panels resizable
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.addWidget(self.file_explorer)
        splitter.addWidget(self.editor)
        splitter.setStretchFactor(0, 1)  # File explorer: 1/4 width
        splitter.setStretchFactor(1, 3)  # Editor: 3/4 width
        
        main_layout.addWidget(splitter)
        
        self.show()