from src.classes import Category, LawnGrass, Smartphone

if __name__ == "__main__":
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, "High", "S23 Ultra", "256GB", "Gray")
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, "High", "15", "512GB", "Gray")
    lawn_grass1 = LawnGrass("Green Lawn", "High-quality grass", 500.0, 100, "USA", "7 days", "Green")

    print(smartphone1)
    print(smartphone2)
    print(lawn_grass1)

    category1 = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни")
    category1.add_product(smartphone1)
    category1.add_product(smartphone2)

    category2 = Category("Трава газонная", "Качественная трава для вашего газона")
    category2.add_product(lawn_grass1)

    print(category1)
    print(category1.products)
    print(Category.category_count)
    print(Category.product_count)

    print(category2)
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)

    # Пример использования итерации по категории
    for product in category1:
        print(product)
