def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты."""
    first = card_number[0:4]
    second = card_number[4:6]
    last = card_number[12:16]
    masked = first + " " + second + "** **** " + last
    return masked


def get_mask_account(card_number: str) -> str:
    """Маскирует номер счета."""
    masked = "**" + card_number[-4:]
    return masked


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))
