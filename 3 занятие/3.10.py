# -- coding: utf-8 --
def k():
    N = int(input('N= '))
    C = int(input('C= '))
    a = 0
    b = 1
    s = 0
    if C < 3:
        s += 1
    for i in range(2, N):
        num = a + b
        a, b = b, num
        if i >= (C-1):
            s += num
    print(s)
k()