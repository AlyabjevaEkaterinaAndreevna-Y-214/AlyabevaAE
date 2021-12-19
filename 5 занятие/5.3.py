#-- coding: utf-8 --

N = int(input("ВВЕДИТЕ ЧИСЛО N "))
k = 2
g = 1
m = 1
while k <= N:
    k *= 2
    g += 1
    m = k/2
print("ПОКАЗАТЕЛЬ ", g - 1, ", ЧИСЛО", m )

