# Задача 1. Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

def Otvet(x, y):
    print(f'{x} -> {y} ({x//100} + {x//10-(10*(x//100))} + {x-(10*(x//10))})')


# 1 вариант. Цикл
# Chislo = int(input('Введите Ваше любимое целое трёхзначное число:  '))
# Chislo_otvet = Chislo
# while Chislo > 999 or Chislo < 100:
#     if Chislo > 999:
#         print (f'Дорогой друг возьми число, поменьше хотя бы на {Chislo - 999}')
#     else:
#         print (f'Дорогой друг возьми число, поменьше хотя бы на {100 - Chislo}')
#     Chislo = int(input('Итак, твое другое любимое целое ТРЁХзначное число:  '))
# sum = 0
# while Chislo > 0:
#     sum += int(Chislo % 10)
#     Chislo /= 10
# print(sum)
# Otvet (Chislo_otvet, sum)

# 2 вариант. Строки. (В данном решении "дорого" проверять число на трехзначность, будем пологаться на пользователя)
Chislo = input('Введите Ваше любимое целое трёхзначное число:  ')
Chislo_otvet = int(Chislo)
sum = 0
for i in Chislo:
    sum += int(i)
print(sum)
Otvet(Chislo_otvet, sum)

# 3 вариант. Разбор домашнего задания.
number = int(input())
if number < 0:
    number = number * -1
a = number // 100
b = number % 100 // 10
c = number % 10
print(a + b + c)
