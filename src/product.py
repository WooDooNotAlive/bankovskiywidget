class Product:
    """Класс для представления товара в интернет-магазине."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ) -> None:
        """Инициализация объекта товара.

        Args:
            name: Название товара.
            description: Описание товара.
            price: Цена товара.
            quantity: Количество в наличии.
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
