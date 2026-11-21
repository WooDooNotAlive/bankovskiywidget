import json
from unittest.mock import mock_open, patch

from src.utils import get_financial_transactions


def test_get_financial_transactions_valid() -> None:
    """Проверка чтения валидного JSON-файла со списком операций."""
    mock_data = [{"id": 1, "amount": "100"}]
    mock_json = json.dumps(mock_data)

    with patch("builtins.open", mock_open(read_data=mock_json)):
        with patch("src.utils.Path.exists", return_value=True):
            result = get_financial_transactions("dummy_path.json")
            assert result == mock_data


def test_get_financial_transactions_not_found() -> None:
    """Проверка возврата пустого списка, если файл не существует."""
    with patch("src.utils.Path.exists", return_value=False):
        result = get_financial_transactions("non_existent.json")
        assert result == []


def test_get_financial_transactions_invalid_json() -> None:
    """Проверка обработки битого JSON-файла."""
    with patch("builtins.open", mock_open(read_data="invalid json")):
        with patch("src.utils.Path.exists", return_value=True):
            result = get_financial_transactions("invalid.json")
            assert result == []


def test_get_financial_transactions_not_list() -> None:
    """Проверка возврата пустого списка, если в JSON не список."""
    mock_json = json.dumps({"not": "a list"})
    with patch("builtins.open", mock_open(read_data=mock_json)):
        with patch("src.utils.Path.exists", return_value=True):
            result = get_financial_transactions("not_list.json")
            assert result == []
