'''
Тема функции и словари
'''
demo_list = [1, 'str', 42.2, [1, 2, 3]]

print(demo_list[-1][1])
phone_book = {'Petrov': 41, #0
              'Vasechkin': 42, #3
              'Siroezhkin': 68} #8

print(type(phone_book), phone_book)
print(phone_book['Siroezhkin'])
# print(demo_list[-3])

'''
забавная фишка
x, y = (10, 12)
print(f' x: {x}, y: {y}')

c = x
x = y
y = c

print(f' x: {x}, y: {y}')

x, y = y, x
print(f' x: {x}, y: {y}')
'''

"""
for key, value in phone_book.items():
    print(key, '#', value)

for key in phone_book.keys():
    print(key)

for value in phone_book.values():
    print(value)
"""

# import random
#
# print(random.randint(5, 10))

# from random import *
# print(randint(5, 10))

from random import randint

print(randint(5, 10))