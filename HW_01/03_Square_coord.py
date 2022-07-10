# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print('Enter x and y coordinates, x ≠ 0 и y ≠ 0')

x = int(input('Enter x = '))
y = int(input('Enter y = '))

if x > 0 and y > 0:
    print(f'The point [{x}, {y}] belongs to 1-st coordinate square')
elif x < 0 and y > 0:
    print(f'The point [{x}, {y}] belongs to 2-nd coordinate square')
elif x < 0 and y < 0:
    print(f'The point [{x}, {y}] belongs to 3-rd coordinate square')
elif x > 0 and y < 0:
    print(f'The point [{x}, {y}] belongs to 4-th coordinate square')