# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# numbers = int(input('Enter list of 5 numbers' [5]))

numbers = [3, 2, 4, 6, 13]
maxx = numbers[0]
for i in numbers:
    # i = int(i)
    print(type(i), end = ', ') # печать в строку <class 'int'>, <class 'int'>, <class 'int'>, <class 'int'>, <class 'int'>, 13
    if i > maxx:
        maxx = i
print(f'\nmax = {maxx}')        

# от препода

# a = []
# # range(5) -> [0, 1, 2, 3, 4]
# # range(5, 8) -> [5, 6, 7]
# # range(1, 11, 2) -> [1, 3, 5, 7, 9]
# for i in range(5):
#     x = int(input('-->'))
#     a.append(x)
# 4

# maxx = a[0]
# # len(a) - длина списка
# for i in range(1, len(a)):
#     if a[i] > maxx:
#         maxx = a[i]

# print(maxx)

# Решение со вводом строкой
numers = (input('Enter  numbers: '))
numers = numers.split(',')
numers = [int(i) for i in numers]

maxx1 = numers[0]
print('length = ', len(numers))
for i in range(1, len(numers)):
    print(numers[i])
    print(type(numers[i]), end=' ')
    if numers[i] > maxx1:
        maxx1 = numers[i]
        # print(f'max = {maxx1}')
print(f'max total = {maxx1}')
# 1, 4, 7, 3, 91