# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque
from collections import Counter

numbers_hexadecimal = Counter({'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                               '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15})
numbers_hexadecimal_back = Counter({0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
                                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'})

print('Введите первое шестнадцатеричное чисело:')
first_number = deque(input())
print('Введите второе шестнадцатеричное чисело:')
second_number = deque(input())
if len(first_number) < len(second_number):
    first_number, second_number = second_number, first_number


def adding_numbers(first_number, second_number):
    result = deque()
    dozen = 0
    first_nmb = first_number.copy()
    second_nmb = second_number.copy()

    while len(first_nmb) > 0:
        x1 = first_nmb.pop()
        x1 = numbers_hexadecimal[x1]
        if dozen > 0:
            x1 += dozen
        if len(second_nmb) > 0:
            x2 = second_nmb.pop()
            x2 = numbers_hexadecimal[x2]
        else:
            x2 = 0
        summa = x1 + x2
        units = 0
        dozen = 0
        if summa > 15:
            units = summa % 16
            dozen = summa // 16
        else:
            units = summa
        units = numbers_hexadecimal_back[units]
        result.appendleft(units)
    if dozen > 0:
        dozen = numbers_hexadecimal_back[dozen]
        result.appendleft(dozen)
    return result


print(f"Результат сложения в шестнадцатеричной системе: {adding_numbers(first_number, second_number)}")


def multiplication_numbers(first_number, second_number):
    second_nmb = second_number.copy()
    dozen = 0
    arr_res = [0] * len(second_nmb) * len(first_number)
    res_0 = deque()
    for i in range(len(second_nmb)):
        x2 = second_nmb.pop()
        x2 = numbers_hexadecimal[x2]
        first_nmb = first_number.copy()
        result = deque()
        units = 0
        dozen = 0
        while len(first_nmb) > 0:
            x1 = first_nmb.pop()
            x1 = numbers_hexadecimal[x1]
            multp = x1 * x2
            if int(dozen) > 0:
                multp = multp + int(dozen)
            units = 0
            dozen = 0
            if multp > 15:
                units = multp % 16
                dozen = multp // 16
            else:
                units = multp
            units = numbers_hexadecimal_back[units]
            result.appendleft(units)
        if int(dozen) > 0:
            dozen = numbers_hexadecimal_back[int(dozen)]
            result.appendleft(dozen)
        for j in range(i):
            result.append('0')
        arr_res[i] = result
    for j in range(len(second_number) - 1):
        arr_res[j + 1] = adding_numbers(arr_res[j + 1], arr_res[j])
    return arr_res[j + 1]


print(f"Результат умножения в шестнадцатеричной системе: {multiplication_numbers(first_number, second_number)}")
