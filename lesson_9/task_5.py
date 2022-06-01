'''Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.'''

class Stationery:
    title = 'Stationery'

    def draw(self):
        print('Starting to draw')

class Pen(Stationery):
    def draw(self):
        print('Starting to draw by pen')

class Pencil(Stationery):
    def draw(self):
        print('Starting to draw by pencil')

class Handle(Stationery):
    def draw(self):
        print('Starting to draw by handle')

pen = Pen()
pencil = Pencil()
handle = Handle()

pen.draw()
pencil.draw()
handle.draw()