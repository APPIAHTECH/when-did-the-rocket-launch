from enum import Enum
from typing import Final

from app.models.color import Color
from app.models.size import Size


class Environment(str, Enum):
    LOCAL = "LOCAL"
    TESTING = "TESTING"
    STAGING = "STAGING"
    PRODUCTION = "PRODUCTION"

    @property
    def is_debug(self):
        return self in (self.LOCAL, self.STAGING, self.TESTING)

    @property
    def is_testing(self):
        return self == self.TESTING

    @property
    def is_deployed(self) -> bool:
        return self in (self.STAGING, self.PRODUCTION)

    @staticmethod
    def use_env(env: str):
        try:
            return Environment[env.upper()]
        except KeyError:
            raise ValueError(f"Invalid environment: {env}")


VIDEO_NAME: Final = "Falcon Heavy Test Flight (Hosted Webcast)-wbSwFU6tY1c"
DISPLAY_SIZE: Final = Size(int(480 * 1.5), int(270 * 1.5))
BLACK: Final = Color(0, 0, 0)
