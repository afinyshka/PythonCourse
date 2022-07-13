# 3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
#     *Пример:* 
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def sequence_num(number: int) -> list:
    list = []
    for i in range(1, number+1):
        list.append(round((1 + 1/i)**i, 3))
    return list

def sum(list: list) -> float:
    sum = 0
    for i in list:
        sum += i
    return sum

print(sequence_num(4))
print(f'Summa of elements = {sum(sequence_num(4))}')
