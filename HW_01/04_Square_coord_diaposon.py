# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)

quarter_num = int(input('Enter number of a qurter from 1 to 4: '))

if quarter_num == 1:
    print('The 1-st square diaposon: x > 0; y > 0')
elif quarter_num == 2:
    print('The 2-nd square diaposon: x < 0; y > 0')
elif quarter_num == 3:
    print('The 3-rd square diaposon: x < 0; y < 0')
elif quarter_num == 4:
    print('The 4-th square diaposon: x > 0; y < 0')
else:
    print('The value is out of quarter numbers range')