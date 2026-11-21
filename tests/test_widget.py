"""Тестирование функций модуля widget."""

import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("МИР 1234567812345678", "МИР 1234 56** **** 5678"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счёт 73654108430135874305", "Счёт **4305"),
        ("счет 35383033474447895560", "счет **5560"),
    ],
)
def test_mask_account_card_valid(input_data: str, expected: str) -> None:
    """Проверка корректности маскирования различных типов карт и счетов."""
    assert mask_account_card(input_data) == expected


@pytest.mark.parametrize(
    "invalid_input",
    [
        "",
        "   ",
        "1234567812345678",
        "Visa",
        "Visa 1234abc5678",
        None,
        12345,
    ],
)
def test_mask_account_card_invalid(invalid_input: str) -> None:
    """Проверка обработки некорректных входных данных."""
    assert mask_account_card(invalid_input) == ""


@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2018-06-30T02:08:58.425572", "30.06.2018"),
        ("2023-12-31T23:59:59.000000", "31.12.2023"),
        ("2020-01-01T00:00:00", "01.01.2020"),
    ],
)
def test_get_date_valid(date_str: str, expected: str) -> None:
    """Проверка правильности преобразования корректных дат ISO."""
    assert get_date(date_str) == expected


@pytest.mark.parametrize(
    "invalid_date",
    [
        "",
        "   ",
        "not-a-date",
        "2024-13-45T00:00:00",
        "11.03.2024",
        None,
        12345678,
    ],
)
def test_get_date_invalid(invalid_date: str) -> None:
    """Проверка обработки некорректных входных значений даты."""
    assert get_date(invalid_date) == ""
