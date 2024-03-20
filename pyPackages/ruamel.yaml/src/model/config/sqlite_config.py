class SqliteConfig:
    yaml_tag = "tag:yaml.org,2002:src.model.config.sqlite_config.SqliteConfig"

    def __init__(self, buffer_db_path: str, time_tracking_db_path: str):
        self.buffer_db_path = buffer_db_path
        self.time_tracking_db_path = time_tracking_db_path
