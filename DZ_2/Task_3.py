# Задача 3 (14). Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

Chislo = int(input('Введите Ваше любимое число: '))
Chisla_rezult = []
dvoika = 1
while dvoika <= Chislo:
    Chisla_rezult.append(dvoika)
    dvoika *=2
print (f'{Chislo} -> ', end='')
print (*Chisla_rezult)
