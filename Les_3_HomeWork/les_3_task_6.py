#В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_item = 0
max_index = 0
min_item = 100
min_index = 0
for i in range(len(array)):
    if array[i] > max_item:
        max_item = array[i]
        max_index = i
    if array[i] < min_item:
        min_item = array[i]
        min_index = i

print(f"Максимальный элемент: {max_item}")
print(f"Минимальный элемент: {min_item}")
summa = 0

if abs(max_index - min_index) <=1:
    print(f"Между максимальныи и минимальным элементами нет чисел")
elif min_index < max_index:
    print(f"Найти сумму элементов: {array[min_index + 1:max_index]}")
    for i in range(min_index+1, max_index):
        summa += array[i]
elif max_index < min_index:
    print(f"Найти сумму элементов: {array[max_index + 1:min_index]}")
    for i in range(max_index+1, min_index):
        summa += array[i]

print(f"Сумма элементов равна: {summa}")
