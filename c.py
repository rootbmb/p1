# -*- coding: Windows-1251 -*-
# Сочетания
# ПРОГРАММА ДЛЯ ГЕНЕРИРОВАНИЯ
# ВСЕХ ПОДМНОЖЕСТВ k МНОЖЕСТВА ЧИСЕЛ n=1..nElem
# макс. число элементов в
# множестве:
MAX_ELEM = 30
#число элементов в
# подмножестве:
k = 0
# список, содержащий
# очередное подмножество:
a = []
# номер подмножества:
nSubset = 0
# ГЛАВНАЯ ФУНКЦИЯ


def main():
    print('Генерируем сочетания')
    print()
    global k
    # бесконечный цикл ввода данных -
    # пока пользователь не закроет программу
    # или не введет 0:
    while True:
        s = "Число элементов (1.." + str(MAX_ELEM) + ") > "
        print(s, end='')
        # число элементов:
        nElem = int(input())
        # если пользователь ввёл 0,
        # то программу закрываем:
        if (nElem == 0):
            return
        # считываем число элементов подмножества:
        s = "Число элементов в подмножестве (1.." + str(nElem) + ") > "
        print(s, end='')
        k = int(input())
        if (k > nElem):
            print("Повторите ввод!")
            print()
            continue

        # генерируем все подмножества:
        n = SubSet(nElem)
        print("Число сочетаний = " + str(n))
        print()
#//Генерируем все сочетания множества
#//из k элементов
# Генерируем все сочетания множества 1..nElem


def SubSet(nElem):
    global nSubset
    global a
    a.append(0)
    for i in range(1, k + 1):
        a.append(i)
    nSubset = 0
    p = k
    while (p >= 1):
        # печатаем очередное подмножество:
        nSubset += 1
        WriteSubset()
        if (k == nElem):
            break
        if (a[k] == nElem):
            p -= 1
        else:
            p = k
        if (p >= 1):
            for i in range(k, p - 1, -1):
                a[i] = a[p] + i - p + 1

    return nSubset

# ПЕЧАТАЕМ ОЧЕРЕДНУЮ ПЕРЕСТАНОВКУ
# ЭЛЕМЕНТОВ МНОЖЕСТВА


def WriteSubset():
    if (nSubset > 29):
        return
    s = ""
    if (nSubset < 1000):
        s += " "
    if (nSubset < 100):
        s += " "
    if (nSubset < 10):
        s += " "
        s += str(nSubset) + "> "
    for i in range(1, k + 1):
        s += str(a[i]) + " "
    print(s)


main()
