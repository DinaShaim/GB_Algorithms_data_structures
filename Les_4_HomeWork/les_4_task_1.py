# Проанализировать скорость и сложность одного любого алгоритма из разработанных
# в рамках домашнего задания первых трех уроков.

# Задание № 2  урока № 2:
# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

# 1 Вариант
import timeit
import cProfile

even = 0  # четный
odd = 0  # нечентый


def counting_recursion(x, even=even, odd=odd):
    if ((x % 10) % 2) == 0:
        even = even + 1
    else:
        odd = odd + 1
    if (x // 10) != 0:
        return counting_recursion(x // 10, even=even, odd=odd)
    return even, odd


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
    return even, odd


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
    return even, odd


A1 = 1e+3
A2 = 1e+7
A3 = 1e+15
A4 = 1e+31
A5 = 1e+63
A6 = 1e+127

print(timeit.timeit('counting_recursion(A1)', number=100, globals=globals()))  # 0.0009046000000000054
print(timeit.timeit('counting_recursion(A2)', number=100, globals=globals()))  # 0.0020120000000000138
print(timeit.timeit('counting_recursion(A3)', number=100, globals=globals()))  # 0.004119700000000004
print(timeit.timeit('counting_recursion(A4)', number=100, globals=globals()))  # 0.007559099999999985
print(timeit.timeit('counting_recursion(A5)', number=100, globals=globals()))  # 0.015897899999999993
print(timeit.timeit('counting_recursion(A6)', number=100, globals=globals()))  # 0.0371291
print()
print(timeit.timeit('counting_while(A1)', number=100, globals=globals()))  # 0.0005190999999999946
print(timeit.timeit('counting_while(A2)', number=100, globals=globals()))  # 0.0009889000000000148
print(timeit.timeit('counting_while(A3)', number=100, globals=globals()))  # 0.0019822999999999924
print(timeit.timeit('counting_while(A4)', number=100, globals=globals()))  # 0.004015200000000024
print(timeit.timeit('counting_while(A5)', number=100, globals=globals()))  # 0.009873900000000019
print(timeit.timeit('counting_while(A6)', number=100, globals=globals()))  # 0.018753200000000025
print()
print(timeit.timeit('counting_list(A1)', number=100, globals=globals()))  # 0.0010371999999999604
print(timeit.timeit('counting_list(A2)', number=100, globals=globals()))  # 0.001844300000000021
print(timeit.timeit('counting_list(A3)', number=100, globals=globals()))  # 0.0035182999999999742
print(timeit.timeit('counting_list(A4)', number=100, globals=globals()))  # 0.0069190000000000085
print(timeit.timeit('counting_list(A5)', number=100, globals=globals()))  # 0.015661900000000006
print(timeit.timeit('counting_list(A6)', number=100, globals=globals()))  # 0.035929199999999994

# Все разработанные алгоритмы имеют линейную вычислительную сложность:
# Вариант с рекурсией пораждает вызов одной рекурсивной фукнции, что соотвествует линейной сложности O(n)
# Решение с циклом while будет реализован n раз, т.е. получаем O(n)
# Третий вариант решения цикл while пробегает n раз и формирует массив,
# далее цикл for аналогично пробегает n раз. Тогда O(n+n) = O(n), т.е. тоже линейная вычислительная сложность.
# Проведенный анализ подтверждается полученными временными значениями функции timeit,
# где с увеличением n в 2 раза, время увеличивается тоже примерно в 2 раза.


print()
cProfile.run('counting_recursion(A1)')
# 7 function calls (4 primitive calls) in 0.000 seconds
#

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      4/1    0.000    0.000    0.000    0.000 les_4_task_1.py:13(counting_recursion)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('counting_recursion(A2)')
cProfile.run('counting_recursion(A3)')
cProfile.run('counting_recursion(A4)')
cProfile.run('counting_recursion(A5)')
cProfile.run('counting_recursion(A6)')

# 131 function calls (4 primitive calls) in 0.001 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#    128/1    0.000    0.000    0.000    0.000 les_4_task_1.py:13(counting_recursion)
#        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print()
cProfile.run('counting_while(A1)')
cProfile.run('counting_while(A2)')
cProfile.run('counting_while(A3)')
cProfile.run('counting_while(A4)')
cProfile.run('counting_while(A5)')
cProfile.run('counting_while(A6)')

# 4 function calls in 0.000 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 les_4_task_1.py:25(counting_while)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print()
cProfile.run('counting_list(A1)')
cProfile.run('counting_list(A2)')
cProfile.run('counting_list(A3)')
cProfile.run('counting_list(A4)')
cProfile.run('counting_list(A5)')
cProfile.run('counting_list(A6)')

# 132 function calls in 0.001 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 les_4_task_1.py:38(counting_list)
#        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      127    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Анализируя результаты, проведенного профилирования, можно отметить, что вызовы всех функций были выполнены
# за 0.000 секунд, что говорит об отсутствии слабых (медленных) мест.
# Необходимо отметить, что в первом и третьем методах решений количество вызовов функций
# растет прямопропорционально n, что требует большего времени выполнения методов.
# Во втором алгоритме всегда происходит вызов 4 функций, что делает этот
# метод решения самым быстрым (что подтверждается вычислительными значениями функции timeit)
# и неиболее оптимальным.
