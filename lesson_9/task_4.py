'''Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.'''

class Car:
    speed_limit = None
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Drr-drr')

    def stop(self):
        print('Car stoped')

    def turn(self, direction):
        print(f'Turning to the {direction}')

    def show_speed(self):
        speed_limit = self.get_speed_limit()
        if speed_limit is None:
            print(self.speed)
        else:
            if self.speed < speed_limit:
                print(self.speed)
            else:
                print('Your speed is too high')

    @classmethod
    def get_speed_limit(cls):
        return cls.speed_limit

class TownCar(Car):
    speed_limit = 60

class SportCar(Car):
    pass

class WorkCar(Car):
    speed_limit = 40

class PoliceCar(Car):
    pass

test_car_one = WorkCar(50, 'red', 'audi', True)
test_car_two = TownCar(30, 'red', 'audi', True)
test_car_three = WorkCar(70, 'red', 'audi', True)

test_car_one.show_speed()
test_car_two.show_speed()
test_car_three.show_speed()

