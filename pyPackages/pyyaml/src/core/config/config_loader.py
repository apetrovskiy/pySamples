import yaml
from src.model.config.config import Config


CONFIG_PATH = "config.yml"


def load_config() -> Config:
    stream = open(CONFIG_PATH, "r")
    return yaml.load(stream, Loader=yaml.Loader)
