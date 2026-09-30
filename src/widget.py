from datetime import datetime

try:
    from src.masks import get_mask_account, get_mask_card_number
except ImportError:
    from masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account_info: str) -> str:
    """Маскирует номер карты или счёта в строке вида 'Название Номер'."""
    if not card_or_account_info or not isinstance(card_or_account_info, str):
        return ""

    parts = card_or_account_info.strip().split()

    if len(parts) < 2:
        return ""

    number = parts[-1]
    name = " ".join(parts[:-1])

    if not number.isdigit():
        return ""

    if name.lower().startswith("счет") or name.lower().startswith("счёт"):
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    if not masked_number:
        return ""

    return f"{name} {masked_number}"


def get_date(date_string: str) -> str:
    """Преобразует дату из ISO-формата в строку вида ДД.ММ.ГГГГ."""
    if not date_string or not isinstance(date_string, str):
        return ""

    try:
        dt = datetime.fromisoformat(date_string)
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        return ""


if __name__ == "__main__":
    print(mask_account_card("Maestro 1596837868705199"))
    print(get_date("2024-03-11T02:26:18.671407"))
