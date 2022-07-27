list_1 = [1, 2, 3, 5, 8, 15]
list_2 = list([(i, (i**2)) for i in list_1 if i%2 == 0])
print(list_2)

# def select(f, col):
#     return [f(x) for x in col]

# def where (f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split() # получим набор строк

# res = select(int, data)
# res = where(lambda x: not x%2, res)
# res = select(lambda x: (x, x**2), res)
# print(res)

li = [x for x in range(1, 20)]
li = list(map(lambda x: x + 10, li))

print(li)