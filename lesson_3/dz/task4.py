'''
*(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов
строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы
фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие
записи, в которых фамилия начинается с соответствующей буквы. Например:
>>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": ["Петр Алексеев"]
        },
    "И": {
        "И": ["Илья Иванов"]
        },
    "С": {
            "И": ["Иван Сергеев", "Инна Серова"],
            "А": ["Анна Савельева"]
        }
}
Как поступить, если потребуется сортировка по ключам?
'''

def thesaurus(*args):

    def get_dict_level2():
        for j in args:
            if j.split()[-1][0] == lastname[0]:
                name = j.split()[0]
                if not name[0] in my_dict_2:
                    my_dict_2[name[0]] = []
                    my_dict_2[name[0]].append(j)
                else:
                    my_dict_2[name[0]].append(j)

    my_dict = {}
    for i in args:
        lastname = i.split()[-1]
        my_dict_2 = {}
        if not lastname[0] in my_dict:
            get_dict_level2()
            my_dict[lastname[0]] = my_dict_2
        else:
            get_dict_level2()
            my_dict[lastname[0]] = my_dict_2
    my_dict_sorted = sorted(my_dict.items())
    return dict(my_dict_sorted)


if __name__ == "__main__":
    print(thesaurus("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))