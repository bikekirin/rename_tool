import csv


def export_to_csv(results, filename="rename_result.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        writer.writerow(["元の名前(拡張子なし)", "サイズ(Bytes)"])

        for stem, size in results:
            writer.writerow([stem, f"{size:,}"])

    print(f"CSVファイルを保存しました: {filename}")


def export_to_tsv(results, filename="rename_result.tsv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter="\t")

        writer.writerow(["元の名前(拡張子なし)", "サイズ(Bytes)"])

        for stem, size in results:
            writer.writerow([stem, f"{size:,}"])

    print(f"TSVファイルを保存しました: {filename}")
