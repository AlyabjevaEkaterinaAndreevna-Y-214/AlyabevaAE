# -- coding: utf-8 --
def k():
    n = int(input("ВВЕДИТЕ ЧИСЛО n "))
    s = 0
    for i in range (1, n+1):
        s = s + i**3
    print("СУММА РАВНА ",s)
k()