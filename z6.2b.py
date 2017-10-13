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
file_out = 'config_sw1_cleared.txt'
file_in = argv[1]
with open(file_in) as src, open(file_out, 'a') as dst:
    for line in src:
        for ig in ignore:
            if ig in line:
                break
        else:
            dst.write(line)
