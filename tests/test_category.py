import pytest

from src.category import Category, CategoryIterator
from src.product import LawnGrass, Product, Smartphone


def test_category_init(first_category: Category) -> None:
    """Проверка инициализации категории."""
    assert first_category.name == "Смартфоны"
    assert Category.category_count >= 1


def test_category_str(first_category: Category) -> None:
    """Проверка строкового отображения категории."""
    assert str(first_category) == "Смартфоны, количество продуктов: 27 шт."


def test_add_product_success(first_category: Category) -> None:
    """Проверка добавления валидного товара."""
    new_prod = Product("Test Phone", "Desc", 1000.0, 2)
    initial_count = Category.product_count
    first_category.add_product(new_prod)
    assert Category.product_count == initial_count + 1
    assert "Test Phone" in first_category.products


def test_add_product_subclass(first_category: Category) -> None:
    """Проверка добавления наследников Product (Smartphone, LawnGrass)."""
    phone = Smartphone("P", "D", 100.0, 1, 99.0, "M", 128, "Red")
    grass = LawnGrass("G", "D", 50.0, 5, "RU", "3 days", "Green")
    first_category.add_product(phone)
    first_category.add_product(grass)
    assert "P" in first_category.products
    assert "G" in first_category.products


def test_add_product_type_error(first_category: Category) -> None:
    """Проверка исключения TypeError при добавлении стороннего объекта."""
    with pytest.raises(TypeError):
        first_category.add_product("Не товар")  # type: ignore


def test_category_iterator(first_category: Category) -> None:
    """Проверка работы итератора."""
    iterator = CategoryIterator(first_category)
    items = list(iterator)
    assert len(items) == 3
    assert items[0].name == "Samsung Galaxy S23 Ultra"
