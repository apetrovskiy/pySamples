class PostgresConfig:
    yaml_tag = "tag:yaml.org,2002:src.model.config.postgres_config.PostgresConfig"

    def __init__(
        self, server: str, port: int, database: str, username: str, password: str
    ):
        self.server = server
        self.port = port
        self.database = database
        self.username = username
        self.password = password
