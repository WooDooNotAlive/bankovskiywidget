# BankWidget

Проект банковского виджета: маскирование карты/счета и обработка операций.

## Установка

```
python -m venv .venv
.venv\Scripts\activate
```

## Использование

filter_by_state — фильтр операций по state (по умолчанию EXECUTED):

```python
from src.processing import filter_by_state

data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

print(filter_by_state(data))
print(filter_by_state(data, "CANCELED"))
```

sort_by_date — сортировка по дате (по умолчанию сначала новые):

```python
from src.processing import sort_by_date

print(sort_by_date(data))
print(sort_by_date(data, reverse=False))
```

Маскирование:

```python
from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date

print(get_mask_card_number("7000792289606361"))
print(get_mask_account("73654108430135874305"))
print(mask_account_card("Maestro 1596837868705199"))
print(get_date("2024-03-11T02:26:18.671407"))
```
