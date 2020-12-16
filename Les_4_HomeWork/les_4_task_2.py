# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать
# соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
#
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.

# 1 Вариант: Решето Эратосфена

import math
import timeit
import cProfile
HOLE = None
MULTIP = 1000

def eratosthenes(i):
    n = i * MULTIP
    count = 0
    all_lst = [i for i in range(n)]
    for k in range(2, int(math.sqrt(n))):
        if k in all_lst:
            for j in range(k * 2, n, k):
                all_lst[j] = HOLE  # циклично делаю "дырки" в полном списке на месте чисел, кратных k
            count += 1  # счетчик простых чисел
        if count == i:
            return k


#i = int(input("Введите какое по счету простое число нужно найти:"))
#print(eratosthenes(i))


# 2 Вариант: поиск простых чисел через делители

def prime_divisors(i):
    n = i * MULTIP
    counter = 0
    all_lst = [i for i in range(n)]
    list_prime = []
    for k in range(2, int(math.sqrt(n))):
        for j in list_prime:
            if k % j == 0:
                break
        else:
            list_prime.append(k)
            counter += 1
        if counter == i:
            return list_prime[counter - 1]


#print(prime_divisors(i))

A1 = 2
A2 = 4
A3 = 8
A4 = 16
A5 = 32

print(timeit.timeit('eratosthenes(A1)', number=100, globals=globals()))  # 0.052629700000000015
print(timeit.timeit('eratosthenes(A2)', number=100, globals=globals()))  # 0.13260000000000002
print(timeit.timeit('eratosthenes(A3)', number=100, globals=globals()))  # 0.5782211
print(timeit.timeit('eratosthenes(A4)', number=100, globals=globals()))  # 2.9454454
print(timeit.timeit('eratosthenes(A5)', number=100, globals=globals()))  # 14.057624500000001
print()
print(timeit.timeit('prime_divisors(A1)', number=100, globals=globals()))  # 0.015501199999999216
print(timeit.timeit('prime_divisors(A2)', number=100, globals=globals()))  # 0.03051129999999702
print(timeit.timeit('prime_divisors(A3)', number=100, globals=globals()))  # 0.0705853999999988
print(timeit.timeit('prime_divisors(A4)', number=100, globals=globals()))  # 0.14598020000000034
print(timeit.timeit('prime_divisors(A5)', number=100, globals=globals()))  # 0.31504520000000014
print()

# Анализируя полученные данные и алрогитмы разработыанных методов, можно сделать следующий вывод:
# В методе решета Эратосфена есть вложенный цикл,  первый пробегает от начала до конца всего формируемого
# массива чисел, а второй уменьшает размер входных данных на каждом шаге. Поэтому алгоритм
# имеет вычислительную сложность O(n*log(n)), что согласуется с полученными значениями функции timeit.
# Во втором методе, аналогично есть два вложенных цикла, однако второй цикл пробегается по массиву простых чисел,
# который формируется в ходе выполнения программы. Таким образом, вычислительная сложность алгоритма
# авно O(n), что подтверждается полученными значениями функции timeit.


cProfile.run('eratosthenes(A1)')
# 6 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:20(eratosthenes)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:23(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('eratosthenes(A2)')
cProfile.run('eratosthenes(A3)')
cProfile.run('eratosthenes(A4)')
cProfile.run('eratosthenes(A5)')
# 6 function calls in 0.146 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.146    0.146 <string>:1(<module>)
#         1    0.143    0.143    0.145    0.145 les_4_task_2.py:20(eratosthenes)
#         1    0.002    0.002    0.002    0.002 les_4_task_2.py:23(<listcomp>)
#         1    0.000    0.000    0.146    0.146 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
print()
cProfile.run('prime_divisors(A1)')
# 7 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:39(prime_divisors)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:42(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('prime_divisors(A2)')
cProfile.run('prime_divisors(A3)')
cProfile.run('prime_divisors(A4)')
cProfile.run('prime_divisors(A5)')
# 37 function calls in 0.003 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.003    0.003 <string>:1(<module>)
#         1    0.000    0.000    0.002    0.002 les_4_task_2.py:39(prime_divisors)
#         1    0.002    0.002    0.002    0.002 les_4_task_2.py:42(<listcomp>)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#        32    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Анализируя подученный данные функции cProfile можно отметить, что в методе
# решета Эратосфена с ростом числа n увеличивается время выполнения программы.
# Наибольший рост времени происходит в самой функции eratosthenes, что связано
# с идеей самого метода (чем большее простое число мы будем искать, тем больший
# массив чисел all_lst будет формироваться, и будет требоваться болшее время для
# прохождения по нему циклически, учитывая вычислительную сложность O(n*log(n))).
# Во втором методе время выполнения программы расстет незначительно, что  говорит
# об отсутствии слабых (медленных) мест.
