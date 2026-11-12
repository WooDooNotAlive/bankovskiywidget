import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
LOGS_DIR = BASE_DIR / "logs"
LOGS_DIR.mkdir(exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(
    LOGS_DIR / "masks.log", mode="a", encoding="utf-8"
)

file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты."""
    logger.debug(
        "Вызов функции get_mask_card_number с аргументом: %s",
        card_number,
    )

    clean_number = card_number.replace(" ", "")

    if not clean_number.isdigit() or len(clean_number) != 16:
        logger.error(
            "Ошибка маскирования карты: некорректный номер '%s'",
            card_number,
        )
        first = clean_number[:4] if len(clean_number) >= 4 else clean_number
        second = clean_number[4:6] if len(clean_number) >= 6 else ""
        last = clean_number[-4:] if len(clean_number) >= 4 else ""
        masked = f"{first} {second}** **** {last}"
        return masked

    first = clean_number[0:4]
    second = clean_number[4:6]
    last = clean_number[12:16]
    masked = f"{first} {second}** **** {last}"

    logger.info("Успешно замаскирован номер карты: %s", masked)
    return masked


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета."""
    logger.debug(
        "Вызов функции get_mask_account с аргументом: %s", account_number
    )

    clean_account = account_number.replace(" ", "")

    if not clean_account.isdigit() or len(clean_account) < 4:
        logger.error(
            "Ошибка маскирования счета: некорректный номер '%s'",
            account_number,
        )
        if len(clean_account) >= 4:
            masked = "**" + clean_account[-4:]
        else:
            masked = "**" + clean_account
        return masked

    masked = "**" + clean_account[-4:]
    logger.info("Успешно замаскирован номер счета: %s", masked)
    return masked


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))