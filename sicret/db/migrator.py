from sqlalchemy.exc import ResourceClosedError

from sicret.db.connection import Connection

TABLE_SCHEMAS = {
    "keys": """
CREATE TABLE IF NOT EXISTS keys (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT DEFAULT NULL,
    private_key TEXT NOT NULL,
    public_key TEXT NOT NULL,
    key_type TEXT NOT NULL DEFAULT 'CLIENT',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""",
    "contacts": """
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    public_key TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""",
}


def run_ddl(sql):
    try:
        Connection.session().query(sql)
    except ResourceClosedError:
        pass


def create_tables():
    db = Connection.session()

    for table_name, table_schema in TABLE_SCHEMAS.items():
        print(f"Checking for table '{table_name}' ")

        table_exists = db.query(
            f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';"
        ).first()

        if not table_exists:
            print(f"Table '{table_name}' does not exist. Creating now.")
            run_ddl(table_schema)


def drop_tables():
    db = Connection.session()

    for table_name in TABLE_SCHEMAS.keys():
        print(f"Dropping table '{table_name}' ")
        run_ddl(f"DROP TABLE IF EXISTS {table_name};")
