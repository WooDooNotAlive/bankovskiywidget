from src.file_readers import read_csv_file, read_excel_file
from src.processing import filter_by_state, sort_by_date
from src.search import process_bank_search
from src.utils import get_financial_transactions
from src.widget import get_date, mask_account_card


def get_amount_and_currency(item: dict) -> tuple[str, str]:
    """Извлекает сумму и код валюты из словаря транзакции."""
    op_amount = item.get("operationAmount")
    if isinstance(op_amount, dict):
        amount = str(op_amount.get("amount", ""))
        curr_info = op_amount.get("currency", {})
        curr = str(curr_info.get("code") or curr_info.get("name") or "руб.")
    else:
        amount = str(item.get("amount", ""))
        curr = str(
            item.get("currency_code")
            or item.get("currency_name")
            or "руб."
        )

    if curr in ("RUB", "RUB."):
        curr = "руб."
    return amount, curr


def filter_rub_transactions(data: list[dict]) -> list[dict]:
    """Фильтрует транзакции, оставляя только рублевые."""
    result = []
    for item in data:
        _, curr = get_amount_and_currency(item)
        if curr == "руб.":
            result.append(item)
    return result


def main() -> None:
    """Основная функция программы для интерактивного взаимодействия."""
    print(
        "Привет! Добро пожаловать в программу работы "
        "с банковскими транзакциями.\n"
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла"
    )

    choice = input("\nПользователь: ").strip()

    if choice == "1":
        print("\nПрограмма: Для обработки выбран JSON-файл.")
        transactions = get_financial_transactions("data/operations.json")
    elif choice == "2":
        print("\nПрограмма: Для обработки выбран CSV-файл.")
        transactions = read_csv_file("data/transactions.csv")
    elif choice == "3":
        print("\nПрограмма: Для обработки выбран XLSX-файл.")
        transactions = read_excel_file("data/transactions_excel.xlsx")
    else:
        print("\nПрограмма: Некорректный выбор пункта меню.")
        return

    valid_statuses = {"EXECUTED", "CANCELED", "PENDING"}
    while True:
        print(
            "\nПрограмма: Введите статус, по которому необходимо выполнить "
            "фильтрацию.\nДоступные для фильтровки статусы: EXECUTED, "
            "CANCELED, PENDING"
        )
        status_input = input("\nПользователь: ").strip().upper()
        if status_input in valid_statuses:
            break
        print(f'\nПрограмма: Статус операции "{status_input}" недоступен.')

    transactions = filter_by_state(transactions, status_input)
    print(f'\nПрограмма: Операции отфильтрованы по статусу "{status_input}"')

    print("\nПрограмма: Отсортировать операции по дате? Да/Нет")
    sort_choice = input("\nПользователь: ").strip().lower()
    if sort_choice == "да":
        print("\nПрограмма: Отсортировать по возрастанию или по убыванию?")
        order_choice = input("\nПользователь: ").strip().lower()
        reverse = order_choice != "по возрастанию"
        transactions = sort_by_date(transactions, reverse=reverse)

    print("\nПрограмма: Выводить только рублевые транзакции? Да/Нет")
    rub_choice = input("\nПользователь: ").strip().lower()
    if rub_choice == "да":
        transactions = filter_rub_transactions(transactions)

    print(
        "\nПрограмма: Отфильтровать список транзакций по определенному "
        "слову в описании? Да/Нет"
    )
    search_choice = input("\nПользователь: ").strip().lower()
    if search_choice == "да":
        search_word = input("\nПользователь (введите слово): ").strip()
        transactions = process_bank_search(transactions, search_word)

    print("\nПрограмма: Распечатываю итоговый список транзакций...\n")

    if not transactions:
        print(
            "Программа: Не найдено ни одной транзакции, "
            "подходящей под ваши условия фильтрации"
        )
        return

    print(f"Всего банковских операций в выборке: {len(transactions)}\n")
    for item in transactions:
        raw_date = str(item.get("date", ""))
        formatted_date = get_date(raw_date) if raw_date else ""
        description = item.get("description", "")

        from_info = str(item.get("from", "")) if item.get("from") else ""
        to_info = str(item.get("to", "")) if item.get("to") else ""

        from_masked = mask_account_card(from_info) if from_info else ""
        to_masked = mask_account_card(to_info) if to_info else ""

        if from_masked and to_masked:
            route = f"{from_masked} -> {to_masked}"
        elif to_masked:
            route = to_masked
        else:
            route = from_masked

        amount, curr = get_amount_and_currency(item)

        print(f"{formatted_date} {description}".strip())
        if route:
            print(route)
        print(f"Сумма: {amount} {curr}\n")


if __name__ == "__main__":
    main()
