"""Модуль генераторов для обработки транзакций и банковских карт."""

from typing import Any, Dict, Iterator, List


def filter_by_currency(
    transactions: List[Dict[str, Any]], currency: str
) -> Iterator[Dict[str, Any]]:
    """Фильтрует список транзакций по заданной валюте и возвращает итератор."""
    for transaction in transactions:
        op_amount = transaction.get("operationAmount", {})
        curr = op_amount.get("currency", {})
        if curr.get("code") == currency:
            yield transaction


def transaction_descriptions(
    transactions: List[Dict[str, Any]]
) -> Iterator[str]:
    """Генератор, возвращающий описание каждой операции из списка транзакций."""
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX

    в заданном диапазоне от start до stop включительно.
    """
    for number in range(start, stop + 1):
        str_number = f"{number:016d}"
        formatted_card = (
            f"{str_number[:4]} {str_number[4:8]} "
            f"{str_number[8:12]} {str_number[12:]}"
        )
        yield formatted_card