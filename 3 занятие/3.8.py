# -- coding: utf-8 --
def k():
    n = int(input("ВВЕДИТЕ ЧИСЛО ПО ЗАДАННОМУ УСЛОВИЮ n<=9 "))
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, sep='', end='')
        print()
k() 