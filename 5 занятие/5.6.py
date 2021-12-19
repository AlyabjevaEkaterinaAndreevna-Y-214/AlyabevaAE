# -- coding: utf-8 --

N=int(input("ВВЕДИТЕ ЧИСЛО "))
a=0
b=0
while N!= 0:
    b+=N
    N=int(input("ВВЕДИТЕ ЧИСЛО"))
    a+=1
print("СРЕДНЕЕ ЗНАЧЕНИЕ ",b/a)
