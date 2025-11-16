# TextEditor API Reference

## Core Modules

### FileManager

```python
from src.core.file_manager import FileManager

manager = FileManager()
content = manager.open_file("path/to/file.txt")
manager.save_file("path/to/file.txt", content)
```

### Settings

```python
from src.core.settings import Settings

settings = Settings()
font_size = settings.get("editor.fontSize", 11)
settings.set("editor.fontSize", 12)
settings.save_settings()
```

### LanguageRunner

```python
from src.core.language_runner import LanguageRunner

runner = LanguageRunner()
stdout, stderr = runner.run_code("print('Hello')", "python")
```

### LanguageRegistry

```python
from src.languages.language_registry import LanguageRegistry

registry = LanguageRegistry()
languages = registry.list_languages()
python_config = registry.get_language("Python")
```

## UI Components

### MainWindow

```python
from src.ui.main_window import MainWindow
window = MainWindow()
window.show()
```

### EditorWidget

```python
from src.ui.widgets.editor_widget import EditorWidget
editor = EditorWidget()
```

### FileExplorer

```python
from src.ui.widgets.file_explorer import FileExplorer
explorer = FileExplorer()
```

### OutputPanel

```python
from src.ui.widgets.output_panel import OutputPanel
output = OutputPanel()
```
