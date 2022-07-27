import random

def shuffle_list_rand(lst: list) -> list: # функция перемешеивания random алгоритм
    for i in range(len(lst)-1):
        x = random.randint(0,len(lst)-1)
        lst[i],lst[x] = lst[x],lst[i]
    return lst

list_num = [1, 2, 3, 4, 5]
print('Initial list_num:              ',list_num)
list_num_2 = shuffle_list_rand(list_num)
print('Shuffle list_num random rule:  ',list_num_2)