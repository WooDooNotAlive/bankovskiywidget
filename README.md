# BankWidget

Проект банковского виджета: маскирование карт/счетов, обработка операций, генераторы и декораторы логирования.

## Установка

```bash
python -m venv .venv
.venv\Scripts\activate

1. Фильтрация и сортировка операций (processing)
filter_by_state — фильтр операций по state (по умолчанию EXECUTED):

Использование
1. Фильтрация и сортировка операций (processing)
filter_by_state — фильтр операций по state (по умолчанию EXECUTED):

Python

from src.processing import filter_by_state

data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
]

print(filter_by_state(data))
sort_by_date — сортировка по дате (по умолчанию сначала новые):

Python

from src.processing import sort_by_date

print(sort_by_date(data))
2. Маскирование данных (masks, widget)
Python

from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card

print(get_mask_card_number("7000792289606361"))
print(get_mask_account("73654108430135874305"))
print(mask_account_card("Maestro 1596837868705199"))
print(get_date("2024-03-11T02:26:18.671407"))
3. Генераторы данных (generators)
filter_by_currency(transactions, currency) — фильтрация по заданной валюте.
transaction_descriptions(transactions) — поочередный вывод описаний операций.
card_number_generator(start, stop) — генерация номеров карт.
Python

from src.generators import card_number_generator

for card in card_number_generator(1, 3):
    print(card)
4. Декоратор логирования (decorators)
Модуль decorators содержит декоратор @log, который автоматически логирует детали выполнения функций (результаты работы или исключения).

Python

from src.decorators import log

# Запись в файл:
@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)
# В файл mylog.txt запишется: my_function ok

# Вывод в консоль:
@log
def divide(x, y):
    return x / y

divide(1, 0)
# В консоль выведется: divide error: ZeroDivisionError. Inputs: (1, 0), {}