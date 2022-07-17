# 2. Напишите программу, которая определит позицию второго вхождения строки 
# в списке либо сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

def find_second_entry (text_list: list, text_str: str):
    count = 0
    for i in range(len(text_list)):
        if (text_str == text_list[i]):
            count += 1
            # print (i , count)
            if (count > 1):
                return(f'The position of the secont entry is {i+1}')
    if count == 0: 
        return('No second entry')



list_1 = ["787", "qwe", "asd", "zxc", "qwe", "ertqwe"]
text_find = 'qwe'
print(find_second_entry(list_1, text_find))

# find_second_entry(list_1, text_find)

# chec = 0

# for index in range(len(list2)):
#     if count2 == list2[index]:
#         chec += 1
#         if chec > 1:
#             print(f'второе вхождение: {index}')
#             break
# else:
#     print('нет таких')