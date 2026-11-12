from src.product import Product


class Category:
    """Класс для представления категории товаров."""

    category_count: int = 0
    product_count: int = 0

    name: str
    description: str
    products: list[Product]

    def __init__(
        self,
        name: str,
        description: str,
        products: list[Product],
    ) -> None:
        """Инициализация объекта категории.

        Автоматически увеличивает счётчики
        category_count и product_count.

        Args:
            name: Название категории.
            description: Описание категории.
            products: Список товаров категории.
        """
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)
