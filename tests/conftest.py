from typing import Any

import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def sample_operations() -> list[dict[str, Any]]:
    """Фикстура с тестовыми операциями."""
    return [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383035158229126723",
        },
        {
            "id": 938307366,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916901",
            "to": "Счет 55701053066177296068",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод организации",
            "from": "Visa Visa 1234567812345678",
            "to": "Счет 35383035158229126723",
        },
        {
            "id": 123456,
            "state": "CANCELED",
            "date": "2018-07-20T00:00:00.000000",
            "operationAmount": {
                "amount": "100.00",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Открытие вклада",
            "from": "Visa 1111222233334444",
            "to": "Счет 5555666677778888",
        },
    ]


@pytest.fixture
def empty_operations() -> list[dict[str, Any]]:
    """Фикстура с пустым списком операций."""
    return []


@pytest.fixture
def operations_same_date() -> list[dict[str, Any]]:
    """Фикстура с операциями за одинаковую дату."""
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "100.00",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод",
            "from": "Visa 1111222233334444",
            "to": "Счет 5555666677778888",
        },
        {
            "id": 2,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "200.00",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод",
            "from": "Visa 1111222233334444",
            "to": "Счет 5555666677778888",
        },
    ]


@pytest.fixture
def transactions_data() -> list[dict[str, Any]]:
    """Фикстура для генераторов транзакций."""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916901",
            "to": "Счет 55701053066177296068",
        },
        {
            "id": 142239672,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.428788",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243225858087",
            "to": "Счет 60882182232096786500",
        },
        {
            "id": 873106593,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.256401",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44841659020303414585",
            "to": "Счет 89658882055656565545",
        },
        {
            "id": 895315405,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Individual 6831982476737658",
            "to": "Счет 35383035158229126723",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод организации",
            "from": "Visa Visa 1234567812345678",
            "to": "Счет 35383035158229126723",
        },
    ]


@pytest.fixture
def first_product() -> Product:
    """Фикстура первого товара."""
    return Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
    )


@pytest.fixture
def second_product() -> Product:
    """Фикстура второго товара."""
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def third_product() -> Product:
    """Фикстура третьего товара."""
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def first_category(
    first_product: Product, second_product: Product, third_product: Product
) -> Category:
    """Фикстура категории товаров."""
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения"
        " дополнительных функций для удобства жизни",
        [first_product, second_product, third_product],
    )