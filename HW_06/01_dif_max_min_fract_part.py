# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.
    
#     *Пример:*
    
#     - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def fraction_part_list2 (listt: list) -> list:
    return [round(i%1, 2) for i in listt if type(i) == float]

new_list = [1.1, 1.2, 3.1, 5, 10.01]
print('Initial list: ',new_list)
new_list_2 = fraction_part_list2(new_list)
print('Fractional parts list: ',new_list_2)
print('Difference between man and min fractional part =',max(new_list_2) - min(new_list_2))