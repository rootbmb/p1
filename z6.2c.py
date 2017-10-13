'''
Задание 6.2c
Переделать скрипт из задания 6.2b:
передавать как аргументы скрипту:
имя исходного файла конфигурации
имя итогового файла конфигурации
Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации, в
которых содержатся слова из списка ignore. И затем записать оставшиеся строки в
итоговый файл.
Проверить работу скрипта на примере файла config_sw1.txt.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']
file_in, file_out = argv[1:]
with open(file_in) as src, open(file_out, 'a') as dst:
    for line in src:
        for ig in ignore:
            if ig in line:
                break
        else:
            dst.write(line)
