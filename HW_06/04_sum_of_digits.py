# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#     *Пример:*   
#     - 6782 -> 23
#     - 0,56 -> 11

def sum_of_index2(text_number: str) -> int:  
    text_number = str(text_number)
    return sum([int(text_number[i]) for i in range(len(text_number)) if (text_number[i].isdigit())])

number = 129.4851
print(number)
print(f'Number = {number}. The summa of text digits = {sum_of_index2(number)}')



