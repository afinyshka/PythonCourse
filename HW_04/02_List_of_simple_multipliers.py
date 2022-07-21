# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def list_iof_simple_multipliers (number: int) -> list:
    list_dev = []
    for i in range(2,number+1):
        if(number%i == 0):
            while number%i == 0:
                number /= i
                # print(number)
                list_dev.append(i)
    return list_dev

number = 786
print(f'List of less dividers for {number}: {list_iof_simple_multipliers(number)}')  

number_1 = 49
print(f'List of less dividers for  {number_1}: {list_iof_simple_multipliers(number_1)}')  