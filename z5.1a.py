# -*- coding: utf-8 -*-
'''
Задание 5.1a
Сделать копию скрипта задания 5.1.
Дополнить скрипт:
- Добавить проверку введенного IP-адреса.
- Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.
Если адрес задан неправильно, выводить сообщение:
'Incorrect IPv4 address'
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ip_address = input('введите IP адрес: ')
ip_list = ip_address.split('.')
try:
    ip = [int(a) for a in ip_address.split('.')]
except ValueError:
    print('Incorrect IPv4 address')
else:
    check_range = [byte for byte in ip if 0 <= byte <= 255]

    if not len(check_range) == 4:
        print('Incorrect IPv4 address')
    elif 0 <= ip[0] <= 127:
        print(('ip {} сlass A').format(ip_address))
    elif 128 <= ip[0] <= 191:
        print(('ip {} сlass B').format(ip_address))
    elif 192 <= ip[0] <= 223:
        print(('ip {} сlass C').format(ip_address))
    elif 224 <= ip[0] <= 239:
        print(('ip {} сlass D').format(ip_address))
    elif ip_address == '255.255.255.255':
        print(('ip {} local broadcast').format(ip_address))
    elif ip_address == '0.0.0.0':
        print(('ip {} unassigned').format(ip_address))
    else:
        print('unused')
