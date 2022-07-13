# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#     *Пример:*   
#     - 6782 -> 23
#     - 0,56 -> 11

from distutils import text_file


def sum_of_digits(number: float) -> int:
    sum = 0
    print(type(number))
    print(number)
    while (number*10%10 !=0):
        number *= 10
    # while number%1 > 0:
    #     number *= 10
        print(number)
    while number > 0:
        sum += number%10
        number = number//10
    return sum

print('sum of digits = ', sum_of_digits(1294.851))

def sum_of_index1(text_number: str) -> int:
    text_number = str(text_number)
    sum = 0
    for i in range(len(text_number)):
        if (text_number[i].isdigit()):
            sum += int(text_number[i])
    return sum    

print('sum of text digits = ', sum_of_index1(129.4851))

def sum_of_index2(text_number: str) -> int:  
    list = []
    sum = 0
    text_number = str(text_number)
    for i in range(len(text_number)):
        if (text_number[i].isdigit()):
            list.append(text_number[i])
        # if (text_number[i] != '.'):
        #     list.append(text_number[i])
    print(list)
    for i in list:
        # i = int(i)
        sum += int(i)
    return sum    

print('sum of text digits = ', sum_of_index2(129.4851))



