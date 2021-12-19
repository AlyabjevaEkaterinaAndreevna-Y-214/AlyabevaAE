# -- coding: utf-8 --

def vtoroezadanieAlyab():
    i = 2
    N = int(input("ВВЕДИТЕ ЧИСЛО НЕ МЕНЬШЕЕ 2 "))
    while N % i != 0:
        i += 1
    print("НАИМЕНЬШИЙ НАТУРАЛЬНЫЙ ДЕЛИТЕЛЬ ", i)
vtoroezadanieAlyab()