from typing import Any

from src.product import Product


def test_product_init() -> None:
    """Проверка инициализации и работы геттера цены."""
    product = Product("iPhone 15", "Смартфон Apple", 129990.0, 10)
    assert product.name == "iPhone 15"
    assert product.description == "Смартфон Apple"
    assert product.price == 129990.0
    assert product.quantity == 10


def test_new_product_classmethod() -> None:
    """Проверка создания товара через класс-метод new_product."""
    data = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет",
        "price": 180000.0,
        "quantity": 5,
    }
    product = Product.new_product(data)
    assert isinstance(product, Product)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_price_setter_success() -> None:
    """Проверка успешной установки новой положительной цены."""
    product = Product("Телевизор", "4K OLED", 100000.0, 3)
    product.price = 120000.0
    assert product.price == 120000.0


def test_product_price_setter_negative(capsys: Any) -> None:
    """Проверка сеттера при установке отрицательной цены или нуля."""
    product = Product("Телевизор", "4K OLED", 100000.0, 3)

    product.price = -100
    captured = capsys.readouterr()
    assert product.price == 100000.0
    assert "Цена не должна быть нулевая или отрицательная" in captured.out

    product.price = 0
    captured = capsys.readouterr()
    assert product.price == 100000.0
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
