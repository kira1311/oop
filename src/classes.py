class Product:
    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
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
        """Строковое отображение для Product"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Сумма всех товаров на складе"""
        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError("Операнд справа должен иметь тип Product")


class Category:
    name: str
    description: str
    __products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__products = []
        Category.category_count += 1

    def add_product_category(self, product):
        """Счетчик продуктов"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            print("Можно добавлять только объекты типа Product")

    @property
    def products(self):
        """Геттер для продуктов"""
        return "\n".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.__products)

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1

    def __iter__(self):
        """Позволяет итерироваться по продуктам категории"""
        return iter(self.__products)

    def __str__(self):
        """Строковое отображение для Category"""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
