import json
import logging
from pathlib import Path
from typing import Any, Dict, List

# Путь к папке logs в корне проекта (BankWidget/logs)
BASE_DIR = Path(__file__).resolve().parent.parent
LOGS_DIR = BASE_DIR / "logs"
LOGS_DIR.mkdir(exist_ok=True)

# 1. Создание логера для модуля utils
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# 2. Настройка file_handler (перезапись файла mode="w")
file_handler = logging.FileHandler(
    LOGS_DIR / "utils.log", mode="w", encoding="utf-8"
)

# 3. Настройка форматера
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)

# 4. Добавление хендлера к логеру
logger.addHandler(file_handler)


def get_financial_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Считывает данные о финансовых транзакциях из JSON-файла.

    Принимает путь к файлу. Возвращает список словарей.
    Если файл пустой, не найден или содержит не-список, возвращает [].
    """
    logger.debug(
        "Вызов функции get_financial_transactions с путем: %s",
        file_path,
    )

    path = Path(file_path)

    if not path.exists():
        logger.error("Файл не найден по пути: %s", file_path)
        return []

    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info(
                    "Успешно получены транзакции из %s. Количество: %d",
                    file_path,
                    len(data),
                )
                return data

            logger.error(
                "Содержимое файла %s не список. Получен тип: %s",
                file_path,
                type(data).__name__,
            )
            return []

    except json.JSONDecodeError as e:
        logger.error(
            "Ошибка чтения JSON в файле %s: %s", file_path, e
        )
        return []
    except OSError as e:
        logger.error(
            "Ошибка ввода-вывода с файлом %s: %s", file_path, e
        )
        return []


if __name__ == "__main__":
    transactions = get_financial_transactions(
        "../data/operations.json"
    )
    print(f"Загружено транзакций: {len(transactions)}")
