# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#  Пример:
#  - 6 -> да
#  - 7 -> да
#  - 1 -> нет

day_number = int(input('Enter a number of the day (from 1 to 7): '))

if day_number == 1 or day_number == 2 or day_number == 3 or day_number == 4 or day_number == 5:
    print('The day is NOT the weekend!')
elif day_number == 6 or day_number == 7:
    print('The day is the WEEKEND!!!')
else:
    print('The day is out of range')