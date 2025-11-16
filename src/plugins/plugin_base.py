"""Base plugin interface."""

from abc import ABC, abstractmethod


class PluginBase(ABC):
    """Base class for all plugins."""

    def __init__(self, name: str, version: str = "1.0.0"):
        """Initialize plugin."""
        self.name = name
        self.version = version

    @abstractmethod
    def activate(self) -> None:
        """Activate the plugin."""
        pass

    @abstractmethod
    def deactivate(self) -> None:
        """Deactivate the plugin."""
        pass
