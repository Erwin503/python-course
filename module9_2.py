first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# 1. first_result - список длин строк из first_strings, где длина строки не менее 5 символов
first_result = [len(word) for word in first_strings if len(word) >= 5]

# 2. second_result - список пар слов из first_strings и second_strings одинаковой длины
second_result = [(word1, word2) for word1 in first_strings for word2 in second_strings if len(word1) == len(word2)]

# 3. third_result - словарь из строк и их длин, только с чётной длиной строки
third_result = {word: len(word) for word in first_strings + second_strings if len(word) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)
