# Задача 2 (18). Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример:
# 5
# 1 2 3 4 5
# 6
# -> 5

N = int(input('Введите Ваше любимое натуральное число N: '))
Spisok = [int(input(f'Введите {i+1} число: '))
          for i in range(N)]  # 1 вариант ввода
# Spisok = map(int, (input(f'Введите {N} Ваших любимых натуральных чисел через пробел: \n').split())) #2 вариант ввода
x = int(input('Введите число X: '))
# min_raznost = x-Spisok[0]
# i, ind = 0, 0
# for chislo in Spisok:
#     raznost = x - chislo
#     if min_raznost > raznost:
#         ind = i
#     i += 1
# 2 вариант
ind = 0
for i in range(len(Spisok)):
    if (x-Spisok[i]) < x-ind and x-Spisok[i] > 0:
        ind = i
print(N)
print(*Spisok)
print(x)
print(f'-> {Spisok[ind]}')
