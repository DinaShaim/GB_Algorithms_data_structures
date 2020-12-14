#Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
#array.insert(SIZE, array[5]) # дополнительная запись повторяющегося элемента
print(array)

item = [array[0]]
count = [0]
item_count = dict(zip(item, count))

for i in range(len(array)):
    if array[i] in item_count.keys():
        item_count[array[i]] += 1
    else:
        item_count[array[i]] = 1
print(item_count)
max_count = 0
max_item = 0
for item, count in item_count.items():
    if count > max_count:
        max_count = count
        max_item = item

if max_count == 1:
    print(f"Все числа встречаются по одному разу.")
else:
    print(f"Чаще всего встречается чило: {max_item}")
