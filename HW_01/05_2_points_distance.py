# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# print ('Enter points coordinates in the format: [x, y]')
# point_a = input('Enter 1-st point coordinates: ')
# # point_b = input('Enter 2-nd point coordinates: ')
# point_a = point_a.split(', ')
# print(point_a)
# x_1 = point_a[0]
# x_1 = x_1[1:len(x_1)]
# y_1 = point_a[1]
# y_1 = y_1[0:len(y_1)-1]
# print(x_1)
# print(y_1)

from cmath import sqrt


print ('Enter points coordinates in the format: x, y')

point_a = input('Enter 1-st point coordinates: ')
point_b = input('Enter 2-nd point coordinates: ')
point_a = point_a.split(',')
point_b = point_b.split(',')

print(point_a)
print(point_b)

x_1 = float(point_a[0])
y_1 = float(point_a[1])
x_2 = float(point_b[0])
y_2 = float(point_b[1])

distance = round((((x_1 - x_2)**2 + (y_1 - y_2)**2)**0.5),2)
# distance = round((sqrt((x_1 - x_2)**2 + (y_1 - y_2)**2)),2)

print(f'distance = {distance}')