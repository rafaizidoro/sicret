from pathlib import Path

import tomli
import tomli_w

DEFAULT_PATH = Path.home() / ".sicret" / "config.toml"


DEFAULT_CONFIG = {
    "client": {"host": "127.0.0.1", "port": 6969, "name": "default"},
    "server": {
        "host": "127.0.0.1",
        "port": 6969,
    },
    "database": {
        "name": "sicret.db",
    },
}


class Config:
    _instance = None

    @classmethod
    def instance(cls, path=None):
        if cls._instance is None:
            cls._instance = Config(path=path)

        return cls._instance

    def __init__(self, path=None):
        self.path = Path(path) if path else DEFAULT_PATH
        self.data = self.load_data()

    def load_data(self):
        if not self.path.parent.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)

        if not self.path.exists():
            data = DEFAULT_CONFIG

            with open(self.path, "wb") as file:
                tomli_w.dump(data, file)
        else:
            with open(self.path, "rb") as file:
                data = tomli.load(file)

        return data

    @classmethod
    def get(cls, uri):
        keys = uri.split(".")

        data = cls.instance().data

        for key in keys:
            if isinstance(data, dict) and key in data:
                data = data[key]
            else:
                return None  # or some default value if you prefer
        return data
