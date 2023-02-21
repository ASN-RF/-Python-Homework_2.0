# **Python-Homework_2.0**
## Домашние задание № 1
**Задача 1.** *Найдите сумму цифр трехзначного числа.* <br>
`Пример`:
```
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
```
<br>

**Задача 2.** *Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?* <br>
`Пример`:
```
6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10
```
<br>

**Задача 3.** *Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.* <br>
`Пример`:
```
385916 -> yes
123456 -> no
```
<br>

**Задача 4.** *Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).* <br>
`Пример`:
```
3 2 4 -> yes
3 2 1 -> no
```
<br>

* * *

## Домашние задание № 2
**Задача 1 (10).** *На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть. Пользователь будет вводить каждое число на новой строке.* <br>
`Пример`:
```
5 -> 1 0 1 1 0
2
```
<br>

**Задача 2 (12).** *Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числ. Пользователь будет вводить каждое число на новой строке.* <br>
`Пример`:
```
4 4 -> 2 2
5 6 -> 2 3
```
<br>

**Задача 3 (14).** *Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.* <br>
`Пример`:
```
10 -> 1 2 4 8
```
<br>

* * *

## Домашние задание № 3
**Задача 1 (16).** *Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.* <br>
`Пример`:
```
5
1 2 3 4 5
3
-> 1
```
<br>

**Задача 2 (18).** *Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.* <br>
`Пример`:
```
5
1 2 3 4 5
6
-> 5
```
<br>

**Задача 3 (20).** *В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.* <br>В случае с английским алфавитом очки распределяются так: <br>
A, E, I, O, U, L, N, S, T, R – 1 очко;<br>
D, G – 2 очка;<br>
B, C, M, P – 3 очка;<br>
F, H, V, W, Y – 4 очка;<br>
K – 5 очков;<br>
J, X – 8 очков;<br>
Q, Z – 10 очков.<br><br>
А русские буквы оцениваются так:<br>
А, В, Е, И, Н, О, Р, С, Т – 1 очко;<br>
Д, К, Л, М, П, У – 2 очка;<br>
Б, Г, Ё, Ь, Я – 3 очка;<br>
Й, Ы – 4 очка;<br>
Ж, З, Х, Ц, Ч – 5 очков;<br>
Ш, Э, Ю – 8 очков;<br>
Ф, Щ, Ъ – 10 очков.<br>
*Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.* <br>
`Пример`:
```
Ввод:
ноутбук
Вывод:
12
```
<br>

## Домашние задание № 4
**Задача 1 (22).** *Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.* <br>
`Пример`:
```
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12
```
<br>

**Задача 2 (24).** *В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним. <br> Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.* <br>

`Пример`:
```
4 -> 1 2 3 4
9 
```
<br>

## Домашние задание № 5
**Задача 1 (26).** *Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.* <br>
`Пример`:
```
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
```
<br>

**Задача 2 (28).** *Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.* <br>
`Пример`:
```
2 2
4
```
<br>

## Домашние задание № 6
**Задача 1 (30).** *Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.* <br>

**Задача 2 (32).** *Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума).* <br>