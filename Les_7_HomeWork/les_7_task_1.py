import numpy as np


def bubble_sorting(array):
    n = 0
    while n < len(array):
        flag_sort = False
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                flag_sort = True
        n += 1
        if not flag_sort:
            break
    return array


arr = np.random.randint(-100, 100, 10)
print(arr)
print(bubble_sorting(arr))
