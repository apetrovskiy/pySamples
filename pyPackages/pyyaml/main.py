from pprint import pprint
import yaml
from configuration import Configuration
from src.core.config.config_loader import load_config
from src.model.config.config import Config

CONFIG_FILE_NAME = "./config.yml"
CONFIG_FILE_NAME_2 = "test.yml"
CONFIG_FILE_NAME_3 = "test2.yml"


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
    print(config.test1)
    print(config.test1.test11.aaa)
    print(config.test1.test11.bbb)
    print(config.test1.test12.ccc)
    print(config.test1.test12.ddd)
    print(config.test2.test21.eeee)
    print(config.enum01)
    # print(config.enum01.name)
    # print(config.enum01.value)
    print(
        "======================================== the end! ========================================"
    )


config01 = load_config()
# <<<<<<< HEAD
display_config(config=config01)


# =======
# pprint(config01)
# pprint(config01.postgres_config)
# print(config01.postgres_config.database)
# print(
#     "===================================================================================================="
# )
# >>>>>>> develop
config02 = load_config_2(CONFIG_FILE_NAME)
display_config(config=config02)


config03 = load_config_3(CONFIG_FILE_NAME_2)
# <<<<<<< HEAD
display_configuration(config=config03)

# =======
# pprint(config03)
# print(config03.test1.test11.aaa)
# print(config03.test1)
# print(config03.test2.test21.eeee)
# pprint(config03.tests)
# pprint(config03.tests2)
# # print(config03.enum01)
# # print(config03.enum01.name)
# # print(config03.enum01.value)
# print(
#     "===================================================================================================="
# )
# >>>>>>> develop

config04=load_config_3(CONFIG_FILE_NAME_3)
display_configuration(config=config04)

#######################


# test_data = Configuration()

# pprint(test_data)

with open(CONFIG_FILE_NAME, "r") as file:
    # config = yaml.safe_load(file)
    # config = yaml.load(file, Loader=yaml.Loader)
    config = yaml.load(file, Loader=yaml.Loader)

pprint(config)
