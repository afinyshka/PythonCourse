# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
    
#     1) с помощью математических формул нахождения корней квадратного уравнения
#     2) с помощью дополнительных библиотек Python 1 12 7 koef

import os
from re import A
path = 'Seminar_4' + os.sep + '02_file_coeficient.txt'
with open (path, 'r') as data:
    a = int(data.readline())
    b = int(data.readline())
    c = int(data.readline())
    print(a)
    print(b)
    print(c)

discriminant = b**2 - 4 * a * c
print(discriminant)
x_1 = -b + (discriminant ** 0.5) / (2 * a)
x_2 = -b - (discriminant ** 0.5) / (2 * a)
print(f'x_1 = {x_1}')
print(f'x_2 = {x_2}')

with open (path, 'a') as data:
    data.write(f'\nКорень_1: {x_1}')
    data.write(f'\nКорень_2: {x_2}')



# path = 'folder/file.txt'
# with open(path, 'r') as my_file:
#     data = my_file.read()

# data = data.split()
# print(data)
# data = data[:-2]
# print(data)
# data = [int(data[0][:-3]), int((data[1] + data[2])[:-1]), int(data[3] + data[4])]
# print(data)
# # D=b^2-4ac
# d = data[1]**2 - 4 * data[0] * data[2]
# print(d)
# # x=((-b(+-))(d^(1/2)))/(2*a))
# x_1 = (-data[1] + d**0.5) / (2 * data[0])
# x_2 = (-data[1] - d**0.5) / (2 * data[0])
# print(x_1, x_2)