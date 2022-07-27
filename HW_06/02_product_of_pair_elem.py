# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем 
# первый и последний элемент, второй и предпоследний и т.д.
    
#     *Пример:*
    
#     - [2, 3, 4, 5, 6] => [12, 15, 16];
#     - [2, 3, 5, 6] => [12, 15]
    
def list_from_keypad() -> list:
    listt = input('Enter the integer list: ').split(' ')
    return [int(i) for i in listt]

def product_of_i_pairs(listt: list) -> list:
    return [listt[i] * listt[-i-1] for i in range((len(listt) + 1) // 2)]

list_t = list_from_keypad()
print(list_t)
 
print('Products of lists\' elements: ',product_of_i_pairs(list_t))