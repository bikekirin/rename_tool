def show_table(data):
    from rich.table import Table
    from rich.console import Console

    console = Console()
    table = Table(title="リネーム結果")

    table.add_column("元の名前(拡張子なし)")
    table.add_column("サイズ(Bytes)", justify="right")

    for item in data:
        table.add_row(
            item["name"],
            f"{item['size']:,}"
        )

    console.print(table)