import pytest

from src.classes import Category, Product


@pytest.fixture()
def test_product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture()
def test_category():
    return Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни")


def test_check_product(test_product):
    assert test_product.name == "Samsung Galaxy S23 Ultra"
    assert test_product.description == "256GB, Серый цвет, 200MP камера"
    assert test_product.price == 180000.0
    assert test_product.quantity == 5


def test_check_category(test_category):
    assert test_category.name == "Смартфоны"
    assert (test_category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни")
    assert test_category.products == ""


def test_add_product_category(test_category, test_product):
    test_category.add_product_category(test_product)
    assert "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт" in test_category.products
    assert Category.product_count == 1


def test_str_product(test_product):
    assert str(test_product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_str_category(test_category, test_product):
    test_category.add_product(test_product)
    assert str(test_category) == "Смартфоны, количество продуктов: 5 шт."


def test_product_addition(test_product):
    product2 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    result = test_product + product2
    assert result == 180000.0 * 10


def test_category_iteration(test_category, test_product):
    product2 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    test_category.add_product(test_product)
    test_category.add_product(product2)

    products = [product for product in test_category]
    assert len(products) == 2
    assert products[0] == test_product
    assert products[1] == product2
