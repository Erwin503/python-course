import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        
        # Проходим по каждому файлу
        for file_name in self.file_names:
            words = []
            
            # Открываем файл для чтения
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    # Приводим строку к нижнему регистру
                    line = line.lower()
                    # Убираем пунктуацию
                    line = line.translate(str.maketrans('', '', string.punctuation.replace('-', '')))
                    # Разбиваем строку на слова
                    words.extend(line.split())
            
            # Добавляем список слов файла в словарь
            all_words[file_name] = words
        
        return all_words

    def find(self, word):
        # Получаем все слова из файлов
        all_words = self.get_all_words()
        result = {}
        
        # Ищем слово в каждом файле
        for file_name, words in all_words.items():
            if word.lower() in words:
                result[file_name] = words.index(word.lower()) + 1
        
        return result

    def count(self, word):
        # Получаем все слова из файлов
        all_words = self.get_all_words()
        result = {}
        
        # Считаем количество вхождений слова в каждом файле
        for file_name, words in all_words.items():
            result[file_name] = words.count(word.lower())
        
        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
