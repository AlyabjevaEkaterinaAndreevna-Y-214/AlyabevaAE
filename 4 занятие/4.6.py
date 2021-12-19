# -- coding: utf-8 --
def k():
    s = input("ВВЕДИТЕ СТРОКУ ")
    if s.count("f") >= 2:
        s = s.replace("f", " ", 1)
        print("ИНДЕКС ВТОРОГО ВХОЖДЕНИЯ БУКВЫ f: ",s.find("f"))
    elif s.count("f") == 1:
        print("ЗНАЧЕНИЕ ЕСЛИ БУКВА f ВСТРЕЧЕНА ЕДИНОЖДЫ ",-1)
    else:
        print("ЗНАЧЕНИЕ ЕСЛИ БУКВА f НЕ ВСТРЕЧЕНА",-2)
k()