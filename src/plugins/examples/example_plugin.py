"""Example plugin implementation."""

from ..plugin_base import PluginBase


class ExamplePlugin(PluginBase):
    """Example plugin demonstrating the plugin system."""

    def __init__(self):
        """Initialize example plugin."""
        super().__init__("ExamplePlugin", "1.0.0")

    def activate(self) -> None:
        """Activate the plugin."""
        print(f"Plugin {self.name} activated")

    def deactivate(self) -> None:
        """Deactivate the plugin."""
        print(f"Plugin {self.name} deactivated")
