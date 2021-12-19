# -- coding: utf-8 --

def chetvertoezadanieALYAB():
    X = int(input("ВВЕДИТЕ КОЛИЧЕСТВО КИЛОМЕТРОВ В ПЕРВЫЙ ДЕНЬ "))
    Y = int(input("ВВЕДИТЕ КОЛИЧЕСТВО КИЛОМЕТРОВ КОТОРОЕ ДОЛЖЕН ПРОБЕЖАТЬ СПОРТСМЕН "))
    SPORTSMEN = 1
    while X < Y:
        X *= 1.1
        SPORTSMEN += 1
    print("НОМЕР ДНЯ В КОТОРЫЙ СПОРТСМЕН ПРОБЕЖИТ Y КИЛОМЕТРОВ ", SPORTSMEN)
chetvertoezadanieALYAB()