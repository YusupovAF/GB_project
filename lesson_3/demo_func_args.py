def fancy_func(base_num, power_num, name='John'):
    return f'{name} count {(base_num * base_num) ** power_num}'

"""
#позиционные аргументы
print(fancy_func(2, 3, 'Katty'))
print(fancy_func(3, 2))

#именнованные аргументы
print(fancy_func(base_num=2, power_num=3, name='Basil'))
print(fancy_func(power_num=2, base_num=3))

#при смешивании соблюдаем порядок
print(fancy_func(2, name='Julia', power_num=3))
"""


def fancy_func_with_many_args(arg1, arg2, *args):
    output_string = f'{arg1} {arg2}'
    # for arg in args:
        # if arg: #if arg == True
        #     print('Ura!')
        # output_string += (str(arg) + ' ')
    if True in args: #проверка на наличие внути списка
        print('Ura!')
    return output_string

# print(fancy_func_with_many_args({1 : '1'}, 'hello', 10, True, 10))

def fancy_func_with_many_args(arg1, arg2, *args, **kwargs):
    output_string = f'{arg1} {arg2}'
    for key, value in kwargs.items():
        print(key, value)
    if kwargs.get('key2') == 4:
        print('Wow!')
    return output_string

print(fancy_func_with_many_args(1, 2, key1=3, key2=4, key3=5, key4=6))

demo_list = [1, 2, [3, 4], 4]
print(demo_list)
print(*demo_list)


