"""Модуль с фикстурами для тестов pytest."""

import pytest


@pytest.fixture
def sample_operations() -> list[dict]:
    """Фикстура возвращает список операций с разными статусами и датами."""
    return [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
        {
            "id": 938307366,
            "state": "CANCELED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 57769032667130285945",
            "to": "Счет 89506691456184518776",
        },
        {
            "id": 615064591,
            "state": "EXECUTED",
            "date": "2018-10-14T08:21:33.419441",
            "operationAmount": {
                "amount": "43512.18",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Platinum 1246377376369388",
            "to": "Visa Classic 6831982476737658",
        },
    ]


@pytest.fixture
def empty_operations() -> list[dict]:
    """Фикстура возвращает пустой список операций."""
    return []


@pytest.fixture
def operations_same_date() -> list[dict]:
    """Фикстура возвращает операции с одинаковыми датами."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T10:00:00.000000"},
        {"id": 2, "state": "EXECUTED", "date": "2023-01-01T10:00:00.000000"},
    ]