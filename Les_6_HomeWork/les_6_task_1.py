# Проанализировать скорость и сложность одного любого алгоритма из разработанных
# в рамках домашнего задания первых трех уроков.

# Задание № 2  урока № 2:
# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

# 1 Вариант

import sys


even = 0  # четный
odd = 0  # нечентый


def counting_recursion(x, even=even, odd=odd):
    if ((x % 10) % 2) == 0:
        even = even + 1
    else:
        odd = odd + 1
    if (x // 10) != 0:
        return counting_recursion(x // 10, even=even, odd=odd)
    list_variables = dir()
    for i in range(len(list_variables)):
        list_variables[i] = locals()[list_variables[i]]
    size = getsize(list_variables)
    return size


# 2 Вариант

def counting_while(x, even=even, odd=odd):
    while True:
        if ((x % 10) % 2) == 0:
            even = even + 1
        else:
            odd = odd + 1
        x = x // 10
        if not x != 0:
            break
    list_variables = dir()
    for i in range(len(list_variables)):
        list_variables[i] = locals()[list_variables[i]]
    size = getsize(list_variables)
    return size


# 3 Вариант

def counting_list(x, even=even, odd=odd):
    array_numbers = [x % 10]
    while (x // 10) != 0:
        x = x // 10
        a = x % 10
        array_numbers.append(a)
    for j in range(len(array_numbers)):
        if array_numbers[j] % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
    list_variables = dir()
    for i in range(len(list_variables)):
        list_variables[i] = locals()[list_variables[i]]
    size = getsize(list_variables)
    return size


def getsize(list):
    size = 0
    for i in range(len(list)):
        size += sys.getsizeof(list[i])
    return size


print('Введите натуральное число')
x = int(input('Число =  '))

s1 = counting_recursion(x)
s2 = counting_while(x)
s3 = counting_list(x)
print(s1)
print(s2)
print(s3)

# Выводы:

# Введите натуральное число
# Число =  12345
# 84
# 80
# 236

# В первом и втором методе используется одинаковый набор переменных, однако во втором методе
# переменная x в конце выполнения кода всгда принимает нулевое значение,
# которое занимает на 4 байта меньше памяти. Это означает что при любых исходных данных второй метод
# будет занимать на 4 байта меньше памяти
# В третьем методе кроме переменных, используемых в первых методах, создаются дополнительные переменные:
# a, j, array_numbers. Список array_numbers занимает на порядок больше памяти и кроме того,
# изменяется в зависимости от длины введенного числа. Следовательно, чем болешее число мы вводим, тем
# больше памяти будет выделяться для реализации третьего метода, в отличие от первых двух методов:

# Введите натуральное число
# Число =  123456789
# 84
# 80
# 268

# Так же можно отметить, что если какая-либо переменная будет принимать нулевое значение, то
# памяти будет выделяться меньше на 4 байта:

# Введите натуральное число
# Число =  11111
# 80
# 76
# 232

# В данном примере количество четных переменных равно 0.
