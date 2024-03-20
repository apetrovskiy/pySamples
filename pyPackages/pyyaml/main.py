from pprint import pprint
import yaml
from configuration import Configuration
from src.core.config.config_loader import load_config
from src.model.config.config import Config

CONFIG_FILE_NAME = "./config.yml"
CONFIG_FILE_NAME_2 = "test.yml"


def load_config_2(path: str) -> Config:
    with open(path, "r") as file:
        return yaml.load(file, Loader=yaml.Loader)


def load_config_3(path: str) -> Configuration:
    with open(path, "r") as file:
        return yaml.load(file, Loader=yaml.Loader)


def display_config(config: Config):
    print(
        "======================================== Config: ========================================"
    )
    pprint(config)
    print(config.postgres_config.database)
    print(config.timebase_config.server)
    print(
        "======================================== the end ========================================"
    )


def display_configuration(config: Configuration):
    print(
        "======================================== Configuaration: ========================================"
    )
    pprint(config)
    print(config.test1.test11.aaa)
    print(config.test1)
    print(config.test2.test21.eeee)
    # print(config.enum01)
    # print(config.enum01.name)
    # print(config.enum01.value)
    print(
        "======================================== the end! ========================================"
    )


config01 = load_config()
display_config(config=config01)


config02 = load_config_2(CONFIG_FILE_NAME)
display_config(config=config02)


config03 = load_config_3(CONFIG_FILE_NAME_2)
display_configuration(config=config03)


#######################


# test_data = Configuration()

# pprint(test_data)

with open(CONFIG_FILE_NAME, "r") as file:
    # config = yaml.safe_load(file)
    # config = yaml.load(file, Loader=yaml.Loader)
    config = yaml.load(file, Loader=yaml.Loader)

pprint(config)
