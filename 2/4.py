# -- coding: utf-8 --
def x():
    a = int(input('Расстояние между рядами - '))
    b = int(input('Расстояние между отверстиями в ряду - '))
    l = int(input('Длина свободного конца шнурка - '))
    N = int(input('Количество отверстий в ряду - '))
    return (2 * N - 1 ) * a + 2 * l + 2 * (N - 1) * b
print(x()) 