# 5. Реализуйте алгоритм перемешивания списка.

import random

def list_from_N_to_N_random(number_N: int, begin_finish_num: int) -> list:
    list = []
    for i in range(1, number_N+1):
        list.append(random.randint(-begin_finish_num, begin_finish_num))
    return list

def list_from_left_to_right_random(number_N: int, left_num: int, right_num: int) -> list:
    return [random.randint(left_num, right_num) for i in range(number_N)]

def shuffle_list(list: list) -> list: # функция перемешеивания i = i + 1
    for i in range(len(list)-1):
        tmp = list[i]
        list[i] = list [i+1]
        list [i+1] = tmp
    return list

def shuffle_list_rand(list: list) -> list: # функция перемешеивания random алгоритм
    for i in range(len(list)-1):
        x = random.randint(0,len(list)-1)
        tmp = list[i]
        list[i] = list [x]
        list [x] = tmp
    return list

def shuffle_list_inner(list: list) -> list: # встроенная функция перемешеивания
    return random.shuffle(list)


list_rand = list_from_N_to_N_random (8, 99)
print('Initial list_rand:              ', list_rand)
list_rand_1 = shuffle_list(list_rand)
print('Shuffle list_rand i = i+1 rule: ',list_rand_1)
list_rand_2 = shuffle_list_rand(list_rand)
print('Shuffle list_rand random rule:  ',list_rand_2)

print('\n')
list_num = [1, 2, 3, 4, 5]
print('Initial list_num:              ',list_num)
list_num_1 = shuffle_list(list_num)
print('Shuffle list_num i = i+1 rule: ',list_num_1)
list_num_2 = shuffle_list_rand(list_num)
print('Shuffle list_num random rule:  ',list_num_2)

print('\n')
list_keypad = input('Enter the list: ').split(' ')
print('Initial list 2:                ', list_keypad)
list_keypad = [int(i) for i in list_keypad]
# print(type(list_keypad))
# print(type(list_keypad[0]))

print('\n')
print('Initial list_keypad:              ',list_keypad)
print('Shuffle list_keypad i = i+1 rule: ',shuffle_list(list_keypad))
print('Shuffle list_keypad random rule:  ',shuffle_list_rand(list_keypad))

list_numerable = [11, 22, 333, 4444, 55555]
print('\n')
print('Initial list_numerable:                ',list_numerable)
shuffle_list_inner(list_numerable)
print('Shuffle list_numerable inner shuffle:  ',list_numerable)

listik = list_from_left_to_right_random(10, 0, 50)
print('\nListik: ',listik)