# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем 
# первый и последний элемент, второй и предпоследний и т.д.
    
#     *Пример:*
    
#     - [2, 3, 4, 5, 6] => [12, 15, 16];
#     - [2, 3, 5, 6] => [12, 15]
    
def list_from_keypad() -> list:
    listt = input('Enter the integer list: ').split(' ')
    print(listt)
    listt = [int(i) for i in listt]
    return listt

def product_of_i_pairs(listt: list) -> list:
    list_f = []
    for i in range(int((len(listt)/2)*-1//1*-1)): # округление в большую сторону
        list_f.append(listt[i]*listt[len(listt)-(i+1)])
    return list_f


list_t = list_from_keypad()
print(list_t)
 
print('Products of lists\' elements: ',product_of_i_pairs(list_t))