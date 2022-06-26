'''
 * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
размер которых превышает объем ОЗУ компьютера.
'''

spammers = {}
data = []
with open('requests.txt') as f:
    for line in f.readlines():
        line_data = line.split()
        data.append((line_data[0], line_data[5][1:], line_data[6]))
        spammers[line_data[0]] = spammers.setdefault(line_data[0], 0) + 1

print(max(spammers, key = spammers.get))