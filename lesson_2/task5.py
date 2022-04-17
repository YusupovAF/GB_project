'''
5. Создать список, содержащий цены на товары (10–20 товаров), например:
[57.8, 46.51, 97, ...]

Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
Создать новый список, содержащий те же цены, но отсортированные по убыванию.
Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
'''

my_list = [57.8, 46.51, 97, 56.3, 45.66, 45.77, 123.44, 978.44, 4.44, 656.22, 87.87, 12.21]
def print_list(my_list):
    my_string = ''
    for i in my_list:
        try:
            integer_part = str(i).split('.')[0]
        except IndexError:
            integer_part = '0'
        try:
            fractional_part = str(i).split('.')[1]
        except IndexError:
            fractional_part = '0'
        my_string += f'«{integer_part} руб {int(fractional_part):02} коп» '
    print(my_string)

# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
print_list(my_list)
print(id(my_list))

# Вывести цены, отсортированные по возрастанию, новый список не создавать
my_list.sort()
print_list(my_list)
print(id(my_list))      # id объекта не изменился

# Создать новый список, содержащий те же цены, но отсортированные по убыванию
my_list_decr = sorted(my_list, reverse=True)
print(my_list_decr)

# Вывести цены пяти самых дорогих товаров.
print(my_list_decr[0:5])