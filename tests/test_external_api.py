from unittest.mock import MagicMock, patch

from src.external_api import convert_to_rub


def test_convert_to_rub_currency_rub() -> None:
    """Проверка возврата суммы для рублевой транзакции без обращения к API."""
    transaction = {
        "operationAmount": {
            "amount": "1500.50",
            "currency": {"code": "RUB"},
        }
    }
    assert convert_to_rub(transaction) == 1500.50


@patch("requests.get")
def test_convert_to_rub_usd(mock_get: MagicMock) -> None:
    """Проверка конвертации USD через внешнее API с использованием Mock."""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 9000.0}
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {"code": "USD"},
        }
    }
    result = convert_to_rub(transaction)
    assert result == 9000.0
    mock_get.assert_called_once()


@patch("requests.get")
def test_convert_to_rub_api_failure(mock_get: MagicMock) -> None:
    """Проверка обработки ошибки сервера API (status_code != 200)."""
    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {"code": "EUR"},
        }
    }
    assert convert_to_rub(transaction) == 0.0


def test_convert_to_rub_invalid_amount() -> None:
    """Проверка обработки некорректной суммы."""
    transaction = {
        "operationAmount": {
            "amount": "invalid",
            "currency": {"code": "RUB"},
        }
    }
    assert convert_to_rub(transaction) == 0.0