import logging

import pytest

from src.classes import Category, LawnGrass, Product, Smartphone


@pytest.fixture()
def test_smartphone():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                      "S23 Ultra", 256, "Серый")


@pytest.fixture()
def test_lawn_grass():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture()
def sample_category():
    return Category("Смартфоны", "Современные смартфоны с высокими характеристиками")


def test_check_smartphone(test_smartphone):
    assert test_smartphone.name == "Samsung Galaxy S23 Ultra"
    assert test_smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert test_smartphone.price == 180000.0
    assert test_smartphone.quantity == 5
    assert test_smartphone.efficiency == 95.5
    assert test_smartphone.model == "S23 Ultra"
    assert test_smartphone.memory == 256
    assert test_smartphone.color == "Серый"


def test_check_lawn_grass(test_lawn_grass):
    assert test_lawn_grass.name == "Газонная трава"
    assert test_lawn_grass.description == "Элитная трава для газона"
    assert test_lawn_grass.price == 500.0
    assert test_lawn_grass.quantity == 20
    assert test_lawn_grass.country == "Россия"
    assert test_lawn_grass.germination_period == "7 дней"
    assert test_lawn_grass.color == "Зеленый"


def test_add_product_category(sample_category, test_smartphone):
    sample_category.add_product(test_smartphone)
    assert "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт" in sample_category.products
    assert Category.product_count == 1


def test_add_invalid_product(sample_category):
    with pytest.raises(TypeError):
        sample_category.add_product("Invalid Product")


def test_product_addition(test_smartphone):
    smartphone2 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                             210000.0, 8, 99.9, "S23 Ultra", 256, "Серый")
    result = test_smartphone + smartphone2
    assert result == 180000.0 * 5 + 210000.0 * 8  # = 900000 + 1680000 = 2580000.0


def test_invalid_product_addition(test_smartphone, test_lawn_grass):
    with pytest.raises(TypeError):
        _ = test_smartphone + test_lawn_grass


def test_logging_mixin(caplog):
    with caplog.at_level(logging.INFO):
        product = Product("Test Product", "Description", 100.0, 10)
    assert "Создан объект Product с параметрами" in caplog.text


def test_zero_product():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Test Product", "Description", 100.0, 0)
