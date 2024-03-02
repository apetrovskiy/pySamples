from dataclasses import dataclass
import yaml


# @dataclass
class Test11(yaml.YAMLObject):
    # aaa: str
    # bbb: str
    yaml_tag = "tag:yaml.org,2002:configuration.Test11"

    # yaml_loader = yaml.SafeLoader
    def __init__(self, aaa: str, bbb: str):
        self.aaa = aaa
        self.bbb = bbb


# @dataclass
class Test12(yaml.YAMLObject):
    # ccc: str
    # ddd: str
    yaml_tag = "tag:yaml.org,2002:configuration.Test12"

    # yaml_loader = yaml.SafeLoader
    def __init__(self, ccc: str, ddd: str):
        self.ccc = ccc
        self.ddd = ddd


# @dataclass
class Test21(yaml.YAMLObject):
    # eeee: str
    yaml_tag = "tag:yaml.org,2002:configuration.Test21"

    # yaml_loader = yaml.SafeLoader
    def __init__(self, eeee: str):
        self.eeee = eeee


# @dataclass
class Test1(yaml.YAMLObject):
    # test11: Test11
    # test12: Test12
    yaml_tag = "tag:yaml.org,2002:configuration.Test1"

    # yaml_loader = yaml.Loader
    def __init__(self, test11: Test11, test12: Test12):
        self.test11 = test11
        self.test12 = test12


# @dataclass
class Test2(yaml.YAMLObject):
    # test21: Test21
    yaml_tag = "tag:yaml.org,2002:configuration.Test2"

    # yaml_loader = yaml.Loader
    def __init__(self, test21: Test21):
        self.test21 = test21


# @dataclass
class Configuration(yaml.YAMLObject):
    yaml_tag = "tag:yaml.org,2002:configuration.Configuration"
    # yaml_loader = yaml.Loader
    # test1: Test1
    # test2: Test2

    def __init__(self, test1: Test1, test2: Test2):
        self.test1 = test1
        self.test2 = test2


# class Config(yaml.YAMLObject):
#     yaml_tag = "tag:yaml.org,2002:src.model.config.config.Config"

#     def __init__(
#         self,
#         sqlite_config: SqliteConfig,
#         postgres_config: PostgresConfig,
#         timebase_config: TimebaseConfig,
#     ):
#         self.sqlite_config = sqlite_config
#         self.postgres_config = postgres_config
#         self.timebase_config = timebase_config
