from typing import Annotated, Optional

import typer

from sicret.cli.ui import show_table
from sicret.config import Config
from sicret.crypto import Key

app = typer.Typer()

from rich import print


@app.command()
def create(
    name: Annotated[str, typer.Argument(help="The alias name for this key")] = None,
):
    """
    Creates a new keypair
    """

    key = Key.build().save(name=name)

    print(f"Key {key.name} created successfully")


@app.command()
def list():
    """
    List all keys
    """

    keys = Key.find_all()

    show_table("Keys", keys, only=["id", "name", "created_at"])


@app.command()
def get(
    name: Annotated[str, typer.Argument(help="The alias name for the key")],
    output_key: Annotated[bool, typer.Option()] = False,
):
    """
    Get a key by name
    """

    key = Key.find_one(name)

    if not key:
        print(f"Key {name} not found")
        return

    if output_key:
        print(key.public_key)
    else:
        print(key)
