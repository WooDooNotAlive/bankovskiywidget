"""Тестирование функций модуля masks."""

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1596837868705199", "1596 83** **** 5199"),
        ("1234567812345678", "1234 56** **** 5678"),
        ("0000000000000000", "0000 00** **** 0000"),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    """Проверка корректности маскирования номера карты."""
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135874305", "**4305"),
        ("35383033474447895560", "**5560"),
        ("123456", "**3456"),
        ("1234", "**1234"),
    ],
)
def test_get_mask_account(account_number: str, expected: str) -> None:
    """Проверка корректности маскирования номера счета."""
    assert get_mask_account(account_number) == expected