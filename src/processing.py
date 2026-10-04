def filter_by_state(
    operations: list[dict], state: str = "EXECUTED"
) -> list[dict]:
    """Фильтрует операции по статусу state."""
    result = []
    for operation in operations:
        if operation["state"] == state:
            result.append(operation)
    return result


def sort_by_date(operations: list[dict], reverse: bool = True) -> list[dict]:
    """Сортирует операции по дате."""
    result = sorted(operations, key=lambda x: x["date"], reverse=reverse)
    return result
