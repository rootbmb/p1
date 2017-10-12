'''
Задание 3.9
Найти индекс последнего вхождения элемента.
Например, для списка num_list, число 10 последний раз встречается с индексом 4; в
списке word_list, слово 'ruby' последний раз встречается с индексом 6.
Сделать решение общим (то есть, не привязываться к конкретному элементу в
конкретном списке) и проверить на двух списках, которые указаны и на разных
элементах.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
num_list = [10, 2, 30, 100, 10, 50, 11, 30]
word_list = ['python', 'ruby', 'perl',
             'ruby', 'perl', 'python', 'ruby', 'perl']

find_int = int(input('Enter the element from "num_list": '))
last_index = len(num_list) - 1 - num_list[::-1].index(find_int)
print('Last index of the element ', find_int, ' is ', last_index)

find_word = input('Enter the element from "word_list": ')
last_index = len(word_list) - 1 - word_list[::-1].index(find_word)
print('Last index of the element ', find_word, ' is ', last_index)
