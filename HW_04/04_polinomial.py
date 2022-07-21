# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
import os

def create_k_list (number_of_max_power: int) -> str:
    return [random.randint(-100, 100) for i in range(number_of_max_power + 1)]

def create_polynomial (k_list: list) -> str:
    str_polynomial = ' = 0'
    for i in range(len(k_list)):
        if (not k_list[len(k_list)-(i+1)] == 0):
            if i == 0:
                str_polynomial = f'{k_list[len(k_list)-(i+1)]}' + str_polynomial
            elif i == 1:
                str_polynomial = f'{k_list[len(k_list)-(i+1)]}*x + ' + str_polynomial
            else:
                str_polynomial = f'{k_list[len(k_list)-(i+1)]}*x^{i} + ' + str_polynomial
    str_polynomial = str_polynomial.replace(' 1*x', ' x')
    str_polynomial = str_polynomial.replace('+  = 0', '= 0')
    str_polynomial = str_polynomial.replace('+ -', '- ')
    str_polynomial = str_polynomial.replace('- 1*x', '- x')
    if (str_polynomial[0:3] == '1*x'):
        str_polynomial = str_polynomial[2:]
    if (str_polynomial[0:4] == '-1*x'):
        str_polynomial = '-' + str_polynomial[3:]
    return str_polynomial


k_list_1 = create_k_list(3)
equasion_1 = create_polynomial(k_list_1)
k_list_2 = create_k_list(4)
equasion_2 = create_polynomial(k_list_2)

print(k_list_1)
print('equasion 1 =', equasion_1)
print(k_list_2)
print('equasion 2 =', equasion_2)

path = 'HW_04' + os.sep + '04_polynomial_1.txt'
with open (path, 'w') as file:
    file.write(equasion_1)

path = 'HW_04' + os.sep + '04_polynomial_2.txt'
with open (path, 'w') as file:
    file.write(equasion_2)
