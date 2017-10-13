'''
Задание 6.2a
Сделать копию скрипта задания 6.2.
Дополнить скрипт:
Скрипт не должен выводить команды, в которых содержатся слова, которые
указаны в списке ignore.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']
file_in = argv[1]
with open(file_in) as src:
    for line in src:
        if not line.startswith('!'):
            for ig in ignore:
                if ig in line:
                    break
            else:
                print(line.rstrip())
