import csv


def export_tsv(data, filename="rename_result.tsv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerow(["元の名前(拡張子なし)", "サイズ(Bytes)"])

        for item in data:
            writer.writerow([item["name"], item["size"]])

    print(f"TSVファイルを保存しました: {filename}")