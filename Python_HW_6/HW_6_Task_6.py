# Задание 5
# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title
# (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
# три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов
# реализовать переопределение метода draw. Для каждого из классов метод должен
# выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет
# описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, name):
        self.name = name

    def draw(self):
        print(f'Запуск отрисовки {self.name}')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск письма {self.name}')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск черчения {self.name}')


class Marker(Stationery):
    def draw(self):
        print(f'Запуск рисования {self.name}')


draw = Stationery('красками')
draw.draw()

pen = Pen('ручкой')
pen.draw()

pencil = Pencil('карандашом')
pencil.draw()

marker = Marker('маркером')
marker.draw()
