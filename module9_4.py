from random import choice
# 1
first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))

print(result)

# 2
def get_advanced_writer(file_name):
    # Внутренняя функция для записи данных в файл
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as f:
            for item in data_set:
                f.write(f"{item}\n")  # Записываем данные, каждое на новой строке

    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#3
class MysticBall:
    def __init__(self, *words):
        self.words = words  # Сохраняем все переданные слова в атрибуте words
    
    def __call__(self):
        return choice(self.words)  # Возвращаем случайное слово из коллекции

first_ball = MysticBall('Да', 'Нет', 'Наверное') 

for i in range(10):
    print(first_ball())
