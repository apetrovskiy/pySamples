from pprint import pprint
import yaml
from configuration import Configuration
from src.core.config.config_loader import load_config
from src.model.config.config import Config

CONFIG_FILE_NAME = "./config.yml"
TEST_YAML_FILE_NAME_01 = "test01.yml"
TEST_YAML_FILE_NAME_02 = "test02.yml"


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
        "======================================== Configuration: ========================================"
    )
    pprint(config)
    if hasattr(config, "tests"):
        print(config.tests)
    if hasattr(config, "test1"):
        print(config.test1.test11.aaa)
        print(config.test1.test11.bbb)
        print(config.test1.test12.ccc)
        print(config.test1.test12.ddd)
    if hasattr(config, "test2"):
        print(config.test2.test21.eeee)
    if hasattr(config, "enum01"):
        print(config.enum01)
        # print(config.enum01.name)
        # print(config.enum01.value)
    print(
        "======================================== the end! ========================================"
    )


config01 = load_config(CONFIG_FILE_NAME)
display_config(config=config01)


config02 = load_config_2(CONFIG_FILE_NAME)
display_config(config=config02)


config03 = load_config_3(TEST_YAML_FILE_NAME_01)
display_configuration(config=config03)


config04 = load_config_3(TEST_YAML_FILE_NAME_02)
display_configuration(config=config04)


#######################


with open(CONFIG_FILE_NAME, "r") as file:
    # config = yaml.safe_load(file)
    # config = yaml.load(file, Loader=yaml.Loader)
    config = yaml.load(file, Loader=yaml.Loader)

pprint(config)
