'''
Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на
русский язык. Например:
>>> num_translate("one")
"один"
>>> num_translate("eight")
"восемь"
Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить
информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или
снаружи.
'''


def num_translate(number: str):
    my_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    try:
        my_string = f'"{my_dict[number]}"'
        return my_string
    except KeyError:
        return None

if __name__ == "__main__":
    print(num_translate('onek'))
    print(num_translate('six'))
    

