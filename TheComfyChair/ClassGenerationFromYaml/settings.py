"""A settings object."""

from dataclasses import dataclass, field
from dotenv import load_dotenv
import os

load_dotenv()

__all__: list[str] = ["SETTINGS"]


@dataclass
class Settings:
    client_secret: str = field(default="")
    tenant_id: str = field(default="")
    other: str = "someothersetting"

    def __post_init__(self):
        """Read and set the config object."""
        for name, _ in self.__dataclass_fields__.items():
            if match := os.getenv(name):
                setattr(self, name, match)


SETTINGS = Settings()
