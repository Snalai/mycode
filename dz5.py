"""
Задание 1. Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""

def kal(zna):
    zna = input("+, -, *, / или 0 для выхода: ")
    if zna != "0":
        if (zna != "0" and zna == "+") or (zna != "0" and zna == "-") or (zna != "0" and zna == "*") or (
                zna != "0" and zna == "/"):
            try:
                firs_n = int(input('Введите первое число: '))
                secn_n = int(input('Введите второе число: '))
            except ValueError:
                print("Вы вместо трехзначного числа ввели строку (((")
            else:
                if zna == "+":
                    print(f"Сумма равна: {firs_n + secn_n}")
                elif zna == "-":
                    print(f"Разница равна: {firs_n - secn_n}")
                elif zna == "*":
                    print(f"Произведение равно: {firs_n * secn_n}")
                elif zna == "/":
                    if secn_n == 0:
                        print("на ноль делить нельзя")
                    else:
                        print(f"Частное равно: {firs_n / secn_n}")
        elif zna == 0:
            return print("sps")
        else:
            print("Вы не ввели +, -, *, / или 0 для выхода: ")
        return kal(zna)
    elif zna == "0":
        return print("sps")
    else:
        return kal(zna)


kal(None)

"""

Задание 2. Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""
sch = 0
n_chet = 0


def chet(num_p):
    global sch, n_chet
    if num_p == 0:
        return print(f"Количество четных и нечетных цифр в числе равно: ({sch}, {n_chet})")
    elif num_p > 0:
        if ((num_p % 10) % 2) == 0:
            sch = sch + 1
        else:
            n_chet = n_chet + 1
    chet(num_p // 10)


chet(int(input("Введите число: ")))

"""
Задание 3. Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
Не забудьте проверить на числе, которое оканчивается на 0.
1230 -> 0321
"""
re_num = ""


def flipper(num_re):
    global re_num
    if num_re == 0:
        return print(re_num)
    elif num_re > 0:
        re_num = str(re_num) + str(num_re % 10)
    flipper(int(num_re) // 10)


flipper(int(input("Введите число, которое требуется перевернуть: ")))

"""
Задание 4. Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""
s_ma = 1
na = 1


def fun_k_s(co__ter):
    global na, s_ma
    if co__ter - 1 == 0:
        return print(s_ma)
    else:
        na = na / -2
        s_ma = s_ma + na
        return fun_k_s(co__ter - 1)


fun_k_s(int(input("Введите количество элементов: ")))

"""
Задание 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
Пример:
32 - 33 - ! 34 - " 35 - # 36 - $ 37 - % 38 - & 39 - ' 40 - ( 41 - )
42 - * 43 - + 44 - , 45 - - 46 - . 47 - / 48 - 0 49 - 1 50 - 2 51 - 3
52 - 4 53 - 5 54 - 6 55 - 7 56 - 8 57 - 9 58 - : 59 - ; 60 - < 61 - =
62 - > 63 - ? 64 - @ 65 - A 66 - B 67 - C 68 - D 69 - E 70 - F 71 - G
72 - H 73 - I 74 - J 75 - K 76 - L 77 - M 78 - N 79 - O 80 - P 81 - Q
82 - R 83 - S 84 - T 85 - U 86 - V 87 - W 88 - X 89 - Y 90 - Z 91 - [
92 - \ 93 - ] 94 - ^ 95 - _ 96 - ` 97 - a 98 - b 99 - c 100 - d 101 - e
102 - f 103 - g 104 - h 105 - i 106 - j 107 - k 108 - l 109 - m 110 - n 111 - o
112 - p 113 - q 114 - r 115 - s 116 - t 117 - u 118 - v 119 - w 120 - x 121 - y
122 - z 123 - { 124 - | 125 - } 126 - ~ 127 - 
Решите через рекурсию. В задании нельзя применять циклы.
Допускается исп-е встроенных ф-ций
"""
asc_tab = ''


def asc(asc_num=32):
    global asc_tab
    if asc_num == 128:
        print(asc_tab)
        return
    else:
        asc_tab += " " + str(asc_num) + " - " + chr(asc_num)
    if (asc_num - 31) % 10 == 0 and asc_num != 32:
        asc_tab += '\n'
    return asc(asc_num + 1)


asc()

"""
Задание 6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""

# Никак не смог понять почему ошибку выводит, но код работает
import random

r_n = int(random.randint(1, 100))
print(r_n)


def rek(s=0):
    global r_n
    if s == 10 - 7:
        return print(f"Вы не угадали за 10 попыток, загадонное число было {r_n}")
    if s < 10 - 7:
        pop_ot = int(input(f"Отгадайте число у вас: {10 - s} попыт. :"))
        if pop_ot < r_n and pop_ot != r_n:
            print(f"Загаданное число больше: {pop_ot}")
        elif pop_ot > r_n and pop_ot != r_n:
            print(f"Загаданное число меньше: {pop_ot}")
        elif pop_ot == r_n:
            return print("Ура")
    return s + rek(s + 1)


rek()
"""
Задание 7. Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Пример:

1+2+3+4+5 = 5(5+1)/2
Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!
Решите через рекурсию. В задании нельзя применять циклы.
"""

import random

k = int(random.randint(0, 10))
d = 0


def rek_8(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return n + rek_8(n - 1)


rek_8(k)
o = k * (k + 1) / 2
if o == rek_8(k):
    print("Да")
else:
    print("No")


# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8
# i = 0

def rel_26(A, B):
    if A == 0:
        return 0
    elif B == 0:
        return 1
    elif B == 1:
        return A
    else:
        return A * rel_26(A, B - 1)


print(f'Ответ: {rel_26(int(input("Введите первое число: ")), int(input("Введите второе число: ")))}')

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#     4

def rek_28(a, b, ):
    if b == 0:
        return a
    else:
        return rek_28(a + 1, b - 1)
print(rek_28(2, 2))