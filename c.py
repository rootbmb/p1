# -*- coding: Windows-1251 -*-
# ���������
# ��������� ��� �������������
# ���� ����������� k ��������� ����� n=1..nElem
# ����. ����� ��������� �
# ���������:
MAX_ELEM = 30
#����� ��������� �
# ������������:
k = 0
# ������, ����������
# ��������� ������������:
a = []
# ����� ������������:
nSubset = 0
# ������� �������


def main():
    print('���������� ���������')
    print()
    global k
    # ����������� ���� ����� ������ -
    # ���� ������������ �� ������� ���������
    # ��� �� ������ 0:
    while True:
        s = "����� ��������� (1.." + str(MAX_ELEM) + ") > "
        print(s, end='')
        # ����� ���������:
        nElem = int(input())
        # ���� ������������ ��� 0,
        # �� ��������� ���������:
        if (nElem == 0):
            return
        # ��������� ����� ��������� ������������:
        s = "����� ��������� � ������������ (1.." + str(nElem) + ") > "
        print(s, end='')
        k = int(input())
        if (k > nElem):
            print("��������� ����!")
            print()
            continue

        # ���������� ��� ������������:
        n = SubSet(nElem)
        print("����� ��������� = " + str(n))
        print()
#//���������� ��� ��������� ���������
#//�� k ���������
# ���������� ��� ��������� ��������� 1..nElem


def SubSet(nElem):
    global nSubset
    global a
    a.append(0)
    for i in range(1, k + 1):
        a.append(i)
    nSubset = 0
    p = k
    while (p >= 1):
        # �������� ��������� ������������:
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

# �������� ��������� ������������
# ��������� ���������


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
