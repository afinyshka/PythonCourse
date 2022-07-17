# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.
    
#     *Пример:*
    
#     - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def list_float_from_keypad() -> list:
    listt = input('Enter the real numbers list: ').split(' ')
    listt = [float(i) for i in listt]
    return listt

def fraction_part_list (listt: list) -> list:
    listt_2 = []
    for i in range(len(listt)):
        listt_2.append(round(listt[i]%1, 2))
    return listt_2

def find_max (listt: list) -> float:
    maxx = listt[0]
    for i in listt:
        if i > maxx: maxx = i
    return maxx

def find_min(listt: list) -> float:
    minn = listt[0]
    for i in listt:
        if i < minn: minn = i
    return minn

def find_difference (number_1: float, number_2: float) -> float:
    return [number_1 - number_2]

new_list = list_float_from_keypad()
print('Initial list: ',new_list)
new_list_2 = fraction_part_list(new_list)
print('Fractional parts list: ',new_list_2)
difference = find_max(new_list_2) - find_min(new_list_2)
print(f'The difference between max and min fractional parts in the list is = {difference}')