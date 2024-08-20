# 2. Работа со словарями:
#   - Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
# Например: Имя(str)-Год рождения(int).
#   - Выведите на экран словарь my_dict.
#   - Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.
#   - Добавьте ещё две произвольные пары того же формата в словарь my_dict.
#  - Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.
#   - Выведите на экран словарь my_dict.

# 3. Работа с множествами:
#   - Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
#   - Выведите на экран множество my_set (должны отобразиться только уникальные значения).
#   - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
#   - Удалите один любой элемент из множества my_set.
#   - Выведите на экран измененное множество my_set.
# Работа со словарями

# Создание словаря
my_dict = {
    "Ivan": 1990,
    "Maria": 1985,
    "Alexey": 2000
}

# Вывод словаря на экран
print("Initial dictionary:", my_dict)

# Вывод одного значения по существующему ключу
print("Year of birth of Ivan:", my_dict.get("Ivan"))

# Вывод одного значения по отсутствующему ключу (без ошибки)
print("Year of birth of unknown person:", my_dict.get("Peter", "Key not found"))

# Добавление двух пар в словарь
my_dict["Anna"] = 1992
my_dict["Dmitry"] = 1988

# Удаление одной пары и вывод значения
removed_value = my_dict.pop("Maria", "Key not found")
print("Removed value:", removed_value)

# Вывод измененного словаря на экран
print("Updated dictionary:", my_dict)

# Работа с множествами

# Создание множества с повторяющимися значениями
my_set = {1, "apple", 3.14, "apple", 1, 42}

# Вывод множества на экран (должны отобразиться только уникальные значения)
print("Initial set:", my_set)

# Добавление двух элементов в множество
my_set.add("banana")
my_set.add(99)

# Удаление одного элемента из множества
my_set.discard(42)

# Вывод измененного множества на экран
print("Updated set:", my_set)
