my_string = input("Введите текст: ")
print("Количество символов в тексте:", len(my_string))

# 1. Выводим строку в верхнем регистре
print("Текст в верхнем регистре:", my_string.upper())

# 2. Выводим строку в нижнем регистре
print("Текст в нижнем регистре:", my_string.lower())

# 3. Удаляем все пробелы из строки
my_string_no_spaces = my_string.replace(" ", "")
print("Текст без пробелов:", my_string_no_spaces)

# 4. Выводим первый символ строки
if len(my_string) > 0:
    print("Первый символ строки:", my_string[0])

# 5. Выводим последний символ строки
if len(my_string) > 0:
    print("Последний символ строки:", my_string[-1])
