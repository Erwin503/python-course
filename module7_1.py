class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name            # Название продукта
        self.weight = weight        # Общий вес товара
        self.category = category    # Категория товара

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"  # Формат строки


class Shop:
    __file_name = 'products.txt'  # Инкапсулированный атрибут с именем файла

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read()  # Чтение всех продуктов из файла
        except FileNotFoundError:
            return "Файл не найден."  # Обработка ошибки если файл не существует

    def add(self, *products):
        existing_products = set()
        try:
            with open(self.__file_name, 'r') as file:
                existing_products = {line.split(', ')[0] for line in file.readlines()}  # Чтение существующих продуктов
        except FileNotFoundError:
            pass  # Если файла нет, просто продолжаем

        for product in products:
            if product.name in existing_products:
                print(f"Продукт {product.name} уже есть в магазине")
            else:
                with open(self.__file_name, 'a') as file:
                    file.write(str(product) + '\n')  # Запись нового продукта в файл
                existing_products.add(product.name)  # Добавляем продукт в набор

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())