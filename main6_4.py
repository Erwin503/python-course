import math

class Figure:
    sides_count = 0  # Атрибут класса

    def __init__(self, sides, color=(0, 0, 0), filled=False):
        # Если количество сторон не совпадает с sides_count, создаём массив из единичных сторон
        if len(sides) != self.sides_count:
            sides = [1] * self.sides_count
        self.__sides = sides  # Инкапсулированный атрибут: список сторон
        self.__color = list(color)  # Инкапсулированный атрибут: список цветов
        self.filled = filled  # Публичный атрибут: закрашенный

    def get_color(self):
        return self.__color  # Возвращаем список RGB цветов

    def __is_valid_color(self, r, g, b):
        return all(isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]  # Устанавливаем новый цвет
        else:
            print("Некорректные значения цвета. Цвет остаётся прежним.")

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)

    def get_sides(self):
        return self.__sides  # Возвращаем список сторон

    def __len__(self):
        return sum(self.__sides)  # Возвращаем периметр фигуры

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)  # Устанавливаем новые стороны
        else:
            print("Некорректное количество или значения сторон. Стороны остаются прежними.")


class Circle(Figure):
    sides_count = 1  # У круга количество сторон равно 1

    def __init__(self, color, circumference):
        super().__init__([circumference], color)  # Инициализация базового класса
        self.__radius = circumference / (2 * math.pi)  # Рассчитываем радиус

    def get_square(self):
        return math.pi * (self.__radius ** 2)  # Площадь круга


class Triangle(Figure):
    sides_count = 3  # У треугольника количество сторон равно 3

    def __init__(self, color, a, b=None, c=None):
        # Если не переданы все три стороны, создаём массив из единичных сторон
        if b is None or c is None:
            sides = [1, 1, 1]
        else:
            sides = [a, b, c]
        super().__init__(sides, color)  # Инициализация базового класса

    def get_square(self):
        # Используем формулу Герона для расчета площади
        a, b, c = self.get_sides()
        s = (a + b + c) / 2  # Полупериметр
        return math.sqrt(s * (s - a) * (s - b) * (s - c))  # Площадь


class Cube(Figure):
    sides_count = 12  # У куба количество рёбер равно 12

    def __init__(self, color, edge_length):
        # Создаём массив из 12 одинаковых сторон
        sides = [edge_length] * self.sides_count
        super().__init__(sides, color)  # Инициализация базового класса

    def get_volume(self):
        edge_length = self.get_sides()[0]  # Все ребра одинаковой длины
        return edge_length ** 3  # Объём куба

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
