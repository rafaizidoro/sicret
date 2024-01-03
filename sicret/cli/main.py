import typer

from sicret.cli import chat, key

app = typer.Typer()

app.add_typer(chat.app, name="chat")
app.add_typer(key.app, name="keys")
