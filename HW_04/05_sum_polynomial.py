# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import os


def get_k_from_equasion (equasion: str) -> list:
    equasion = equasion.replace(' x', ' 1*x')
    equasion = equasion.replace('*x ', '*x^1 ')
    if (equasion[0] == 'x'):
        equasion = '1*' + equasion
    k_list = equasion.split(' ')
    k_list = k_list[:-2]
    k_list_new = [(k_list[0])]
    k_list = [k_list[i] + k_list[i+1] for i in range(1, len(k_list) - 1, 2)]
    k_list_new = k_list_new + k_list
    len_k = int(k_list_new[0][-1]) + 1 # length of k list needed
    k = []
    if len(k_list_new) < 2:
        k_list_new.append('0')
    for i in range(len_k - 1):
        if (k_list_new[i][-2:]) != f'^{len_k - (i + 1)}':
            k_list_new.insert(i, f'0*x^{len_k - (i + 1)}')
    for i in k_list_new:
        k.append(i[:-4])
    if (len(k_list_new) == len_k):
        k.pop()
        k.append(k_list_new[-1])
    else:
        k.append(0)
    k = [int(i) for i in k]
    return k

def match_length (list_1: list, list_2: list) -> list:
    while len(list_1) < len(list_2):
        list_1.insert(0, 0)
    while len(list_2) < len(list_1):
        list_2.insert(0, 0)

def sum_k_list (list_1: list, list_2: list) -> list:
    return [x+y for x,y in zip(list_1,list_2)]

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


path_1 = 'HW_04' + os.sep + '04_polynomial_1.txt'
path_2 = 'HW_04' + os.sep + '04_polynomial_2.txt'

with open(path_1, 'r') as data_source:
    equasion_1 = data_source.readline()

with open(path_2, 'r') as data_source:
    equasion_2 = data_source.readline()

print(equasion_1)
print(equasion_2)

k_list_1 = get_k_from_equasion(equasion_1)
print('k list 1 = ', k_list_1)
k_list_2 = get_k_from_equasion(equasion_2)
print('k list 2 = ', k_list_2)

match_length(k_list_1, k_list_2)

print('k list 1_0 = ', k_list_1)
print('k list 2_0 = ', k_list_2)

sum_list = sum_k_list(k_list_1, k_list_2)
print('k sum  list = ', sum_list)
print(type(sum_list))

polinomial_sum = create_polynomial(sum_list)
print('Polynomial summa =',polinomial_sum)

path = 'HW_04' + os.sep + '05_polynomial_sum.txt'
with open (path, 'w') as file:
    file.write(polinomial_sum)