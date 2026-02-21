def export_to_csv(results, filename="rename_result.csv"):
    """
    リネーム結果をCSVファイルに出力する。

    Parameters
    ----------
    results : list[tuple[str, int]]
        (stem, size) のタプル配列
    filename : str
        保存するCSVファイル名
    """

    # 遅延インポート（CSV出力時のみ依存）
    try:
        import csv
    except ImportError:
        print("csvモジュールの読み込みに失敗しました。")
        return

    if not results:
        print("出力対象のデータがありません。")
        return

    try:
        with open(filename, mode="w", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f)

            # ヘッダー
            writer.writerow(["元の名前(拡張子なし)", "サイズ(Bytes)"])

            # データ
            for stem, size in results:
                writer.writerow([stem, size])

        print(f"CSVファイルを保存しました: {filename}")

    except Exception as e:
        print("CSV出力中にエラーが発生しました。")
        print(f"詳細: {e}")