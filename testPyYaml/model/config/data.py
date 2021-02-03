import yaml
from dataclasses import dataclass


# @dataclass
class Config(yaml.YAMLObject):
    # yaml_tag = u'!Config'
    def __init__(self, id: int, path: str):
        self.id = id
        self.path = path

    # id: int
    # path: str
    # is_it: bool
