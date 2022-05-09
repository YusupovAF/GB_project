'''
Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
>>> odd_to_15 = odd_nums(15)
>>> next(odd_to_15)
1
>>> next(odd_to_15)
3
...
>>> next(odd_to_15)
15
>>> next(odd_to_15)
...StopIteration...
'''
my_number = 15

def nums_generator(max):
    for num in range(1, max + 1, 2):
        yield num

my_list = nums_generator(my_number)

for i in range(8):
    print(my_list.__next__())