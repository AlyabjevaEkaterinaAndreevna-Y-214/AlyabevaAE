# -- coding: utf-8 --
def k():
    s = input("ВВЕДИТЕ СТРОКУ ")
    s1 = s[:len(s)-len(s)//2]
    s2 = s[len(s)-len(s)//2:]
    s1,s2 = s2,s1
    s = s1+s2
    print("РЕЗУЛЬТАТ ", s)
k()