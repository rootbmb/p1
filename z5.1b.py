'''
Задание 5.1b
Сделать копию скрипта задания 5.1a.
Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
while True:

    ip_address = input('введите IP адрес: ')
    ip_list = ip_address.split('.')
    try:
        ip = [int(a) for a in ip_address.split('.')]
    except ValueError:
        print('Incorrect IPv4 address')
        continue
    else:
        check_range = [byte for byte in ip if 0 <= byte <= 255]

        if not len(check_range) == 4:
            print('Incorrect IPv4 address')
            continue
        elif 0 <= ip[0] <= 127:
            print(('ip {} сlass A').format(ip_address))
            break
        elif 128 <= ip[0] <= 191:
            print(('ip {} сlass B').format(ip_address))
            break
        elif 192 <= ip[0] <= 223:
            print(('ip {} сlass C').format(ip_address))
            break
        elif 224 <= ip[0] <= 239:
            print(('ip {} сlass D').format(ip_address))
            break
        elif ip_address == '255.255.255.255':
            print(('ip {} local broadcast').format(ip_address))
            break
        elif ip_address == '0.0.0.0':
            print(('ip {} unassigned').format(ip_address))
            break
        else:
            print('unused')
            break
