'''
Задание 3.7
Преобразовать MAC-адрес в двоичную строку (без двоеточий).
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
MAC = 'AAAA:BBBB:CCCC'
mac = MAC.split(':')
print(mac)
new_mac = "".join(mac)
print(new_mac)
print(bin(int(new_mac, 16)))
