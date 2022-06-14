'''1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать
их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.'''

class Data:
    def __init__(self, datatime):
        self.datatime = datatime

    @staticmethod
    def validation(period, num):
        if period == 'day':
            return num if 1 < num < 31 else None
        if period == 'month':
            return num if 1 < num < 12 else None
        if period == 'year':
            return num if 1900 < num < 2100 else None

    @classmethod
    def date_conversion(cls, datatime):
        day = datatime.split('-')[0]
        month = datatime.split('-')[1]
        year = datatime.split('-')[2]
        print(day, month, year)
        return day, month, year

my_data = Data('12-11-2011')
my_data.date_conversion('11-11-2011')
print(Data.validation('day', 4))


