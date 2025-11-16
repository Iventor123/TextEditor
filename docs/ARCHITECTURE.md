# TextEditor Architecture

## Project Structure Overview

```
src/
├── ui/              # User interface components
├── editor/          # Core editor functionality
├── core/            # Business logic (file management, settings, execution)
├── plugins/         # Plugin system
├── languages/       # Language definitions and registry
└── utils/           # Utility functions and constants
```

## Key Design Decisions

### Separation of Concerns
- **UI Layer** (`src/ui/`): All PyQt6 components and GUI logic
- **Editor Logic** (`src/editor/`): Editor core, syntax highlighting, autocompletion
- **Business Logic** (`src/core/`): File operations, settings, language execution
- **Plugin System** (`src/plugins/`): Extensibility through well-defined interfaces

### Plugin Architecture
- Plugins inherit from `PluginBase` and implement `activate()`/`deactivate()` methods
- Enables modular feature development without core modifications
- Plugins are loaded dynamically from the plugins directory

### Language Support
- YAML-based language definitions for easy extensibility
- `LanguageRegistry` manages supported languages
- `LanguageRunner` handles code execution

## Module Dependencies

```
main.py
  └── src.ui.main_window
      ├── src.ui.widgets.editor_widget
      ├── src.ui.widgets.file_explorer
      ├── src.ui.widgets.output_panel
      └── src.core (all modules)
```

## Development Guidelines

1. **Add new UI components** to `src/ui/widgets/`
2. **Extend editor functionality** in `src/editor/`
3. **Add new business logic** to `src/core/`
4. **Create plugins** in `src/plugins/examples/` following `PluginBase`
5. **Add language support** by creating YAML definitions in `src/languages/definitions/`
