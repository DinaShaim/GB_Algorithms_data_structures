# Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных
# подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.

import hashlib


def search_substrings(input_string):
    list_hash = []
    for i in range(len(input_string) - 1):
        for j in range(len(input_string) - i):
            substrings = input_string[j:i + j + 1]
            hash_substrings = hashlib.sha256(substrings.encode('utf-8')).hexdigest()
            if hash_substrings not in list_hash:
                list_hash.append(hash_substrings)
    print(len(list_hash))


print('Введите строку')
x = input()
search_substrings(x)
