"""Language registry for managing supported languages."""

import yaml
from pathlib import Path
from typing import Dict, Any


class LanguageRegistry:
    """Registry for programming language definitions."""

    def __init__(self):
        """Initialize language registry."""
        self.languages: Dict[str, Any] = {}
        self._load_definitions()

    def _load_definitions(self) -> None:
        """Load language definitions from YAML files."""
        definitions_dir = Path(__file__).parent / "definitions"
        if definitions_dir.exists():
            for yaml_file in definitions_dir.glob("*.yaml"):
                with open(yaml_file, 'r') as f:
                    config = yaml.safe_load(f)
                    if config:
                        lang_name = config.get('name', yaml_file.stem)
                        self.languages[lang_name] = config

    def get_language(self, name: str) -> Dict[str, Any]:
        """Get language definition by name."""
        return self.languages.get(name, {})

    def list_languages(self) -> list:
        """List all available languages."""
        return list(self.languages.keys())
