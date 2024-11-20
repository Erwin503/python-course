def add_everything_up(a, b):
    try:
        # Если a и b оба числа (int или float), выполняем их сложение
        return a + b
    except TypeError:
        # Если возникла ошибка, значит a и b разных типов, склеиваем их как строки
        return str(a) + str(b)

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
