import re
from collections import Counter
from typing import Any, Dict, List


def process_bank_search(
    data: List[Dict[str, Any]], search: str
) -> List[Dict[str, Any]]:
    """Ищет транзакции, у которых в описании есть заданная строка search.

    Использует библиотеку re для поиска без учета регистра.
    """
    if not search:
        return data

    pattern = re.compile(re.escape(search), re.IGNORECASE)
    result = []
    for item in data:
        description = str(item.get("description", ""))
        if pattern.search(description):
            result.append(item)
    return result


def process_bank_operations(
    data: List[Dict[str, Any]], categories: List[str]
) -> Dict[str, int]:
    """Подсчитывает количество операций для каждой категории из списка.

    Использует Counter из библиотеки collections.
    """
    category_counts: Counter[str] = Counter()
    categories_lower = [c.lower() for c in categories]

    for item in data:
        desc = str(item.get("description", "")).lower()
        for cat, cat_lower in zip(categories, categories_lower):
            if cat_lower in desc:
                category_counts[cat] += 1

    return dict(category_counts)
