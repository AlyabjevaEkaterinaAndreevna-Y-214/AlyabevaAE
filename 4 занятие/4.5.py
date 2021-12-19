# -- coding: utf-8 --
def k():
    s = input("ВВЕДИТЕ СТРОКУ ")
    if s.count('f') == 1:
        print(s.find('f')+1)
    elif s.count('f') >= 2:
        print("ВЫВОД ИНДЕКСА F/ВЫВОД ПЕРВОГО И ПОСЛЕДНЕГО ИНДЕКСА F ЕСЛИ F>1/НЕ ВЫВОДИТСЯ НИЧЕГО ЕСЛИ F=0: ", s.find('f')+1, " ", s.rfind('f'))
k()