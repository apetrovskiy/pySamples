from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
import ruamel.yaml


@dataclass
class Test11:
    aaa: str
    bbb: str
    # yaml_tag = "tag:yaml.org,2002:configuration.Test11"
    yaml_tag = "!configuration.Test11"

    def __init__(self, aaa: str, bbb: str):
        self.aaa = aaa
        self.bbb = bbb


@dataclass
class Test12:
    ccc: str
    ddd: str
    yaml_tag = "tag:yaml.org,2002:configuration.Test12"

    def __init__(self, ccc: str, ddd: str):
        self.ccc = ccc
        self.ddd = ddd


@dataclass
class Test21:
    # eeee: str
    yaml_tag = "tag:yaml.org,2002:configuration.Test21"

    def __init__(self, eeee: str):
        self.eeee = eeee


@dataclass
class Test1:
    yaml_tag = "tag:yaml.org,2002:configuration.Test1"
    test11: Test11
    test12: Test12

    def __init__(self, test11: Test11, test12: Test12):
        self.test11 = test11
        self.test12 = test12


@dataclass
class Test2:
    test21: Test21
    yaml_tag = "tag:yaml.org,2002:configuration.Test2"

    # def __init__(self, test21: Test21):
    #     self.test21 = test21


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
class Configuration:
    # yaml_tag = "tag:yaml.org,2002:configuration.Configuration"
    yaml_tag = "!configuration.Configuration"

    test1: Test1
    test2: Test2
    tests: List[Test1]
    tests2: Optional[List[Test2]]
    enum01: Enum01 = field(default=None, metadata={"by_value": True})

    def __init__(
        self,
        test1: Test1,
        test2: Test2,
        tests: List[Test1],
        tests2: Optional[List[Test2]],
    ):
        self.test1 = test1
        self.test2 = test2
        self.tests = tests
        self.tests2 = tests2
