from src.product import Product


def test_product_init() -> None:
    """Проверка инициализации атрибутов Product."""
    product = Product("iPhone 15", "Смартфон Apple", 129990.0, 10)
    assert product.name == "iPhone 15"
    assert product.description == "Смартфон Apple"
    assert product.price == 129990.0
    assert product.quantity == 10


def test_product_types() -> None:
    """Проверка типов атрибутов Product."""
    product = Product("Наушники", "Беспроводные", 2990.5, 100)
    assert isinstance(product.name, str)
    assert isinstance(product.description, str)
    assert isinstance(product.price, float)
    assert isinstance(product.quantity, int)


def test_product_custom_values() -> None:
    """Проверка создания Product с произвольными данными."""
    product = Product("Чехол", "Силиконовый", 490.0, 50)
    assert product.name == "Чехол"
    assert product.price == 490.0
    assert product.quantity == 50
