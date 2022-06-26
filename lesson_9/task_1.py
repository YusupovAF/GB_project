'''Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение
и завершать скрипт.'''

from itertools import cycle
from time import sleep

class TrafficLight:
    __color__ = 'red'
    __color__code = {'red': 7,
                     'yellow': 2,
                     'green': 3}
    def running(self, iters):
        color_cycle = cycle(['red', 'yellow', 'green', 'yellow'])
        for _ in range(iters):
            TrafficLight.__color__ = next(color_cycle)
            print(f'TrafficLight color {TrafficLight.__color__}')
            sleep(TrafficLight.__color__code[TrafficLight.__color__])

my_trafficlite = TrafficLight()
my_trafficlite.running(100)
