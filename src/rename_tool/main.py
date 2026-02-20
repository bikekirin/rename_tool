import os
import re
import argparse
from pathlib import Path

from rename_tool.table_view import show_table
from rename_tool.export_excel import export_to_excel
from rename_tool.export_csv import export_to_csv, export_to_tsv


def has_size_suffix(filename_stem):
    """
    末尾が _数字 になっているか判定
    例: file_1234 → True
    """
    return re.search(r"_\d+$", filename_stem) is not None


def main():
    parser = argparse.ArgumentParser(description="ファイル名にサイズを付加するツール")
    parser.add_argument("target_dir", help="対象フォルダのパス")
    parser.add_argument("--dry-run", action="store_true", help="リネームせず確認のみ")

    args = parser.parse_args()
    target_path = Path(args.target_dir)

    if not target_path.exists():
        print("指定フォルダが存在しません。")
        return

    if not target_path.is_dir():
        print("指定パスはフォルダではありません。")
        return

    results = []

    for file_path in target_path.iterdir():
        if not file_path.is_file():
            continue

        stem = file_path.stem
        suffix = file_path.suffix

        # 既に _サイズ が付いているものは除外
        if has_size_suffix(stem):
            continue

        size = file_path.stat().st_size

        new_name = f"{stem}_{size}{suffix}"
        new_path = file_path.with_name(new_name)

        results.append((stem, size))

        if not args.dry_run:
            file_path.rename(new_path)

    if not results:
        print("対象ファイルがありません。")
        return

    # ファイル数表示
    print(f"\n対象ファイル数: {len(results)} 件")


    # 表示
    show_table(results)

    # 出力（正式仕様）
    export_to_excel(results)
    export_to_csv(results)
    export_to_tsv(results)


if __name__ == "__main__":
    main()
