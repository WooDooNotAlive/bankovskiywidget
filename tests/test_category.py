from src.category import Category
from src.product import Product


def reset_counts() -> None:
    """Вспомогательный сброс счетчиков."""
    Category.category_count = 0
    Category.product_count = 0


def test_category_init_and_products_getter() -> None:
    """Проверка инициализации категории и работы геттера products."""
    reset_counts()
    p1 = Product("Samsung Galaxy S23 Ultra", "256GB", 180000.0, 5)
    p2 = Product("Iphone 15", "512GB", 210000.0, 8)
    cat = Category("Смартфоны", "Мобильные телефоны", [p1, p2])

    expected = (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )
    assert cat.products == expected


def test_add_product() -> None:
    """Проверка добавления товара через add_product."""
    reset_counts()
    p1 = Product("Samsung", "Desc", 100.0, 2)
    cat = Category("Электроника", "Гаджеты", [p1])

    assert Category.product_count == 1

    p2 = Product("iPhone", "Desc", 200.0, 3)
    cat.add_product(p2)

    assert Category.product_count == 2
    assert "iPhone, 200.0 руб. Остаток: 3 шт.\n" in cat.products


def test_category_and_product_counts() -> None:
    """Проверка корректности работы счетчиков категорий и товаров."""
    reset_counts()
    p1 = Product("A", "D", 10.0, 1)
    p2 = Product("B", "D", 20.0, 2)
    p3 = Product("C", "D", 30.0, 3)

    c1 = Category("Кат1", "D", [p1, p2])
    c2 = Category("Кат2", "D", [p3])

    assert c1.name == "Кат1"
    assert c2.name == "Кат2"
    assert Category.category_count == 2
    assert Category.product_count == 3
