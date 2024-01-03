from dataclasses import asdict, dataclass
from datetime import datetime

from sicret.crypto.keyutils import decrypt_message, encrypt_message, generate_keys
from sicret.db.connection import Connection
from sicret.utils import random_name


@dataclass
class Key:
    public_key: str
    private_key: str = None
    name: str = None
    id: int = None
    created_at: datetime = None

    def dump(self):
        return asdict(self)

    def encrypt(self, content, content_type='message'):
        if content_type == 'message':
            return self.encrypt_message(content)

    def decrypt(self, content, content_type='message'):
        if content_type == 'message':
            return self.decrypt_message(content)

    def save(self, name=None):
        if not self.name:
            self.name = name or random_name()

        params = (self.name, self.private_key, self.public_key, self.created_at)

        inserted_id = Connection.query(
            "INSERT INTO keys (name, private_key, public_key, created_at) VALUES (?, ?, ?, ?)",
            params,
        )

        self.id = inserted_id

        return self

    @classmethod
    def build(cls):
        private_key, public_key = generate_keys()

        return Key(
            private_key=private_key,
            public_key=public_key,
            created_at=datetime.utcnow().isoformat(),
        )

    @classmethod
    def find_all(cls):
        keys = Connection.query("SELECT id, name, public_key, created_at FROM keys")

        return [Key(**key) for key in keys]

    @classmethod
    def find_one(cls, name):
        key = Connection.query(
            "SELECT id, name, public_key, created_at FROM keys WHERE name = ?", (name,)
        )

        if key:
            return Key(**key[0])
