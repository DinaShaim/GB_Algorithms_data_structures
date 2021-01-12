# Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и
# отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import Counter

print('Введите количество предприятий:')
n = int(input())
i = 0
company_array = [0]*n
total_profit = 0
for i in range(len(company_array)):
    print('Введите название предприятия:')
    company_name = input()
    print('Введите последовательно прибыль за 4 квартала данного предприятия:')
    qrt1 = input()
    qrt2 = input()
    qrt3 = input()
    qrt4 = input()
    summa_profit = int(qrt1) + int(qrt2) + int(qrt3) + int(qrt4)
    company_array[i] = Counter(name=company_name, quarter_1=qrt1, quarter_2=qrt2, quarter_3=qrt3,
                               quarter_4=qrt4, profit=summa_profit)
    total_profit += company_array[i]['profit']
average_profit = total_profit/n
print(f"Средняя прибыль за год для всех предприятий = {average_profit}.")
print()
print('Предприятия, чья прибыль выше средней:')
for i in range(len(company_array)):
    if float(company_array[i]['profit']) > average_profit:
        print(f"Предприятие {company_array[i]['name']} с прибылью {company_array[i]['profit']}.")

print()
print('Предприятия, чья прибыль ниже средней:')
for i in range(len(company_array)):
    if float(company_array[i]['profit']) < average_profit:
        print(f"Предприятие {company_array[i]['name']} с прибылью {company_array[i]['profit']}.")
