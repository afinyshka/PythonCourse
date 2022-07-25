# [1, 1, 2] -> [2]

listt = [1, 1, 2, 3, 4, 4, 5, 6, 5, 7]
list1 = [i for i in listt if listt.count(i)<2]
print(list1)


# от Студентов

in_list = [1, 0, 2, 3, 0, 4, 5, 6, 5, 7]

print(list(filter(lambda x: in_list.count(x) == 1, in_list)))