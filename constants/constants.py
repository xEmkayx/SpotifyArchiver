from enum import Enum

CACHE_FILE_NAME = 'cached_token.txt'


class ScriptType(Enum):
    RELEASE_RADAR = "release_radar"
    DISCOVER_WEEKLY = "discover_weekly"
