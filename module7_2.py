def custom_write(file_name, strings):
    strings_positions = {}
    
    with open(file_name, 'w', encoding='utf-8') as f:
        for line_number, string in enumerate(strings, 1):
            # Получаем текущую позицию в файле перед записью строки
            byte_position = f.tell()
            # Записываем строку в файл
            f.write(string + '\n')
            # Сохраняем в словарь кортеж (номер строки, позиция в байтах) и саму строку
            strings_positions[(line_number, byte_position)] = string
            
    return strings_positions

# Пример выполнения кода
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)
