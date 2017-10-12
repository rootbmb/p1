# -*- coding: utf-8 -*-
'''
Задание 5.1
1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить какому классу принадлежит IP-адрес.
3. В зависимости от класса адреса, вывести на стандартный поток вывода:
   'unicast' - если IP-адрес принадлежит классу A, B или C
   'multicast' - если IP-адрес принадлежит классу D
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях
Подсказка по классам (диапазон значений первого байта в десятичном формате):
A: 1-127
B: 128-191
C: 192-223
D: 224-239
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
subnet = input("Введите адрес сети в формате 10.0.1.1:")
try:
    ip = int(subnet.split('.')[0])
    if ip <= 127:
        print(('ip {} сlass A').format(subnet))
    elif ip > 127 and ip <= 191:
        print(('ip {} сlass B').format(subnet))
    elif ip > 191 and ip <= 223:
        print(('ip {} сlass C').format(subnet))
    elif ip > 223 and ip <= 239:
        print(('ip {} сlass D').format(subnet))
    elif subnet == '255.255.255.255':
        print(('ip {} local broadcast').format(subnet))
    elif subnet == '0.0.0.0':
        print(('ip {} unassigned').format(subnet))
    else:
        print('unused')
except(ValueError):
    print('не правильно введен ip')
