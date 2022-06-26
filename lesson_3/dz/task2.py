'''
 *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать
корректную работу с числительными, начинающимися с заглавной буквы — результат тоже
должен быть с заглавной. Например:
>>> num_translate_adv("One")
"Один"
>>> num_translate_adv("two")
"два"
'''

def num_translate_adv(number):
    my_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
               'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    if number.istitle():
        all_charlow= my_dict[number.lower()]
        return f'"{all_charlow.title()}"'
    else:
        return f'"{my_dict[number]}"'

if __name__ == "__main__":
    print(num_translate_adv('one'))
    print(num_translate_adv('Seven'))
