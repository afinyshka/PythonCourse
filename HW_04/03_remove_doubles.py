# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# [7, 1, 4, 4, 5, 1, 6, 4, 7]  ->  [5, 6]

def creat_list_no_doubles (listt: list) -> list: # удаляет все повторяющиеся элементы
    return [i for i in listt if listt.count(i)<2]

list_1 = [7, 1, 4, 4, 5, 1, 6, 4, 7]
list_original = creat_list_no_doubles(list_1)

print('list_start = ',list_1)
print('list_original = ',list_original)

list_2 = [2, 1, 4, 3, 5, 1, 6, 4, 7]
list_original_2 = creat_list_no_doubles(list_2)

print('list_start = ',list_2)
print('list_original = ',list_original_2)