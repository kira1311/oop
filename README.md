Мой проект.

Этот проект представляет собой систему управления продуктами, включающую в себя базовые классы для продуктов, смартфонов, газонной травы и категорий. Проект также включает тесты для проверки функциональности классов.


Установка

Склонируйте репозиторий:

```bash
git clone <URL репозитория>
```

Перейдите в директорию проекта:

```bash
cd Мой_проект
```

Установите необходимые зависимости:

```bash
pip install -r requirements.txt
```


Использование:

Основные классы
Product: Базовый класс для всех продуктов.
Атрибуты: name, description, price, quantity.
Методы: __init__, price (геттер и сеттер), __str__, __add__.
Smartphone: Наследует Product.

Дополнительные атрибуты: efficiency, model, memory, color.
Методы: __init__, __str__.
LawnGrass: Наследует Product.

Дополнительные атрибуты: country, germination_period, color.
Методы: __init__, __str__.
Category: Класс для управления категориями продуктов.

Атрибуты: name, description, __products (список продуктов).
Методы: __init__, products (геттер), add_product, __iter__, __str__.




Пример использования:

```bash
from src.classes import Category, LawnGrass, Smartphone

if __name__ == '__main__':
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")

    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    smartphone_sum = smartphone1 + smartphone2
    print(smartphone_sum)

    grass_sum = grass1 + grass2
    print(grass_sum)

    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны")
    category_grass = Category("Газонная трава", "Различные виды газонной травы")

    category_smartphones.add_product(smartphone1)
    category_smartphones.add_product(smartphone2)
    category_smartphones.add_product(smartphone3)

    category_grass.add_product(grass1)
    category_grass.add_product(grass2)

    print(category_smartphones.products)
    print(Category.product_count)

```


Тестирование:

Для запуска тестов используйте команду:

```bash
pytest
```
Тесты находятся в файле test_classes.py и включают проверки для всех классов и их методов.


Отчёт о покрытии тестов:
```bash
File	          Statements	    Missing 	   Excluded	    Coverage
src\__init__.py	       0	       0	       0	      100%
src\classes.py	      22	       0	       0	      100%
Total	              22	       0	       0	      100%
```