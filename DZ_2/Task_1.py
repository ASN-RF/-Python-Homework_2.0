# Задача 1 (10). На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
# Пример:
# 5 -> 1 0 1 1 0
# 2
# ------------------- 1 вариант -------------------------

# Kol_monet = int (input('Введите сколько монет должно лежать на столе: '))
# Sum_reshka = 0
# Sum_gerb = 0
# Storoni_monet = []
# Otvet_storona = str('Решка')
# for i in range (Kol_monet):
#     Storona_monet = int(input(f'Какой стороной лежит {i+1} монетка? 1 - герб, 0 - решка.\nИтак: '))
#     while Storona_monet < 0 or Storona_monet > 1:
#         Storona_monet = int(input(f'Монета {i}, может упасть только 1 или 0, 1 - герб, 0 - решка.\nИтак: '))
#     Storoni_monet.append (Storona_monet)
    
# for i in Storoni_monet:
#     if i == 0:
#         Sum_reshka +=1
#     elif i == 1:
#         Sum_gerb +=1
        
# if Sum_reshka > Sum_gerb:
#     Kol_perevernut = Kol_monet - Sum_reshka
# else:
#     Kol_perevernut = Kol_monet - Sum_gerb
#     Otvet_storona = str('Герб')
# # print(f'\n{Kol_perevernut}')
# print(f'{Kol_monet} -> ', end='')
# print (*Storoni_monet)
# print (Kol_perevernut)
# print('Пояснение: ')
# print(f'При подкидывании монеты {Kol_monet} раз(а), {Kol_monet - Kol_perevernut} раз(а) выпал(а) {Otvet_storona}\nПоэтому минимальным количеством монет, которые нужно перевернуть, будет {Kol_perevernut}.')

# ------------------- 2 вариант -------------------------
import random
stack_size = int(input('Введиите количество монет: '))
coins = [random.randint(0,1) for _ in range(stack_size)]
print (*coins)
if coins.count(1) < coins.count(0):
    print(f'Переверни единички! ИХ {coins.count(1)}')
elif coins.count(1) > coins.count(0):
    print(f'Переверни нолики! ИХ {coins.count(0)}')
else:
    print(f'Переверни что хочешь! Любой цифры {coins.count(0)}')