import yaml
from model.config import Config


config = Config()

with open('data.yaml') as f:
    result = yaml.safe_load(f)

print(result)
