# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции вводит пользователь через пробел.

import random

def list_from_N_to_N(number_N: int, begin_finish_num: int) -> list:
    list = []
    for i in range(1, number_N+1):
        list.append(random.randint(-begin_finish_num, begin_finish_num))
    return list  

def product_of_list_elem(list: list, i_1: int, i_2: int) -> int:
    product = list[i_1] * list[i_2]
    return product

elems_num = int(input('Enter the number of elemens in the list: '))
begin_finish_num = int(input('Enter the number of [-N, N]-diaposone: '))
list_1 = list_from_N_to_N(elems_num, begin_finish_num)

print('List: ', list_1)


index_1 = int(input(f'Enter the 1-st index from 0 to {len(list_1)-1} = '))
index_2 = int(input(f'Enter the 2-nd index from 0 to {len(list_1)-1} = '))

print(f'Product of {index_1}-index element and {index_2}-index element = {product_of_list_elem(list_1, index_1, index_2)}')
    