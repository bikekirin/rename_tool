def show_table(results):
    """
    リネーム結果をターミナルにテーブル表示する。

    Parameters
    ----------
    results : list[tuple[str, int]]
        (stem, size) のタプル配列
    """

    # 遅延インポート（テーブル表示時のみ依存）
    try:
        from rich.console import Console
        from rich.table import Table
    except ImportError:
        print("rich がインストールされていません。")
        print("以下を実行してください:")
        print("    pip install rich")
        return

    if not results:
        print("表示対象のデータがありません。")
        return

    try:
        console = Console()
        table = Table(title="リネーム結果")

        table.add_column("元の名前(拡張子なし)", justify="left")
        table.add_column("サイズ(Bytes)", justify="right")

        for stem, size in results:
            table.add_row(stem, f"{size:,}")

        console.print(table)

    except Exception as e:
        print("テーブル表示中にエラーが発生しました。")
        print(f"詳細: {e}")