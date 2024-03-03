from src.model.config.postgres_config import PostgresConfig
from src.model.config.sqlite_config import SqliteConfig
from src.model.config.timebase_config import TimebaseConfig
import yaml


class Config(yaml.YAMLObject):
    yaml_tag = "tag:yaml.org,2002:src.model.config.config.Config"

    def __init__(
        self,
        sqlite_config: SqliteConfig,
        postgres_config: PostgresConfig,
        timebase_config: TimebaseConfig,
    ):
        self.sqlite_config = sqlite_config
        self.postgres_config = postgres_config
        self.timebase_config = timebase_config
