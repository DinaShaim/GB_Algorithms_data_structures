#Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

print('Введите целое трехзначное число')
x = int(input('Число =  '))

S = x % 10 + x // 10 % 10 + x // 100
P = (x % 10) * ((x // 10) % 10) * (x // 100)

print(f'Сумма чисел введенного числа = {S}')
print(f'Произведение чисел введенного числа = {P}')