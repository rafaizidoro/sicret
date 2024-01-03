from typing import Annotated, Optional

import typer

from sicret.chat import ChatClient, ChatServer
from sicret.config import Config

app = typer.Typer()


@app.command()
def server(
    host: Annotated[str, typer.Argument(help="The host to listen")] = Config.get(
        "server.host"
    ),
    port: Annotated[int, typer.Argument(help="The port to listen")] = Config.get(
        "server.port"
    ),
):
    """
    Starts a sicret chat server.
    """

    print(f"Starting server at {host}:{port}")

    server = ChatServer(host=host, port=port)
    server.listen()


@app.command()
def client(
    host: Annotated[
        str, typer.Argument(help="The server host to connect to")
    ] = Config.get("client.host"),
    port: Annotated[
        int, typer.Argument(help="The server port to connect to")
    ] = Config.get("client.port"),
):
    """
    Starts a sicret chat client.
    """

    print(f"Connecting to {host}:{port}")

    client = ChatClient(host=host, port=port)
    client.run()
