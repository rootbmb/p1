'''
Задание 4.1
Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24
Затем вывести информацию о сети и маске в таком формате:
Network:
10 1 1 0
00001010 00000001 00000001 00000000
255 255 255 0
11111111 11111111 11111111 00000000
Mask:
/24
Проверить работу скрипта на разных комбинациях сеть/маска.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
IP = input('введите IP адрес в формате:10.1.1.0/24 -- ')
new_IP = IP.split('/')
Mask = new_IP.pop(-1)
print(Mask)
print(new_IP)
IP = '.'.join(new_IP).split('.')
print(IP)
print('Network:\n', ("{:10} {:10} {:10} {:10}").format(
    IP[0], IP[1], IP[2], IP[3]), '\n', ("{:10} {:10} {:10} {:10}").format(bin(
        int(IP[0])), bin(int(IP[1])), bin(int(IP[2])), bin(int(IP[3]))))
print('-' * 44)
mask_net = int(Mask) // 8
print(mask_net)
m = {}
#a = ['255' for i in range(mask_net)]
# print(a)

#
'''MASK = mask_net.split()
print('Mask:', '\n', '/' + Mask)
print((" {:10} {:10} {:10} {:10}").format(
    MASK[0], MASK[1], MASK[2], MASK[3]), '\n', ("{:10} {:10} {:10} {:10}").format(bin(
        int(MASK[0])), bin(int(MASK[1])), bin(int(MASK[2])), bin(int(MASK[3]))))

print('-' * 44)
'''
