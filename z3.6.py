'''Обработать строку ospf_route и вывести информацию на стандартный поток вывода в
виде:
Protocol: OSPF
Prefix: 10.0.24.0/24
AD/Metric: 110/41
Next-Hop: 10.0.13.3
Last update: 3d18h
Outbound Interface: FastEthernet0/0
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ospf_route = 'OSPF         10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

ospf_route = ospf_route.split()
print(ospf_route)
AttributProtocol = ['Protocol', 'Prefix', 'AD/Metric',
                    'Next-Hop', 'Last update', 'Outbound Interface']

# OSPF = dict(AttributProtocol[0]=ospf_route[0], AttributProtocol[1]=ospf_route[1], AttributProtocol[2]=ospf_route[2])

ospf_route1 = dict.fromkeys(AttributProtocol)

print(ospf_route1)
ospf_route1['Protocol'] = ospf_route[0]
ospf_route1['Prefix'] = ospf_route[1]
ospf_route1['AD/Metric'] = ospf_route[2]
ospf_route1['Next-Hop'] = ospf_route[4]
ospf_route1['Last update'] = ospf_route[5]
ospf_route1['Outbound Interface'] = ospf_route[6]


print(ospf_route1)
