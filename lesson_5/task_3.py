'''Есть два списка:
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = [9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
('Иван', '9А')
('Анастасия', '7В')
...
Количество генерируемых кортежей не должно быть больше длины списка tutors.
Если в списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние кортежи в виде:
(<tutor>, None), например: ('Станислав', None)
### Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
Подумать, в каких ситуациях генератор даст эффект. '''



def joining_lists(first_list, second_list):
    for i in range(max(len(tutors), len(klasses))):
        if i < len(klasses) and i < len(tutors):
            combined_list = (tutors[i], klasses[i])
        elif i > len(tutors):
            combined_list = (None, klasses[i])
        else:
            combined_list = (tutors[i], None)
        yield combined_list

if __name__ == "__main__":
    tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', '']
    klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
    combined_list = joining_lists(tutors, klasses)
    print(*combined_list)