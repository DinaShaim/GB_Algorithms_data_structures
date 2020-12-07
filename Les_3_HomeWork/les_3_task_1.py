#В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

number_multiple = [0] * 8

for i in range(2, 100):
    for j in range(2, 10):
        if (i%j == 0):
            number_multiple[j - 2] += 1

for j in range(2, 10):
    print(f"Числу {j} из заданного диапазона кратно {number_multiple[j-2]} чисел.")
