from pathlib import Path

APP_NAME = "TextEditor"
APP_VERSION = "0.1.0"

# Directory / file names (used by code; actual locations resolved at runtime)
DEFAULT_CONFIG_FILENAME = "default_settings.yaml"
USER_SETTINGS_FILENAME = "settings.yaml"
RECENT_FILES_FILENAME = "recent_files.json"

# Limits and defaults that are NOT user-facing editable (but can be changed by dev)
MAX_RECENT_FILES = 20
FILE_READ_CHUNK = 64 * 1024  # bytes

# Supported file types / extensions (used by detectors & runners)
SUPPORTED_EXTENSIONS = {
    "python": [".py"],
    "javascript": [".js", ".mjs"],
    "html": [".html", ".htm"],
}

# Default editor values (still considered constants; user can override in settings)
DEFAULT_FONT_FAMILY = "Consolas"
DEFAULT_FONT_SIZE = 11

# Resource locations (relative to package src/)
PACKAGE_ROOT = Path(__file__).resolve().parent.parent
RESOURCES_DIR = PACKAGE_ROOT / "resources"
LANG_DEFS_DIR = RESOURCES_DIR / "languages"

# Keys used in settings file — keep consistent across code
SETTINGS_KEYS = {
    "window": "window",
    "editor": "editor",
    "plugins": "plugins",
}
