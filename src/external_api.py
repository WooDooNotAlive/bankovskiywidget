import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY") or ""


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """Принимает словарь с транзакцией и возвращает сумму в рублях.

    Если транзакция в USD или EUR, обращается к внешнему API.
    """
    operation_amount = transaction.get("operationAmount", {})
    amount_str = operation_amount.get("amount", "0")
    currency_code = (
        operation_amount.get("currency", {}).get("code", "RUB")
    )

    try:
        amount = float(amount_str)
    except (ValueError, TypeError):
        return 0.0

    if currency_code == "RUB":
        return amount

    if currency_code in ("USD", "EUR"):
        url = (
            f"https://api.apilayer.com/exchangerates_data/convert"
            f"?to=RUB&from={currency_code}&amount={amount}"
        )
        headers: Dict[str, str] = {"apikey": API_KEY}
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                result = data.get("result")
                if result is not None:
                    return float(result)
        except requests.RequestException:
            return 0.0

    return 0.0