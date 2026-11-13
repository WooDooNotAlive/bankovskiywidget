from src.search import process_bank_operations, process_bank_search


def test_process_bank_search_found() -> None:
    """Проверка поиска операций по существующему слову."""
    data = [
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
        {"description": "Перевод с карты на карту"},
    ]
    result = process_bank_search(data, "Перевод")
    assert len(result) == 2
    assert result[0]["description"] == "Перевод организации"
    assert result[1]["description"] == "Перевод с карты на карту"


def test_process_bank_search_empty_query() -> None:
    """Проверка поиска с пустой строкой запроса."""
    data = [{"description": "Перевод"}]
    result = process_bank_search(data, "")
    assert result == data


def test_process_bank_search_not_found() -> None:
    """Проверка поиска, когда ничего не найдено."""
    data = [{"description": "Открытие вклада"}]
    result = process_bank_search(data, "Оплата")
    assert result == []


def test_process_bank_operations_counter() -> None:
    """Проверка подсчета количества операций по категориям."""
    data = [
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
        {"description": "Перевод с карты на карту"},
    ]
    categories = ["Перевод", "Вклад"]
    result = process_bank_operations(data, categories)
    assert result == {"Перевод": 2, "Вклад": 1}
