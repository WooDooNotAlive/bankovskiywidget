from pathlib import Path
from typing import Any, Dict, List

import pandas as pd


def read_csv_file(file_path: str) -> List[Dict[str, Any]]:
    """Считывает данные о финансовых транзакциях из CSV-файла.

    Принимает путь к CSV-файлу. Возвращает список словарей.
    В случае если файл пустой, не найден или произошла ошибка чтения,
    возвращает пустой список [].
    """
    path = Path(file_path)
    if not path.exists():
        return []

    try:
        df = pd.read_csv(path, encoding="utf-8")
        if df.empty:
            return []
        df = df.fillna("")
        return list(df.to_dict(orient="records"))
    except Exception:
        return []


def read_excel_file(file_path: str) -> List[Dict[str, Any]]:
    """Считывает данные о финансовых транзакциях из Excel-файла (.xlsx).

    Принимает путь к XLSX-файлу. Возвращает список словарей.
    В случае если файл пустой, не найден или произошла ошибка чтения,
    возвращает пустой список [].
    """
    path = Path(file_path)
    if not path.exists():
        return []

    try:
        df = pd.read_excel(path)
        if df.empty:
            return []
        df = df.fillna("")
        return list(df.to_dict(orient="records"))
    except Exception:
        return []
