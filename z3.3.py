'''

Получить из строки CONFIG список VLANов вида: ['1', '3', '10', '20', '30', '100'] 
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
CONF = CONFIG.split()
VLANS = CONF[-1].split(',')

print(VLANS)
