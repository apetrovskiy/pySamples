from pprint import pprint
import yaml

CONFIG_FILE_NAME = "config_2.yaml"  # "config.yml" # "config.yaml"

with open(CONFIG_FILE_NAME, "r") as file:
    config: dict = yaml.safe_load(file)

pprint(config, sort_dicts=False)

[pprint(f"a high-level item -> {item}") for item in config.items()]
