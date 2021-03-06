'''
Аналогично заданию 3.6 обработать строки из файла ospf.txt и вывести информацию
по каждой в таком виде:
Protocol: OSPF
Prefix: 10.0.24.0/24
AD/Metric: 110/41
Next-Hop: 10.0.13.3
Last update: 3d18h
Outbound Interface: FastEthernet0/0
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ospf_route = open('ospf.txt', 'r')

ospf_route = ospf_route.read().split()
AttributProtocol = ['Protocol', 'Prefix', 'AD/Metric',
                    'Next-Hop', 'Last update', 'Outbound Interface']

ospf_route1 = dict.fromkeys(AttributProtocol)
ospf_route1['Protocol'] = ospf_route[0]
ospf_route1['Prefix'] = ospf_route[1]
ospf_route1['AD/Metric'] = ospf_route[2]
ospf_route1['Next-Hop'] = ospf_route[4]
ospf_route1['Last update'] = ospf_route[5]
ospf_route1['Outbound Interface'] = ospf_route[6]
print()
print('{}:{:>17}\n{}:{:>27}\n{}:{:>18}\n{}:{:>22}\n{}:{:>15}\n{}:{:>18}\n'
      .format(
          AttributProtocol[0], ospf_route1[AttributProtocol[0]],
          AttributProtocol[1], ospf_route1[AttributProtocol[1]],
          AttributProtocol[2], ospf_route1[AttributProtocol[2]
                                           ].strip('[]'),
          AttributProtocol[3], ospf_route1[AttributProtocol[3]
                                           ].strip(','),
          AttributProtocol[4], ospf_route1[AttributProtocol[4]
                                           ].strip(','),
          AttributProtocol[5], ospf_route1[AttributProtocol[5]]))
