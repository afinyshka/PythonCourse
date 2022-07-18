# 3. Найти наименьшее общее кратное у двух чисел

from math import lcm


number_1 = 27
number_2 = 45

def list_int_deviders (number: int) -> list:
    list_dev = []
    for i in range(2,number+1):
        if(number%i == 0):
            while number%i == 0:
                number /= i
                # print(number)
                list_dev.append(i)
    return list_dev

def list_del_the_same(listt_1: list, listt_2: list) -> list:
    for i in listt_1:
        for j in listt_2:
            if i == j:
                listt_2.remove(i)
                print(listt_2)
                break
    return(listt_2)

def product_of_lists(listt_1: list, listt_2: list) -> list:
    product = 1
    for i in listt_1:
        product *= i
    for i in listt_2:
        product *= i
    return product


list_div_1 = list_int_deviders(number_1)
print('list_1 = ',list_div_1)

list_div_2 = list_int_deviders(number_2)
print('list_2 = ',list_div_2)

list_div_2 = list_del_the_same(list_div_1, list_div_2)
print('list_2.1 = ',list_div_2)

my_lcm = product_of_lists(list_div_1, list_div_2)
print('lcm = ', my_lcm)

pr = lcm(45, 27)
print(pr)