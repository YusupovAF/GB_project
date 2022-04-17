students_ages = ['26', '15', '19', '21']
students_names = ['basil', 'ivan', 'Ilya', 'katya']

print(list(map(type, students_ages)))
print(list(map(str.capitalize, students_names)))

for name, age in zip(students_names, students_ages):
    print(name, age)

print(*filter(str.islower, students_names))
