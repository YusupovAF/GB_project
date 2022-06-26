my_number = 15

my_list = (num for num in range(1, my_number + 1, 2))

for i in range(8):
    print(my_list.__next__())