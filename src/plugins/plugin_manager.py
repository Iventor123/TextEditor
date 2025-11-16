"""Plugin manager for loading and managing plugins."""

import importlib.util
from pathlib import Path
from typing import Dict, List

from .plugin_base import PluginBase


class PluginManager:
    """Manage plugin lifecycle and discovery."""

    def __init__(self, plugin_dir: str = None):
        """Initialize plugin manager."""
        self.plugin_dir = Path(plugin_dir) if plugin_dir else Path(__file__).parent / "examples"
        self.plugins: Dict[str, PluginBase] = {}

    def load_plugin(self, plugin_path: str) -> bool:
        """Load a plugin from a file path."""
        try:
            spec = importlib.util.spec_from_file_location("plugin", plugin_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            # Find plugin class
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, type) and issubclass(attr, PluginBase) and attr is not PluginBase:
                    plugin = attr()
                    self.plugins[plugin.name] = plugin
                    plugin.activate()
                    return True
            return False
        except Exception as e:
            print(f"Error loading plugin: {e}")
            return False

    def get_plugin(self, name: str) -> PluginBase:
        """Get a loaded plugin by name."""
        return self.plugins.get(name)

    def list_plugins(self) -> List[str]:
        """List all loaded plugins."""
        return list(self.plugins.keys())
