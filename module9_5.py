# 1. Класс исключения StepValueError
class StepValueError(ValueError):
    pass

# 2. Класс Iterator
class Iterator:
    def __init__(self, start, stop, step=1):
        # Проверка шага
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')
        
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start  # Начальное значение указателя

    def __iter__(self):
        # Сбрасываем указатель на начало
        self.pointer = self.start
        return self
    
    def __next__(self):
        # Проверка условия завершения итерации в зависимости от знака шага
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration  # Завершаем итерацию

        current = self.pointer  # Сохраняем текущее значение
        self.pointer += self.step  # Увеличиваем указатель на шаг
        return current  # Возвращаем текущее значение

# Пример использования:

# Попытка создать итератор с шагом 0
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError as e:
    print(e)

# Итераторы с различными параметрами
iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

# Печать результатов итерации
for i in iter2:
    print(i, end=' ')
print()

for i in iter3:
    print(i, end=' ')
print()

for i in iter4:
    print(i, end=' ')
print()

for i in iter5:
    print(i, end=' ')
print()
