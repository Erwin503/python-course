def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    
    # Вызов inner_function внутри test_function
    inner_function()

# Вызов test_function
test_function()

# Попытка вызвать inner_function вне test_function
try:
    inner_function()  # Этот вызов приведет к ошибке
except NameError as e:
    print(f"Ошибка: {e}")
