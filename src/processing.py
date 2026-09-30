from typing import Any


def filter_by_state(
    operations: list[dict[str, Any]], state: str = "EXECUTED"
) -> list[dict[str, Any]]:
    """Возвращает операции, у которых ключ state совпадает с переданным значением."""
    return [operation for operation in operations if operation.get("state") == state]
