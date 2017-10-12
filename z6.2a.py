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

file = argv[1]
new_file = []
nl = []
with open(file) as f:
    for line in f:
        line = line.strip('!').strip('\n').rstrip()
        new_file.append(line)
    for line in new_file:
        for i in ignore:
            if line.strip().startswith(i):
                new_file.remove(line)
    for line in new_file:
        if line == '':
            continue
        else:
            print(line)
