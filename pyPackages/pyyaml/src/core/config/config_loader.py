import yaml
from src.model.config.config import Config


def load_config(file_path: str) -> Config:
    stream = open(file=file_path, mode="r")
    return yaml.load(stream, Loader=yaml.Loader)
