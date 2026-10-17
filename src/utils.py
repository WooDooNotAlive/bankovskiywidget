import json
import os
from typing import Any, Dict, List


def get_financial_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Считывает данные о финансовых транзакциях из JSON-файла.

    Принимает путь к файлу. Возвращает список словарей.
    Если файл пустой, не найден или содержит не-список, возвращает [].
    """
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, OSError):
        return []