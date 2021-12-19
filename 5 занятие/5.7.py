# -- coding: utf-8 --

def sedimoezadanieALYAB():
    k = 0
    N = int(input('ВВЕДИТЕ N'))
    while N != 0:
        x = int(input('ВВЕДИТЕ X '))
        if N < x:
            k += 1
        N = x
    print("КОЛИЧЕСТВО ЭЛЕМЕНТОВ ПРЕВОСХОДЯЩИХ ПРЕДЫДУЩИЙ ЭЛЕМЕНТ ", k)
sedimoezadanieALYAB()
