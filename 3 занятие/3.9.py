# -- coding: utf-8 --
def k():
    n = int(input("ВВЕДИТЕ ЧИСЛО n "))
    a = 0
    b = 1
    summa = 1
    c = 0
    for i in range(2, n+1):
        summa += c
        c = a + b
        a, b = b, c
    print(summa)
k()