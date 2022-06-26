'''
Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно,
что при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая.
Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей,
чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи
'''
import sys

users_file = open('users.csv', encoding= 'UTF-8')
hobby_file = open('hobby.csv', encoding= 'UTF-8')
result_file = open('result.csv', 'w')

result_dict = {}
while True:
    user_line = users_file.readline()
    hobby_line = hobby_file.readline()

    if not user_line:
        print(result_dict)
        users_file.close()
        hobby_file.close()
        result_file.close()
        sys.exit(0)

    user = user_line.replace('\n', '')
    if not hobby_line:
        result_dict[user] = None
        result_file.write(f'{user}: None\n')
    else:
        result_dict[user] = hobby_line.replace('\n', '')
        result_file.write(f'{user}: {result_dict[user]}\n')