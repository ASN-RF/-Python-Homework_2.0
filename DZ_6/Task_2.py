# Задача 2 (32). Определить индексы элементов массива (списка), значения которых принадлежат заданному
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума).

# -------- МОЁ РЕШЕНИЕ ---------
# import random   
# Dlina_spiska = int(input('Введите длину списка: '))    # подумал, что длину задает пользователь
# Spisok = [random.randint(-99, 99) for i in range(Dlina_spiska)]  # подумал, заполнить случайными числами
# min_spiska = int(input('Введите минимум: '))
# max_spiska = int(input('Введите максимум: '))
# Rezult = [i for i in range(Dlina_spiska) if min_spiska <= Spisok[i] <= max_spiska]
# print (f'{Spisok}\n{Rezult}')


# -------- ЭТАЛОННОЕ РЕШЕНИЕ ---------
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = int(input())
max_number = int(input())
for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        print(i)