# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

even = 0
odd = 0

def counting(x, even = even, odd = odd):
    if ((x % 10) % 2) == 0:
        even = even + 1
    else:
        odd = odd +1
    if (x // 10) != 0:
        return counting(x//10, even=even, odd=odd)
    return even, odd


print('Введите натуральное число')
x = int(input('Число =  '))
even, odd = counting(x)
print(f"Четных цифр - {even}. Нечетных цифр -  {odd}.")
