import pytest

from src.product import BaseProduct, LawnGrass, Product, Smartphone


def test_base_product_instantiation() -> None:
    """Проверка запрета создания экземпляра абстрактного класса BaseProduct."""
    with pytest.raises(TypeError):
        BaseProduct()  # type: ignore


def test_print_mixin(capsys: pytest.CaptureFixture[str]) -> None:
    """Проверка работы миксина логирования при создании продукта."""
    Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
    )
    captured = capsys.readouterr()
    assert (
        "Product('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)"
        in captured.out
    )


def test_product_init(first_product: Product) -> None:
    """Проверка корректной инициализации продукта."""
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert (
        first_product.description == "256GB, Серый цвет, 200MP камера"
    )
    assert first_product.price == 180000.0
    assert first_product.quantity == 5


def test_product_str(first_product: Product) -> None:
    """Проверка строкового представления продукта."""
    assert (
        str(first_product)
        == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    )


def test_product_add_same_class(
    first_product: Product, second_product: Product
) -> None:
    """Проверка сложения объектов одного класса Product."""
    assert first_product + second_product == 2580000.0


def test_product_add_different_classes(
    first_product: Product,
) -> None:
    """Проверка TypeError при сложении разных классов."""
    grass = LawnGrass(
        "Трава", "Описание", 100.0, 10, "РФ", "5 дней", "Зеленый"
    )
    with pytest.raises(TypeError):
        _ = first_product + grass


def test_smartphone_init() -> None:
    """Проверка инициализации дочернего класса Smartphone."""
    phone = Smartphone(
        "Iphone 15",
        "512GB",
        210000.0,
        8,
        98.2,
        "15",
        512,
        "Gray space",
    )
    assert phone.name == "Iphone 15"
    assert phone.efficiency == 98.2


def test_lawngrass_init() -> None:
    """Проверка инициализации дочернего класса LawnGrass."""
    grass = LawnGrass(
        "Газонная трава",
        "Элитная",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )
    assert grass.name == "Газонная трава"
    assert grass.country == "Россия"


def test_price_setter(
    first_product: Product, capsys: pytest.CaptureFixture[str]
) -> None:
    """Проверка установки цены и отбраковки отрицательных значений."""
    first_product.price = 200000.0
    assert first_product.price == 200000.0

    first_product.price = -100.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
