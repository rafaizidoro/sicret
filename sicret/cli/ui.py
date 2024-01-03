from typing import Dict, List

from rich.console import Console
from rich.table import Table


def sanitize(items: List[Dict]) -> List[Dict]:
    for item in items:
        for key, value in item.items():
            if isinstance(value, bytes):
                item[key] = value.decode("utf-8")
            if isinstance(value, int):
                item[key] = str(value)

    return items


def show_table(title: str = None, items: List[Dict] = None, exclude=None, only=None):
    table = Table(expand=True, show_lines=True, header_style="bold green")

    if not isinstance(items[0], dict):
        items = [item.dump() for item in items]

    if only:
        for key in items[0].keys():
            if key not in only:
                items = [{k: v for k, v in item.items() if k != key} for item in items]
    elif exclude:
        for key in exclude:
            items = [{k: v for k, v in item.items() if k != key} for item in items]

    for key in items[0].keys():
        table.add_column(key)

    items = sanitize(items)

    for item in items:
        table.add_row(*item.values())

    console = Console()
    console.print(table)
