
def arithmetic(a, b, fun):
    if fun == '*':
        c = a * b
    elif fun == '-':
        c = a - b
    elif fun == '/':
        c = a / b
    elif fun == '//':
        c = a // b
    elif fun == '+':
        c = a + b
    else:
        c = 'not fun'
        print(c)
    return c


n = ('+', '*', '-', '/', '//', 'tjgirtg')
for i in n:
    print(arithmetic(10, 20, i))
print()
