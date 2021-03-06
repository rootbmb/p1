
# -*- coding: utf-8 -*-
'''
Задание 4.1a
Всё, как в задании 4.1.
Но, если пользователь ввел адрес хоста, а не адрес сети,
то надо адрес хоста преобразовать в адрес сети и вывести адрес сети и маску, как в задании 4.1.
Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16
Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30
Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:
Network:
10        0         1         0
00001010  00000000  00000001  00000000
Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000
Проверить работу скрипта на разных комбинациях сеть/маска.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

masks = {
    "0": "0.0.0.0",
    "1": "128.0.0.0",
    "2": "192.0.0.0",
    "3": "224.0.0.0",
    "4": "240.0.0.0",
    "5": "248.0.0.0",
    "6": "252.0.0.0",
    "7": "254.0.0.0",
    "8": "255.0.0.0",
    "9": "255.128.0.0",
    "10": "255.192.0.0",
    "11": "255.224.0.0",
    "12": "255.240.0.0",
    "13": "255.248.0.0",
    "14": "255.252.0.0",
    "15": "255.254.0.0",
    "16": "255.255.0.0",
    "17": "255.255.128.0",
    "18": "255.255.192.0",
    "19": "255.255.224.0",
    "20": "255.255.240.0",
    "21": "255.255.248.0",
    "22": "255.255.252.0",
    "23": "255.255.254.0",
    "24": "255.255.255.0",
    "25": "255.255.255.128",
    "26": "255.255.255.192",
    "27": "255.255.255.224",
    "28": "255.255.255.240",
    "29": "255.255.255.248",
    "30": "255.255.255.252",
    "31": "255.255.255.254",
    "32": "255.255.255.255"
}

bin_mask = {'31': '0',
            '30': '00',
            '29': '000',
            '28': '0000',
            '27': '00000',
            '26': '000000',
            '25': '0000000',
            '24': '00000000',
            '23': '000000000',
            '22': '0000000000',
            '21': '00000000000',
            '20': '000000000000',
            '19': '0000000000000',
            '18': '00000000000000',
            '17': '000000000000000',
            '16': '0000000000000000',
            '15': '00000000000000000',
            '14': '000000000000000000',
            '13': '0000000000000000000',
            '12': '00000000000000000000',
            '11': '000000000000000000000',
            '10': '0000000000000000000000',
            '9': '00000000000000000000000',
            '8': '000000000000000000000000',
            '7': '0000000000000000000000000',
            '6': '00000000000000000000000000',
            '5': '000000000000000000000000000',
            '4': '0000000000000000000000000000',
            '3': '00000000000000000000000000000',
            '2': '000000000000000000000000000000',
            '1': '0000000000000000000000000000000'}

subnet = input("Введите адрес сети в формате 10.1.1.0/24: ")
net_info = subnet.split("/")
net_ip = net_info[0]
net_mask = net_info[1]

net_ip = net_ip.split('.')

# Переводим в bin адрес

bin_ip = ('{:08b}{:08b}{:08b}{:08b}').format(
    int(net_ip[0]), int(net_ip[1]), int(net_ip[2]), int(net_ip[3]))

# Получаем единую строку и срез по битам

bin_ip = ('').join(bin_ip)
new_net_mask = bin_mask[net_mask]
new_bin_ip = bin_ip[:int(net_mask)] + new_net_mask

'''
ну а дальше все и так понятно
'''

new_ip_net = [int(new_bin_ip[:8], 2), int(new_bin_ip[8:16], 2), int(
    new_bin_ip[16:24], 2), int(new_bin_ip[24:32], 2)]

print("Network:")
print(('{:<8} {:<8} {:<8} {:<8}').format(
    new_ip_net[0], new_ip_net[1], new_ip_net[2], new_ip_net[3]))

print(('{:08b} {:08b} {:08b} {:08b}').format(
    int(new_ip_net[0]), int(new_ip_net[1]),
    int(new_ip_net[2]), int(new_ip_net[3])))

print("Mask:")
print("/" + net_mask)
net_mask = masks[net_mask]

net_mask = net_mask.split('.')
print(('{:8} {:8} {:8} {:8}').format(
    net_mask[0], net_mask[1], net_mask[2], net_mask[3]))

print(('{:08b} {:08b} {:08b} {:08b}').format(
    int(net_mask[0]), int(net_mask[1]), int(net_mask[2]), int(net_mask[3])))
