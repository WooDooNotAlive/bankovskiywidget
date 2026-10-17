"""Тестирование функций модуля processing."""

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state, expected_count",
    [
        ("EXECUTED", 2),
        ("CANCELED", 2),
        ("PENDING", 0),
    ],
)
def test_filter_by_state(
    sample_operations: list[dict], state: str, expected_count: int
) -> None:
    """Проверка фильтрации по различным статусам state."""
    result = filter_by_state(sample_operations, state=state)
    assert len(result) == expected_count
    assert all(item["state"] == state for item in result)


def test_filter_by_state_default(sample_operations: list[dict]) -> None:
    """Проверка фильтрации со значением state по умолчанию (EXECUTED)."""
    result = filter_by_state(sample_operations)
    assert len(result) == 2
    assert all(item["state"] == "EXECUTED" for item in result)


def test_filter_by_state_empty(empty_operations: list[dict]) -> None:
    """Проверка фильтрации пустого списка операций."""
    result = filter_by_state(empty_operations)
    assert result == []


def test_sort_by_date_descending(sample_operations: list[dict]) -> None:
    """Проверка сортировки по дате по убыванию (по умолчанию)."""
    sorted_ops = sort_by_date(sample_operations)
    dates = [op["date"] for op in sorted_ops]
    assert dates == sorted(dates, reverse=True)
    assert sorted_ops[0]["id"] == 41428829


def test_sort_by_date_ascending(sample_operations: list[dict]) -> None:
    """Проверка сортировки по дате по возрастанию."""
    sorted_ops = sort_by_date(sample_operations, reverse=False)
    dates = [op["date"] for op in sorted_ops]
    assert dates == sorted(dates, reverse=False)
    assert sorted_ops[0]["id"] == 938307366


def test_sort_by_date_empty(empty_operations: list[dict]) -> None:
    """Проверка сортировки пустого списка."""
    assert sort_by_date(empty_operations) == []


def test_sort_by_date_same_dates(operations_same_date: list[dict]) -> None:
    """Проверка сортировки операций с одинаковыми датами."""
    sorted_ops = sort_by_date(operations_same_date)
    assert len(sorted_ops) == 2