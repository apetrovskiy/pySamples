from pprint import pprint
import yaml

CONFIG_FILE_NAMES = [
    "config_01.yaml",
    "config_02.yaml",
    "config_03.yaml",
    "config_04.yaml",
    "config_05.yaml",
    "config_06.yaml",
]


def load_config(file_name: str):
    with open(file_name, "r") as file_name:
        config: dict = yaml.safe_load(file_name)

    pprint(config, sort_dicts=False)

    print("----------------------------------------------------------------")

    # [pprint(f"a high-level item -> \n{item}") for item in config.items()]

    print("================================================================")


[load_config(config_file_name) for config_file_name in CONFIG_FILE_NAMES]
