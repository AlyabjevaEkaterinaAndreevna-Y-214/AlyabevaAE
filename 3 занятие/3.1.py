# -- coding: utf-8 --
a = int (input ('a= '))
b = int (input ("b= "))
if a <= b:
	for i in range(a, b+1):
		print(i)
else:
	print("ОШИБКА! ВВЕДИТЕ ЧИСЛА СООТВЕТСТВУЮЩИЕ УСЛОВИЮ a<b")