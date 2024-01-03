import sqlite3
from pathlib import Path

from sicret.config import Config


class Connection:
    _session = None

    def __init__(self):
        if not Connection._session:
            self.config = Config.instance()
            self.path = self.config.path.parent / Config.get("database.name")
            Connection._session = sqlite3.connect(str(self.path))

    @classmethod
    def session(cls):
        if not cls._session:
            cls._session = cls()._session
        return cls._session

    @classmethod
    def query(cls, sql, params=None):
        cursor = cls.session().cursor()
        result = None

        if params is not None:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)

        # Check if the operation is an INSERT
        if sql.strip().upper().startswith("INSERT"):
            result = cursor.lastrowid
            cls.session().commit()
        elif cursor.description:  # This checks if the query returns data
            columns = [column[0] for column in cursor.description]
            rows = cursor.fetchall()
            result = [dict(zip(columns, row)) for row in rows]

        cursor.close()

        # Commit for non-query operations other than INSERT
        if not cursor.description and not sql.strip().upper().startswith("INSERT"):
            cls.session().commit()

        return result

    @classmethod
    def close(cls):
        if cls._session:
            cls._session.close()
            cls._session = None
