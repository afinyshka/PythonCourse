# 1. Считать строку из файла. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

from encodings.utf_8 import StreamReader
import os
path = 'Seminar_4' + os.sep + '01_file.txt'
with open (path, 'r') as data:
    strring = data.read()
    print(strring)
    print(type(StreamReader))

def str_to_list (strr: str) -> list:
    listt = []
    listt = strr.split(' ')
    listt = [int(i) for i in listt]
    return listt

my_list = str_to_list(strring)

print(my_list)
print(min(my_list))
print(max(my_list))

# от Кирилла

# import os

# def convert_to_int(str):
#     return [int(x) for x in str.split()]

# path = os.path.join('folder', 'file.txt')


# with open(path, 'r') as writer:
#     text = writer.readline()

# int_list = convert_to_int(text)


# print(int_list)
# print(max(int_list))
# print(min(int_list))

# от Максима
# path = r'Testfiles/S4T1.txt'

# with open(path, 'r') as f:
#     data = f.readlines()

# data_split = data[0].split(' ')
# print(data_split)

# minn = int(data_split[0])
# maxx = int(data_split[0])

# for i in data_split:
#     if int(i) < minn:
#         minn = int(i)
#     if int(i) > maxx:
#         maxx = int(i)

# print(f'Минимальное число: {minn}')
# print(f'Максимальное число: {maxx}')

# от Питончик
# def is_int(str: str) -> bool:
#     try:
#         int(str)
#         return True
#     except ValueError:
#         return False


# def input_list_int_numbers(str_in: str) -> list:
#     list_dirty = str_in.split(' ')
#     list_clean = []
#     for elem in list_dirty:
#         if is_int(elem):
#             list_clean.append(int(elem))
#     return list_clean

# f = open('str_file', 'r')
# str_in = f.readline()
# f.close()

# numb_list = input_list_int_numbers(str_in)

# print(numb_list)
# print(max(numb_list))
# print(min(numb_list))
