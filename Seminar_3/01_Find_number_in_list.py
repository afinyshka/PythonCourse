# list() - список: изменяемый, индексируемый
# tuple() - кортеж: неизменяемый, индексируемый
# set() - множество: изменяемый, неиндексируемый
# dict() - словарь: изменяемый, индексируемый по ключу

# 1. Задайте список. Напишите программу, которая определит, присутствует
# ли в заданном списке строк некое число.

def find_text(text_from, text_what):
    count = 0
    for i in text_from:
        if text_what in i:
            count += 1
    return count

org_text = ["qwe", "asgfd", "zxc", "3", "13ertqwe", "2", "3gf", "8"]
text_num = 3
text_num = str(text_num)
print(f'Text {text_num} is found in {org_text} {find_text(org_text, text_num)}-times')

# # от Кирилл

# str_list = ['12asd36', '256', 'dsds89358', '5698a']

# s_nym = input('Enter the number: ')
# is_Found = False

# for item in str_list:
#     print(item)
#     if item.__contains__(s_nym):
#         is_Found = True
#         break

# print(is_Found)

# # от Стоун

# 1. Задайте список. Напишите программу, которая определит, присутствует
# ли в заданном списке строк некое число.

exit()
list = ['123', '321', '456', '96']
count = '3'
array_find = []

for find_count in list:
    if count in find_count:
        array_find.append(find_count)
print(array_find)



