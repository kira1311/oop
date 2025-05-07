import logging
from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, name, description, price, quantity):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class LoggingMixin:
    """Автоматическое логирование создания объектов."""
    def __init__(self, *args, **kwargs):
        logging.info(f"Создан объект {self.__class__.__name__} с параметрами: {args}, {kwargs}")
        super().__init__(*args, **kwargs)


class Product(LoggingMixin, BaseProduct):
    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Инициализация объекта Product."""
        super().__init__(name, description, price, quantity)
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        """Возвращает цену продукта"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Устанавливает новую цену продукта"""
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    def __str__(self):
        """Строковое отображение для класса Product"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Сумма всех товаров на складе"""
        if isinstance(other, type(self)):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError("Операнд справа должен иметь тип Product")


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """Класс наследник для Product"""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return f"{self.name}, {self.model}, {self.memory}, {self.color}, {self.price} руб. Остаток: {self.quantity} шт."


class LawnGrass(Product):
    """Класс наследник для Product"""
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        """Возвращает строковое представление объекта Smartphone."""
        return f"{self.name}, {self.country}, {self.germination_period}, {self.color}, {self.price} руб. Остаток: {self.quantity} шт."


class Category:
    name: str
    description: str
    __products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name, description):
        """Инициализация объекта LawnGrass."""
        self.name = name
        self.description = description
        self.__products = []
        Category.category_count += 1

    @property
    def products(self):
        """Геттер для продуктов"""
        return "\n".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.__products)

    def add_product(self, product: Product):
        """Добавляет продукт в категорию."""
        try:
            if isinstance(product, Product):
                self.__products.append(product)
                Category.product_count += 1
            else:
                raise TypeError("Можно добавлять только объекты типа Product или его наследников.")
        except ValueError as e:
            print(e)
        finally:
            print("Обработка добавления товара завершена")

    def __iter__(self):
        """Позволяет итерироваться по продуктам категории"""
        return iter(self.__products)

    def __str__(self):
        """Строковое отображение для класса Category"""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def middle_price(self):
        try:
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0
