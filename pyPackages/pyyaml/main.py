from pprint import pprint
import yaml
from configuration import Configuration
from src.core.config.config_loader import load_config
from src.model.config.config import Config

CONFIG_FILE_NAME = "./config.yml"  # "test.yml"


def load_config_2(path: str) -> Config:
    with open(path, "r") as file:
        return yaml.load(file, Loader=yaml.Loader)


def load_config_3(path: str) -> Configuration:
    with open(path, "r") as file:
        return yaml.load(file, Loader=yaml.Loader)


config01 = load_config()
pprint(config01)
print(config01.postgres_config.database)
print(
    "===================================================================================================="
)
config02 = load_config_2(CONFIG_FILE_NAME)
pprint(config02)
print(config02.timebase_config.server)
print(
    "===================================================================================================="
)
config03 = load_config_3("test.yml")
pprint(config03)
print(config03.test1.test11.aaa)
print(
    "===================================================================================================="
)

#######################


# test_data = Configuration()

# pprint(test_data)

with open(CONFIG_FILE_NAME, "r") as file:
    # config = yaml.safe_load(file)
    # config = yaml.load(file, Loader=yaml.Loader)
    config = yaml.load(file, Loader=yaml.Loader)

pprint(config)
