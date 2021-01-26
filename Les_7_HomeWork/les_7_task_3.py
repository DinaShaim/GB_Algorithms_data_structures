import numpy as np
import random


def select_rnd(n, array):
    pivot = random.choice(array)

    lows = [item for item in array if item < pivot]
    if len(lows) > n:
        return select_rnd(n, lows)
    n -= len(lows)

    pivots = array.count(pivot)
    if pivots > n:
        return pivot
    n -= pivots

    highs = [item for item in array if item > pivot]
    return select_rnd(n, highs)


def median(items):
    if len(items) % 2:
        return select_rnd(len(items)//2, items)
    else:
        left = select_rnd((len(items)-1) // 2, items)
        right = select_rnd((len(items)+1) // 2, items)
        return (left + right) / 2


print('Введите натуральное число')
m = int(input('Число =  '))

arr = np.random.random(2*m+1).tolist()
print(arr)
print(median(arr))
