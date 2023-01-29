# Задача 3. Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали
# билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех
# цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется
# написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no
Nomer_bileta = int(input('Введите номер Вашего билета: '))
print(f'{Nomer_bileta} -> ', end='')
# 1 вариант. Строки.
# !!! Переформатировал из int in str, чтобы первоначальный ввод подошел для всех вариантов решения
# Nomer_bileta_str = str(Nomer_bileta)
# schetchik = 0
# Pervay_polovina = 0
# Ftoray_polovina = 0
# for i in Nomer_bileta_str:
#     if schetchik < 3:
#         Pervay_polovina += int(i)
#     else:
#         Ftoray_polovina += int(i)
#     schetchik += 1
# if Pervay_polovina == Ftoray_polovina:
#     print ('YES')
# else:
#     print ('NO')

# 2 вариант. Числа
# Pervay_polovina = Nomer_bileta // 1000
# sum_1 = 0
# while Pervay_polovina > 10:
#     sum_1 += Pervay_polovina % 10
#     Pervay_polovina //= 10
# sum_1 += Pervay_polovina

# sum_2 = 0
# Ftoray_polovina = (Nomer_bileta/1000 - Nomer_bileta//1000)*1000
# while Ftoray_polovina > 10:
#     sum_2 += Ftoray_polovina % 10
#     Ftoray_polovina //= 10
# sum_2 += Ftoray_polovina
# if round (sum_1) == round (sum_2):
#     print ('YES')
# else:
#     print ('NO')

# 3 вариант. Числа (аналог 2, цикл отделил функцией)
def sum_rezult (x):
    sum_x = 0
    while x > 10:
        sum_x += x % 10
        x //= 10
    sum_x += x
    return(round(sum_x))
if sum_rezult (Nomer_bileta // 1000) == sum_rezult ((Nomer_bileta/1000 - Nomer_bileta//1000)*1000):
    print ('YES')
else:
    print ('NO')   


# 4 вариант. Числа (еще вариант с ФУНКЦИЕЙ)
# def summa_chisla(x, y):
#     summa = 0
#     while x > y:
#         summa += x % 10
#         x //= 10
#     if x < 99:
#         summa += x
#     return (summa)
# if summa_chisla(Nomer_bileta//1000, 10) == summa_chisla(Nomer_bileta, 1000):
#     print ('YES')
# else:
#     print ('NO')
