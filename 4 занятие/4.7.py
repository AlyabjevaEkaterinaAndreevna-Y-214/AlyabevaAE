# -- coding: utf-8 --
def k():
    s = input("ВВЕДИТЕ СТРОКУ В КОТОРОЙ БУКВА h БУДЕТ ВСТРЕЧЕНА НЕ МЕНЕЕ 2 РАЗ ")
    s = s[:s.find("h")] + s[s.rfind("h")+1:]
    print("ВЫВОД СТРОКИ БЕЗ ПЕРВОЙ И ПОСЛЕДНЕЙ h И ВСЕХ БУКВ МЕЖДУ НИМИ ", s)
k()