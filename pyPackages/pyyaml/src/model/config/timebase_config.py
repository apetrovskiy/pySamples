import yaml


class TimebaseConfig(yaml.YAMLObject):
    yaml_tag = "tag:yaml.org,2002:src.model.config.timebase_config.TimebaseConfig"

    def __init__(
        self, server: str, port: int, database: str, username: str, password: str
    ):
        self.server = server
        self.port = port
        self.username = username
        self.password = password
