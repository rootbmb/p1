'''
Из строк command1 и command2 получить список VLANов, которые есть и в команде
command1 и в команде command2.
Для данного примера, результатом должен быть список: [1, 3, 100] Этот список
содержит подсказку по типу итоговых данных.
Ограничение: Все задания надо выполнять используя только пройденные темы.
command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
'''
command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

com1 = command1.split()
vlan1 = com1[-1].split(',')
print(vlan1)
com2 = command2.split()
vlan2 = com2[-1].split(',')
print(vlan2)

VLAN = (set(vlan1) & set(vlan2))
VLAN = list(VLAN)

print(VLAN)
