# 2. Напишите программу, которая будет принимать на вход дробь
# и показывать первую цифру дробной части числа.
    
#     *Примеры:*
    
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

x = input('x = ')

for i in range(len(x)):
    if x[i] == ',' or x[i] == '.':
        print(x[i + 1])
        break

n = float(input('enter number: '))
m = int(n*10)
print(m%10)

str_1 = '6,78'
print(str_1.split(','))