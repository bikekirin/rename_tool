def export_to_excel(results, filename="rename_result.xlsx"):
    """
    リネーム結果をExcelファイルに出力する。

    Parameters
    ----------
    results : list[tuple[str, int]]
        (stem, size) のタプル配列
    filename : str
        保存するExcelファイル名
    """

    # 遅延インポート（Excel出力時のみ依存）
    try:
        from openpyxl import Workbook
    except ImportError:
        print("openpyxl がインストールされていません。")
        print("以下を実行してください:")
        print("    pip install openpyxl")
        return

    if not results:
        print("出力対象のデータがありません。")
        return

    try:
        wb = Workbook()
        ws = wb.active
        ws.title = "リネーム結果"

        # ヘッダー
        ws.append(["元の名前(拡張子なし)", "サイズ(Bytes)"])

        # データ書き込み
        for row_index, (stem, size) in enumerate(results, start=2):
            ws.cell(row=row_index, column=1, value=stem)

            size_cell = ws.cell(row=row_index, column=2, value=size)
            size_cell.number_format = "#,##0"  # 3桁区切り

        wb.save(filename)
        print(f"Excelファイルを保存しました: {filename}")

    except Exception as e:
        print("Excel出力中にエラーが発生しました。")
        print(f"詳細: {e}")