class Horse:
    def __init__(self):
        self.x_distance = 0  # Пройденный путь
        self.sound = 'Frrr'  # Звук, который издает лошадь

    def run(self, dx):
        self.x_distance += dx  # Увеличиваем пройденный путь


class Eagle:
    def __init__(self):
        self.y_distance = 0  # Высота полета
        self.sound = 'I train, eat, sleep, and repeat'  # Звук, который издает орел

    def fly(self, dy):
        self.y_distance += dy  # Увеличиваем высоту полета


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)  # Инициализация класса Horse
        Eagle.__init__(self)  # Инициализация класса Eagle

    def move(self, dx, dy):
        self.run(dx)  # Вызываем метод run из класса Horse
        self.fly(dy)  # Вызываем метод fly из класса Eagle

    def get_pos(self):
        return (self.x_distance, self.y_distance)  # Возвращаем текущее положение в виде кортежа

    def voice(self):
        print(self.sound)  # Печатаем звук

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()