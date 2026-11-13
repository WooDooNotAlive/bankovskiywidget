from typing import Iterator

from src.product import Product


class Category:
    """Класс для представления категории товаров."""

    category_count: int = 0
    product_count: int = 0

    name: str
    description: str
    __products: list[Product]

    def __init__(
        self, name: str, description: str, products: list[Product]
    ) -> None:
        """Инициализация объекта категории."""
        self.name = name
        self.description = description
        self.__products = []
        Category.category_count += 1
        for product in products:
            self.add_product(product)

    def __str__(self) -> str:
        """Строковое отображение категории."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        """Добавление продукта в категорию с проверкой типа."""
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты класса Product или "
                "его дочерних классов"
            )
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер списочного представления товаров."""
        result = ""
        for product in self.__products:
            result += f"{product}\n"
        return result

    @property
    def products_list(self) -> list[Product]:
        """Возвращает список объектов продуктов (для итератора)."""
        return self.__products


class CategoryIterator:
    """Класс для итерации по товарам категории."""

    def __init__(self, category: Category) -> None:
        """Инициализация итератора."""
        self.products = category.products_list
        self.index = 0

    def __iter__(self) -> Iterator[Product]:
        """Возвращает объект итератора."""
        self.index = 0
        return self

    def __next__(self) -> Product:
        """Возвращает следующий товар категории."""
        if self.index < len(self.products):
            product = self.products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
