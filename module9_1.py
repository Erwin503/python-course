def apply_all_func(int_list, *functions):
    results = {}  # Словарь для хранения результатов
    
    # Перебираем все переданные функции
    for func in functions:
        # Вызываем функцию и сохраняем результат в словарь по её имени
        results[func.__name__] = func(int_list)
    
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
