# Задача:

# Напишите 4 переменных которые буду обозначать следующие данные:
# Количество выполненных ДЗ (запишите значение 12)
# Количество затраченных часов (запишите значение 1.5)
# Название курса (запишите значение 'Python')
# Время на одно задание (вычислить используя 1 и 2 переменные)
# Выведите на экран(в консоль), используя переменные, следующую строку:
# Курс: Python, всего задач:12, затрачено часов: 1.5, среднее время выполнения 0.125 часа.

class Mytime:

    def calculate(self):
        if self.hours % 1 != 0:
            self.mins += (self.hours % 1) * 60
            self.hours -= self.hours % 1

        if self.mins % 1 != 0:
            self.secs += (self.mins % 1) * 60
            self.mins -= self.mins % 1

        if self.secs > 59:
            self.mins += (self.secs // 60) // 1
            self.secs = self.secs % 60

        if self.mins > 59:
            self.hours += (self.mins // 60) // 1
            self.mins = self.mins % 60

        return self

    def __init__(self, hours = 0, mins = 0, secs = 0):
        self.hours = hours
        self.mins = mins
        self.secs = secs
        self.calculate()
    
    def __str__(self) -> str:
        return ('Часы: ' + str(self.hours) + '\nМинуты: ' + str(self.mins) + '\nСекунды: ' + str(self.secs))
    
    def __add__(self, other: 'Mytime'):
        result = Mytime(self.hours + other.hours, self.mins + other.mins, self.secs + other.secs)
        return result.calculate()
    
    def __mul__(self, other: 'int'):
        mins = self.hours * 60 + self.mins
        secs = mins * 60 + self.secs
        secs = secs * other
        result = Mytime(0, 0, secs)
        return result.calculate()
    
    def __floordiv__(self, other: 'int'):
        mins = self.hours * 60 + self.mins
        secs = mins * 60 + self.secs
        secs = secs / other
        result = Mytime(0, 0, secs)
        return result.calculate()

        
t = Mytime(12.25, 10.5, 10)
s = Mytime(1, 2, 2)
print(t + s)

homeWork = 12
hoursCount = Mytime(hours=1.5)
courseName = 'Python'
avgTaskTime = hoursCount // homeWork

print('Курс: ', courseName, ', всего задач:', homeWork, sep='')
print('Затраченные часы:\n', hoursCount)
print('Среднее время на задачу:\n', avgTaskTime)

# Да, я запарился...
