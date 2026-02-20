from openpyxl import Workbook


def export_to_excel(results, filename="rename_result.xlsx"):
    wb = Workbook()
    ws = wb.active
    ws.title = "リネーム結果"

    ws.append(["元の名前(拡張子なし)", "サイズ(Bytes)"])

    for row_index, (stem, size) in enumerate(results, start=2):
        ws.cell(row=row_index, column=1, value=stem)
        size_cell = ws.cell(row=row_index, column=2, value=size)
        size_cell.number_format = "#,##0"

    wb.save(filename)
    print(f"Excelファイルを保存しました: {filename}")

