import yaml


from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from yaml import YAMLObject


@dataclass
class Test11(YAMLObject):
    aaa: str
    bbb: str
    yaml_tag = "tag:yaml.org,2002:configuration.Test11"

    # def __init__(self, aaa: str, bbb: str):
    #     self.aaa = aaa
    #     self.bbb = bbb


@dataclass
class Test12(YAMLObject):
    ccc: str
    ddd: str
    yaml_tag = "tag:yaml.org,2002:configuration.Test12"

    # def __init__(self, ccc: str, ddd: str):
    #     self.ccc = ccc
    #     self.ddd = ddd


@dataclass
class Test21(YAMLObject):
    # eeee: str
    yaml_tag = "tag:yaml.org,2002:configuration.Test21"

    def __init__(self, eeee: str):
        self.eeee = eeee


@dataclass
class Test1(YAMLObject):
    yaml_tag = "tag:yaml.org,2002:configuration.Test1"
    test11: Test11
    test12: Test12

    # def __init__(self, test11: Test11, test12: Test12):
    #     self.test11 = test11
    #     self.test12 = test12


@dataclass
class Test2(YAMLObject):
    test21: Test21
    yaml_tag = "tag:yaml.org,2002:configuration.Test2"

    # def __init__(self, test21: Test21):
    #     self.test21 = test21


"""
class Enum01(Enum):
    AAA = "aaaa"
    BBB = "bbbb"
    yaml_ta = "tag:yaml.org,2002:configuration.Enum01"

    def __init__(self, value) -> None:
        super().__init__()


# @dataclass
class Configuration(yaml.YAMLObject):
"""


@dataclass
class Enum01(Enum):
    # yaml_tag = "tag:yaml.org,2002:configuration.Enum01"
    AAA = "aaaa"
    BBB = "bbbb"

    # @classmethod
    # def __init__(cls, constructor, node):
    #     return cls[node.value]

    @classmethod
    def to_yaml(cls, representer, node):
        return representer.represent_sclar(f"!{cls.__name__}", "{.name}".format(node))

    @classmethod
    def from_yaml(cls, constructor, node):
        print("breakpoint hit")
        return cls[node.value]


@dataclass
class Configuration(YAMLObject):
    yaml_tag = "tag:yaml.org,2002:configuration.Configuration"

    test1: Test1
    test2: Test2
    tests: List[Test1] = field(default=None)
    tests2: Optional[List[Test2]] = field(default=None)
    enum01: Enum01 = field(default=None, metadata={"by_value": True})


# def __init__(self, test1: Test1, test2: Test2):
#     self.test1 = test1
#     self.test2 = test2
