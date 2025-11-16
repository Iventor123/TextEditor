# Plugin Development Guide

## Creating a Plugin

All plugins must inherit from `PluginBase` and implement the required methods.

### Basic Plugin Template

```python
from src.plugins.plugin_base import PluginBase

class MyCustomPlugin(PluginBase):
    def __init__(self):
        super().__init__("MyCustomPlugin", "1.0.0")
    
    def activate(self):
        """Called when plugin is loaded."""
        print(f"{self.name} activated")
    
    def deactivate(self):
        """Called when plugin is unloaded."""
        print(f"{self.name} deactivated")
```

## Plugin Lifecycle

1. **Discovery**: Plugin files are located in the plugins directory
2. **Loading**: Plugin classes are imported and instantiated
3. **Activation**: `activate()` method is called
4. **Deactivation**: `deactivate()` method is called when unloading

## Plugin Manager Usage

```python
from src.plugins.plugin_manager import PluginManager

# Initialize manager
manager = PluginManager()

# Load a plugin
manager.load_plugin("path/to/plugin.py")

# Get plugin
plugin = manager.get_plugin("MyCustomPlugin")

# List all plugins
plugins = manager.list_plugins()
```

## Best Practices

1. Keep plugin functionality focused and single-purpose
2. Handle errors gracefully in activate/deactivate
3. Document plugin dependencies
4. Use semantic versioning for plugin versions
5. Test plugins thoroughly before distribution

## Plugin functionalities

### text manipulation
The text can be manipulated using the `textMan` class in `PluginBase`.