'''Задание 6.2b
Дополнить скрипт из задания 6.2a:
вместо вывода на стандартный поток вывода, скрипт должен записать полученные
строки в файл config_sw1_cleared.txt
При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.
Ограничение: Все задания надо выполнять используя только пройденные темы.
ignore = ['duplex', 'alias', 'Current configuration']
'''

from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']

file = argv[1]
new_file = []
with open(file) as f:
    for line in f:
        line = line.strip('\n').rstrip()
        new_file.append(line)
    for line in new_file:
        for i in ignore:
            if line.strip().startswith(i):
                new_file.remove(line)
    for line in new_file:
        if line == '':
            continue
        else:
            file_out = open('config_sw1_cleared.txt', 'a')
            file_out.write(line + '\n')
