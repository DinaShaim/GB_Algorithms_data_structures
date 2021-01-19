import numpy as np


def merge(right: list, left: list, result: list):
    if left[0] < right[0]:
        a = left.pop(0)
    else:
        a = right.pop(0)
    result.append(a)
    while len(left) > 0 and len(right) > 0:
        merge(right, left, result)
    else:
        return result + left + right


def merge_sort(array: list):
    if len(array) == 1:
        return array
    return merge(merge_sort(array[len(array) // 2:]),
                 merge_sort(array[:len(array) // 2]), [])


arr = np.random.uniform(0, 50, 5).tolist()
print(arr)
print(merge_sort(arr))


