import json
from unittest.mock import mock_open, patch

from src.utils import get_financial_transactions


def test_get_financial_transactions_valid() -> None:
    """Проверка чтения валидного JSON-файла со списком операций."""
    mock_data = [{"id": 1, "amount": "100"}]
    mock_json = json.dumps(mock_data)

    with patch("builtins.open", mock_open(read_data=mock_json)):
        with patch("os.path.exists", return_value=True):
            result = get_financial_transactions("dummy_path.json")
            assert result == mock_data


def test_get_financial_transactions_not_list() -> None:
    """Проверка случая, когда JSON содержит словарь вместо списка."""
    mock_json = json.dumps({"key": "value"})

    with patch("builtins.open", mock_open(read_data=mock_json)):
        with patch("os.path.exists", return_value=True):
            result = get_financial_transactions("dummy_path.json")
            assert result == []


def test_get_financial_transactions_invalid_json() -> None:
    """Проверка обработки некорректного синтаксиса JSON."""
    with patch("builtins.open", mock_open(read_data="invalid json")):
        with patch("os.path.exists", return_value=True):
            result = get_financial_transactions("dummy_path.json")
            assert result == []


def test_get_financial_transactions_file_not_found() -> None:
    """Проверка работы, если файл не существует."""
    with patch("os.path.exists", return_value=False):
        result = get_financial_transactions("non_existent.json")
        assert result == []