"""Application settings management."""

import json
from pathlib import Path
from typing import Any, Dict


class Settings:
    """Manage application settings and preferences."""

    def __init__(self, config_dir: str = None):
        """Initialize settings manager."""
        self.config_dir = Path(config_dir) if config_dir else Path.home() / ".texteditor"
        self.config_dir.mkdir(exist_ok=True)
        self.config_file = self.config_dir / "settings.json"
        self.settings: Dict[str, Any] = self._load_settings()

    def _load_settings(self) -> Dict[str, Any]:
        """Load settings from file."""
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                return json.load(f)
        return {}

    def save_settings(self) -> None:
        """Save settings to file."""
        with open(self.config_file, 'w') as f:
            json.dump(self.settings, f, indent=2)

    def get(self, key: str, default: Any = None) -> Any:
        """Get a setting value."""
        return self.settings.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set a setting value."""
        self.settings[key] = value
    
    def get_all_settings(self) -> Dict[str, Any]:
        """Get all settings and return them."""
        return self.settingsµ
    def _reset_settings(self) -> None:
        """Reset all settings to default."""
        self.settings = {}
        self.save_settings()