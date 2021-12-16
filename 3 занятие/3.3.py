# -- coding: utf-8 --
a = int(input("a= "))
b = int(input("b= "))
for i in range(a - a % 2 -1, b -1, -2):
    print(i)