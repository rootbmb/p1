# -*- coding: utf-8 -*-
username = input('Введите имя пользователя: ')
password = input('Введите пароль: ')
password_correct = False
while not password_correct:
    if len(password) < 8:
        print('Пароль слишком короткий\n')
        password = input('Введите пароль еще раз: ')
    elif username in password:
        print('Пароль содержит имя пользователя\n')
        password = input('Введите пароль еще раз: ')
    else:
        print('Пароль для пользователя {} установлен'.format(username))
        password_correct = True
