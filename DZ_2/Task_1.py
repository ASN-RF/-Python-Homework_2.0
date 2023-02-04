# Задача 1 (10). На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
# Пример:
# 5 -> 1 0 1 1 0
# 2
# 1 вариант
Kol_monet = int (input('Введите сколько монет должно лежать на столе: '))
Sum_reshka = 0
Sum_gerb = 0
Storoni_monet = []
for i in range (Kol_monet):
    Storoni_monet.append (int(input(f'Какой стороной лежит {i} монетка? 1 - герб, 0 - решка.\nИтак: ')))
    
for i in Storoni_monet:
    if i == 0:
        Sum_reshka +=1
    elif i == 1:
        Sum_gerb +=1
        
if Sum_reshka > Sum_gerb:
    Kol_perevernut = Kol_monet - Sum_reshka
else:
    Kol_perevernut = Kol_monet - Sum_gerb
print(f'\n{Kol_perevernut}')
print(f'{Kol_monet} -> {Storoni_monet}\n{Kol_perevernut}')