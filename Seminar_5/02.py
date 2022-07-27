# 1. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число

import os

path = 'Seminar_5' + os.sep + '02_file.txt'

with open(path, 'r') as data:
    list_1 = data.readline().split()
    list_1 = [int(i) for i in list_1]

print(list_1)

result = list(filter(lambda i: list_1[i] + 1 == list_1[i+1]), range(len(list_1)) - 1)

print(result)

# от Славы

# my_list = [1, 2, 4, 5, 6]

# f = lambda i: (my_list[i] - my_list[i - 1]) != 1
# x = tuple(filter(f, range(1, len(my_list))))
# print(x[0] + 1)

# def f(my_list: list):
#     for i in range(1, len(my_list)):
#         if my_list[i] - my_list[i - 1] != 1:
#             return my_list[i - 1] + 1
#     return 'Not found'