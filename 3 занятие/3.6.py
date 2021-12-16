# -- coding: utf-8 --
def k():
    FACTORIAL=1
    n=int(input("ВВЕДИТЕ ЧИСЛО "))
    for i in range(1, n + 1):
        FACTORIAL *= i
    print(FACTORIAL)
k()