# Проверить является ли число квадратом другого

a = int(input('Enter a: '))
b = int(input('Enter b: '))
if a==b**2:
    print(f'{a} is a square of {b}')
elif b==a**2:
    print(f'{b} is a square of {a}')
else:
    print(f'{a} is NOT a square of {b}, {b} is NOT a square of {a}')