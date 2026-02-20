from rich.table import Table
from rich.console import Console

console = Console()


def show_table(results):
    table = Table(title="リネーム結果")
    table.add_column("元の名前(拡張子なし)", justify="left")
    table.add_column("サイズ(Bytes)", justify="right")

    for stem, size in results:
        table.add_row(stem, f"{size:,}")

    console.print(table)
