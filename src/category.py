from src.product import Product


class Category:
    """Класс для представления категории товаров."""

    category_count: int = 0
    product_count: int = 0

    name: str
    description: str
    __products: list[Product]

    def __init__(
        self,
        name: str,
        description: str,
        products: list[Product],
    ) -> None:
        """Инициализация объекта категории."""
        self.name = name
        self.description = description
        self.__products = []
        Category.category_count += 1

        for product in products:
            self.add_product(product)

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в категорию и увеличивает счетчик продуктов."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер возвращает список товаров в виде строки по шаблону."""
        result = ""
        for product in self.__products:
            result += (
                f"{product.name}, {product.price} руб. "
                f"Остаток: {product.quantity} шт.\n"
            )
        return result
