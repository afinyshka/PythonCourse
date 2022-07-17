# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.    
#     *Пример:*    
#     - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci_negative (n: int) -> list:
    listt = [0, 1]
    for i in range(2,n+1):
        listt.append(listt[i-1] + listt[i-2])
    for i in range(n):
        listt.insert(0, (listt[1] - listt[0]))
    return listt

item_number = int(input('Enter number of Fibonacci elements in both: negative and positive direction: '))
my_list = fibonacci_negative(item_number)
print(f'Fibonacci list: {my_list} for {item_number} elements')
