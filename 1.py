# -*- coding: utf-8 -*-
"""
Задание 4.1

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.
"""

network = input('Введите адрес сети: ')

# Вариант без использования генераторов списка

ip, mask = network.split('/')
ip_list = ip.split('.')
mask = int(mask)

# Преобразуем каждый октет адреса в int
# и записываем каждый октет адреса в отдельную переменную
oct1, oct2, oct3, oct4 = [int(ip_list[0]), int(ip_list[1]),
                          int(ip_list[2]), int(ip_list[3])]

bin_mask = '1' * mask + '0' * (32 - mask)
# Разделение по октетам:
bin_mask = [bin_mask[0:8], bin_mask[8:16], bin_mask[16:24], bin_mask[24:32]]
# Преобразование в int:
m1, m2, m3, m4 = [int(bin_mask[0], 2), int(bin_mask[1], 2),
                  int(bin_mask[2], 2), int(bin_mask[3], 2)]


ip_output = '''
Network:
{:<8}  {:<8}  {:<8}  {:<8}
{:08b}  {:08b}  {:08b}  {:08b}'''

mask_output = '''
Mask:
/{}
{:<8}  {:<8}  {:<8}  {:<8}
{:08b}  {:08b}  {:08b}  {:08b}
'''

print(ip_output.format(oct1, oct2, oct3, oct4,
                       oct1, oct2, oct3, oct4))

print(mask_output.format(mask,
                         m1, m2, m3, m4,
                         m1, m2, m3, m4))


# Вариант с генераторами списка
ip, mask = network.split('/')
mask = int(mask)

# каждый октет адреса в отдельной переменной
oct1, oct2, oct3, oct4 = [int(i) for i in ip.split('.')]

bin_mask = '1' * mask + '0' * (32 - mask)
# Каждый октет маски в отдельной переменной
m1, m2, m3, m4 = [int(bin_mask[i:i + 8], 2) for i in [0, 8, 16, 24]]

ip_output = '''
Network:
{:<8}  {:<8}  {:<8}  {:<8}
{:08b}  {:08b}  {:08b}  {:08b}'''

mask_output = '''
Mask:
/{}
{:<8}  {:<8}  {:<8}  {:<8}
{:08b}  {:08b}  {:08b}  {:08b}
'''

print(ip_output.format(oct1, oct2, oct3, oct4,
                       oct1, oct2, oct3, oct4))

print(mask_output.format(mask,
                         m1, m2, m3, m4,
                         m1, m2, m3, m4))


# еще можно в шаблоне указывать номер аргумента, чтобы не нужно было повторять их
ip_output = '''
Network:
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}'''

mask_output = '''
Mask:
/{0}
{1:<8}  {2:<8}  {3:<8}  {4:<8}
{1:08b}  {2:08b}  {3:08b}  {4:08b}
'''

print(ip_output.format(oct1, oct2, oct3, oct4))
print(mask_output.format(mask, m1, m2, m3, m4))
