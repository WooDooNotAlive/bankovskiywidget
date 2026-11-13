"""Тестирование функций модуля generators."""

from typing import List

import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


@pytest.mark.parametrize(
    "currency, expected_count",
    [
        ("USD", 3),
        ("RUB", 2),
        ("EUR", 0),
    ],
)
def test_filter_by_currency(
    transactions_data: list[dict], currency: str, expected_count: int
) -> None:
    """Проверка фильтрации транзакций по различным валютам."""
    usd_generator = filter_by_currency(transactions_data, currency)
    result = list(usd_generator)
    assert len(result) == expected_count
    assert all(
        item["operationAmount"]["currency"]["code"] == currency
        for item in result
    )


def test_filter_by_currency_empty() -> None:
    """Проверка работы filter_by_currency с пустым списком."""
    assert list(filter_by_currency([], "USD")) == []


def test_transaction_descriptions(transactions_data: list[dict]) -> None:
    """Проверка получения описаний транзакций по очереди."""
    descriptions = transaction_descriptions(transactions_data)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Перевод организации"


def test_transaction_descriptions_empty() -> None:
    """Проверка работы transaction_descriptions с пустым списком."""
    assert list(transaction_descriptions([])) == []


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (
            9999999999999998,
            9999999999999999,
            [
                "9999 9999 9999 9998",
                "9999 9999 9999 9999",
            ],
        ),
    ],
)
def test_card_number_generator(
    start: int, stop: int, expected: List[str]
) -> None:
    """Проверка генерации номеров карт в заданных диапазонах."""
    assert list(card_number_generator(start, stop)) == expected
