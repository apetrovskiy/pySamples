import ruamel.yaml
from src.model.config.postgres_config import PostgresConfig
from src.model.config.sqlite_config import SqliteConfig
from src.model.config.timebase_config import TimebaseConfig
from src.model.config.config import Config


CONFIG_PATH = "config.yml"


def register_classes_01():
    yaml = ruamel.yaml.YAML()
    yaml.register_class(Config)
    yaml.register_class(PostgresConfig)
    yaml.register_class(SqliteConfig)
    yaml.register_class(TimebaseConfig)
    return yaml


def load_config() -> Config:
    stream = open(CONFIG_PATH, "r")
    return register_classes_01().load(stream)
