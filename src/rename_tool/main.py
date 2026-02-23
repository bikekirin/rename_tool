import argparse
from pathlib import Path

from rename_tool.table_view import show_table
from rename_tool.export_excel import export_excel
from rename_tool.export_csv import export_csv
from rename_tool.export_tsv import export_tsv


def main():
    parser = argparse.ArgumentParser(description="サイズ付きリネームCLI")
    parser.add_argument("directory")
    parser.add_argument("--dry-run", action="store_true", help="変更せず確認のみ")
    parser.add_argument("--csv", action="store_true")
    parser.add_argument("--excel", action="store_true")
    parser.add_argument("--tsv", action="store_true")

    args = parser.parse_args()

    target_dir = Path(args.directory)

    if not target_dir.exists():
        print("指定ディレクトリが存在しません")
        return

    files = sorted(
        [f for f in target_dir.iterdir() if f.is_file() and not f.name.startswith(".")]
    )

    print(f"\n対象ファイル数: {len(files)} 件\n")

    file_data = []

    for f in files:
        size = f.stat().st_size
        new_name = f"{f.stem}_{size}{f.suffix}"
        new_path = f.with_name(new_name)

        file_data.append({
            "name": f.stem,
            "size": size
        })

        if args.dry_run:
            print(f"[DRY-RUN] {f.name} → {new_name}")
        else:
            print(f"{f.name} → {new_name}")
            f.rename(new_path)

    if not args.dry_run:
        print("\nリネームを実行しました。\n")
    else:
        print("\n※ dry-run のため変更は行われていません\n")

    show_table(file_data)

    export_all = not (args.csv or args.excel or args.tsv)

    if args.csv or export_all:
        export_csv(file_data)

    if args.excel or export_all:
        export_excel(file_data)

    if args.tsv or export_all:
        export_tsv(file_data)


if __name__ == "__main__":
    main()