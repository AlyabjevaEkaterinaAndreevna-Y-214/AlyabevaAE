# -- coding: utf-8 --
def k():
    FACTORIAL=1
    n=int(input("ВВЕДИТЕ ЧИСЛО "))
    summa=0
    for i in range(1, n + 1):
        FACTORIAL *= i
        summa=summa+FACTORIAL
    print("СУММА ФАКТОРИАЛОВ= ",summa)
k()