import yaml
from model.config.data import Config


config = Config(111, "sss")

# with open('data.yaml') as f:
#     result = yaml.safe_load(f)
stream = open('data.yaml', 'r')
result = yaml.load(stream, Loader=yaml.Loader)

print(result)
print(result.id)
print(result.path)
