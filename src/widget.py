from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account_info: str) -> str:
    """Маскирует карту или счет."""
    if not card_or_account_info or not isinstance(card_or_account_info, str):
        return ""

    words = card_or_account_info.strip().split()

    if len(words) < 2:
        return ""

    number = "".join(w for w in words if w.isdigit())
    name = " ".join(w for w in words if not w.isdigit())

    if not number or not name:
        return ""

    if name.lower().startswith("счет") or name.lower().startswith("счёт"):
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    if not masked_number:
        return ""

    return f"{name} {masked_number}"


def get_date(date_string: str) -> str:
    """Переводит дату из ISO в ДД.ММ.ГГГГ."""
    if not date_string or not isinstance(date_string, str):
        return ""

    try:
        dt = datetime.fromisoformat(date_string)
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        return ""


if __name__ == "__main__":
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("Visa 1234 5678 9012 3456"))
    print(get_date("2024-03-11T02:26:18.671407"))