'''
2. Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
(добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов

Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?
Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже.
Главное: дополнить числа до двух разрядов нулём!

'''

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
my_new_list = []
my_string = ''
count = 0
for i in my_list:
    if not i.isalpha():
        my_new_list.insert(count, '"')
        if i.startswith('+'):
            my_new_list.append(f'+{int(i):02}')
        else:
            my_new_list.append(f'{int(i):02}')
        my_new_list.insert(count + 2, '"')
        count += 2
    else:
        my_new_list.append(i)
    count += 1
print(my_list)
print(my_new_list)

first_symbol = False                         # признак раскрывающей ковычки
for i in my_new_list:
    if i == '"':
        if not first_symbol:
            first_symbol = True
            my_string += f'{i}'
        else:
            first_symbol = False
            my_string += f'{i} '
    elif first_symbol:
        my_string += f'{i}'
    else:
        my_string += f'{i} '
print(my_string)
