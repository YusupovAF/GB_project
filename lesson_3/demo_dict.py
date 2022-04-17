adress_book = {'Surkov': {'adress': 'Moscow',
                          "phone": '+79097654321',
                          "age": 27,
                          "family": ['son', 'son',
                                     'son', 'son',
                                     'лапочка дочка']},
               'Moskalets': {'adress': 'Spb',
                          "phone": '+79197654321',
                          "age": 27}}
'''
# print(adress_book['Moskalets']['family'])
print(adress_book['Moskalets'].get('family'))

for surname_key in adress_book.keys():
    family_members = adress_book[surname_key].get('family')

    if not family_members: #отсутствие информации == 0, а 0 - это логическое нет
        print(f'Для {surname_key} информация отсутствует')
    else:
        print(f'Surname: {surname_key}, family: {family_members}')

# print(help(dict))
for surname_key in adress_book.keys():
    family_members = adress_book[surname_key].setdefault('family', ['cat'])

    if not family_members: #отсутствие информации == 0, а 0 - это логическое нет
        print(f'Для {surname_key} информация отсутствует')
    else:
        print(f'Surname: {surname_key}, family: {family_members}')

print(adress_book)
'''
# print(help(dict))

# phone_pop_res = adress_book['Surkov'].pop('phone')
# print(phone_pop_res)
adress_book['Surkov'].pop('phone')
print(adress_book)
family = adress_book['Surkov'].popitem()
print('Family', family)
print(adress_book)
adress_book['Surkov']['index'] = 110659
# adress_book['Surkov']['index_1'] = 110659
# adress_book['Surkov']['index_0'] = 110659
# print(adress_book['Surkov'].popitem())

adress_book['Petrov'] = {"phone": '+79097654321',
                          "age": 27}

# print(adress_book['Surkov'].popitem())
# print(adress_book)

keys = list(adress_book.keys())
for surname_key in keys:
    if adress_book[surname_key].get('adress') == 'Spb':
        # spb_user = (surname_key, adress_book.pop(surname_key))
        del adress_book[surname_key]

# print('SPB', spb_user)
print(adress_book)