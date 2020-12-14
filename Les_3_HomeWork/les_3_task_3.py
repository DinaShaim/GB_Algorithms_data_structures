#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

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
array[min_index], array[max_index] = array[max_index], array[min_index]
print(f"Новый массив: {array}")
