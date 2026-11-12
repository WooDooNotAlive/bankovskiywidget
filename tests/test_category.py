from src.category import Category
from src.product import Product


def reset_counts() -> None:
    """Сброс счётчиков перед проверкой."""
    Category.category_count = 0
    Category.product_count = 0


def test_category_init() -> None:
    """Проверка инициализации атрибутов Category."""
    reset_counts()
    p1 = Product("iPhone", "Смартфон", 129990.0, 10)
    p2 = Product("Samsung", "Смартфон", 99990.0, 5)
    cat = Category("Смартфоны", "Мобильные устройства", [p1, p2])
    assert cat.name == "Смартфоны"
    assert cat.description == "Мобильные устройства"
    assert len(cat.products) == 2


def test_category_products_are_objects() -> None:
    """Проверка, что в products хранятся объекты Product."""
    reset_counts()
    p = Product("Наушники", "Беспроводные", 2990.0, 20)
    cat = Category("Аксессуары", "Периферия", [p])
    for product in cat.products:
        assert isinstance(product, Product)


def test_category_count() -> None:
    """Проверка подсчёта количества категорий."""
    reset_counts()
    assert Category.category_count == 0
    Category("Электроника", "Гаджеты", [])
    assert Category.category_count == 1
    Category("Одежда", "Вещи", [])
    assert Category.category_count == 2


def test_product_count() -> None:
    """Проверка подсчёта количества товаров."""
    reset_counts()
    assert Category.product_count == 0
    p1 = Product("A", "desc", 10.0, 1)
    p2 = Product("B", "desc", 20.0, 2)
    Category("Кат1", "desc", [p1, p2])
    assert Category.product_count == 2


def test_product_count_multiple_categories() -> None:
    """Проверка подсчёта товаров в нескольких категориях."""
    reset_counts()
    p1 = Product("A", "desc", 10.0, 1)
    p2 = Product("B", "desc", 20.0, 2)
    p3 = Product("C", "desc", 30.0, 3)
    Category("Кат1", "desc", [p1, p2])
    Category("Кат2", "desc", [p3])
    assert Category.category_count == 2
    assert Category.product_count == 3


def test_category_empty_products() -> None:
    """Проверка категории без товаров."""
    reset_counts()
    cat = Category("Пустая", "Нет товаров", [])
    assert len(cat.products) == 0
    assert Category.category_count == 1
    assert Category.product_count == 0
