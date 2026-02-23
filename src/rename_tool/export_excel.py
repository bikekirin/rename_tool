from openpyxl import Workbook


def export_excel(data, filename="rename_result.xlsx"):
    wb = Workbook()
    ws = wb.active
    ws.title = "Files"

    ws.append(["元の名前(拡張子なし)", "サイズ(Bytes)"])

    for item in data:
        ws.append([item["name"], item["size"]])

    wb.save(filename)

    print(f"Excelファイルを保存しました: {filename}")