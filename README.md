# rename_tool

ファイル一覧を取得し、サイズ情報を表示し、
Excel / CSV / TSV 形式でエクスポートできるCLIツールです。

---

## 🔧 Features

- 指定ディレクトリ内のファイル一覧を取得
- ファイルサイズを表示
- rich によるテーブル表示
- Excel (.xlsx) 出力
- CSV 出力
- TSV 出力
- --dry-run 対応

---

## 🖥 Requirements

- Python 3.10+
- pip

---

## 📦 Installation

### 1. Clone repository

```bash
git clone git@github.com:bikekirin/rename_tool.git
cd rename_tool

## Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

## Install dependencies
pip install -r requirements.txt

## Basic usage
rename_tool <target_directory>

## Dry run mode
rename_tool <target_directory> --dry-run

## Example
rename_tool ~/test_files --dry-run

### Output example:
対象ファイル数: 4 件
+----------------------+---------------+
| 元の名前(拡張子なし) | サイズ(Bytes) |
+----------------------+---------------+
| file1                | 6             |
| file2                | 12            |
| bigfile              | 5242880       |
| data                 | 0             |
+----------------------+---------------+

Excelファイルを保存しました: rename_result.xlsx
CSVファイルを保存しました: rename_result.csv
TSVファイルを保存しました: rename_result.tsv

## Project Structure
rename_tool/
├── src/
│   └── rename_tool/
│       ├── main.py
│       ├── table_view.py
│       ├── export_excel.py
│       ├── export_csv.py
│       └── __init__.py
├── tests/
├── requirements.txt
└── README.md

