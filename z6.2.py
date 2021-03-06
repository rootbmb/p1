'''
Задание 6.2
Создать скрипт, который будет обрабатывать 
конфигурационный файл config_sw1.txt:
имя файла передается как аргумент скрипту
Скрипт должен возвращать на стандартный поток вывода команды из переданного
конфигурационного файла, исключая строки, которые начинаются с '!'.
Между строками не должно быть дополнительного символа перевода строки.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
from sys import argv
file_in = argv[1]
with open(file_in) as src:
    for line in src:
        if not line.startswith('!'):
            print(line.rstrip())
