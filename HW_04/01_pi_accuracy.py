# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math
from math import pi

def get_n_round (number: float) -> int:
    number = str(number)
    num_digits =len(number[2:len(number)])
    return num_digits

def pi_find (number_i: int) -> float: # формула Бэйли — Боруэйна — Плаффа
    my_pi = 0
    for i in range(number_i):
        my_pi += 1/16 ** i * (4/(8 * i + 1) - 2/(8 * i + 4) - 1/(8 * i + 5) - 1/(8 * i + 6))
    return my_pi    

d = input('Enter the accuracy of the number = ')
d = str(d)
accuracy_number = get_n_round(d)
print('Number of digits after comma = ', accuracy_number)


number_iterations = 100
my_pi = pi_find(number_iterations)
math_pi = float(pi)
print('pi from import math = ',math_pi)
print('my pi =               ',round(my_pi,accuracy_number))
