# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт 
# сумму элементов списка, стоящих на нечётной позиции.
#     *Пример:*  
#     - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def create_list (number_elem: int) -> list:
    return [input(f'Enter integer meaning of the {i+1} element = ') for i in range(number_elem)]

def sum_even_position (list_list: list):
    sum = 0
    for i in range(1,len(list_list),2):
        sum += int(list_list[i])
    return sum


list_num = create_list(8)
print(list_num)
print('Summa of even elements equals = ', sum_even_position(list_num))
    
