"""
Реализовать вывод информации о промежутке времени в зависимости от его
продолжительности duration в секундах:
a. до минуты: <s> сек;
b. до часа: <m> мин <s> сек;
c. до суток: <h> час <m> мин <s> сек;
d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""

def naive_realisation(duration: int):
    total_time = ''
    """
    Решение задачи БЕЗ использования циклов.
    Переменная total_time - строковая переменная,
    содержащая в себе промежуток времени в нужно формате
    """

    if 60 <= duration < 3600:
        total_time = f'{duration // 60} мин {duration % 60} сек'
    elif 3600 <= duration < 86400:
        total_time = f'{duration // 3600} час {(duration % 3600) // 60} мин {(duration % 3600) % 60} сек'
    elif 86400 <= duration:
        total_time = f'{duration // 86400} дн {(duration % 86400) // 3600} час {((duration % 86400) % 3600) // 60} мин {((duration % 86400) % 3600) % 60} сек'
    else:
        total_time = f'{duration} сек'
    return total_time


def one_cycle_realisation(duration):
    total_time = ''
    """
    Решение задачи с использования циклов.
    Можно два, но высший пилотаж через 1 цикл.
    Переменная total_time - строковая переменная,
    содержащая в себе промежуток времени в нужно формате
    """
    second, minute, hour, day = 0, 0, 0, 0
    for i in range(1, duration + 1):
        second += 1
        if second == 60:
            minute += 1
            second = 0
        if minute == 60:
            hour += 1
            minute = 0
        if hour == 24:
            day += 1
            hour = 0
    if minute == 0 and hour == 0 and day == 0:
        total_time = f'{second} сек'
    elif hour == 0 and day == 0:
        total_time = f'{minute} мин {second} сек'
    elif day == 0:
        total_time = f'{hour} час {minute} мин {second} сек'
    else:
        total_time = f'{day} дн {hour} час {minute} мин {second} сек'
    return total_time


if __name__ == '__main__':
    duration = 642
    print(naive_realisation(duration))
    print(one_cycle_realisation(duration))

