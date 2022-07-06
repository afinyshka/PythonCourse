print('lecture')

# print('Введите а');
# a = input()
# print('Введите b');
# b = input()
# print(a, b)
# print('{} -- {}'.format(a, b))

# a = int(input('Введите \nа: '))
# b = int(input('Введите \nb: '))
# c=a+b
# print('{} + {} = {}'.format(a, b, c))

# a = int(input('Введите а: '))
# b = int(input('Введите b: '))
# c = 33
# print('{} + {} = {}'.format(a, b, c)) # 11 + 22 = 33

# Приоритет операций
# **, +N, -N, *, /, //, %, + , -

exp1=2**3-10%5+2*3
exp2=2**3-10/5+2*3
print(exp1) # 14
print(exp2) # 12

iter = 2
iter += 3 # iter = iter + 3
iter -= 4 # iter = iter - 4
iter *= 5 # iter = iter * 5
iter /= 5 # iter = iter / 5
iter //= 5 # iter = iter // 5 
iter %= 5 # iter = iter % 5
iter **= 5 # iter = iter ** 5

a, b ,c = 1, 2, 3
# a: 1 b: 2 c: 3
print('a: {} b: {} c: {}'.format(a, b, c))

range(*(1,5,2))

# username = input('Введите имя: ')
# if(username == 'Маша'):
#     print('Ура, это же МАША!');
# else:
#     print('Привет, ', username);

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет, ', username)

original = 2378
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted) #8732

original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Пожалуй')
    print('хватит )')
print(inverted)
# Пожалуй
# хватит )
# 32

for i in 1, -2, 3, 14, 5:
    print(i) #1 # -2 #3 # 14 #5

r = range(5)           # range (0, 5)
r = range(2, 5)        # range (2, 5)
r = range(-5, 0)       # range (-5, 0)
r = range(1, 10, 2)    # range (1, 10, 2)
r = range(100, 0, -20) # range(100, 0, -20)
for i in r:
    print(i)           # 100 80  60 40 20
for i in range(5):
    print(i)           # 0 1 2 3 4 5

line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line) # 5 рядов по 5 *

# СТРОКИ
text = 'съешь еще этих мягких французских булок'
print(len(text))                 # 39
print('еще' in text)             # True
print(text.isdigit())            # False
print(text.islower())            # True
print(text.replace('еще','ЕЩЕ')) #
# for c in text:
#     print(c) # разбил по буквам
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[len(text)-2:]) # ок
print(text[-1]) # к
print(text[:]) # весь текст
print(text[:2]) # cъ
print(text[0:len(text):6]) # сеикакл - каждый 0-1 символ при разбивке на группы по 6 по всему тексту
print(text[::6]) # сеикакл
text = text[2:9]+text[-5]+text[:2]
print(text)

# СПИСКИ
numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]
numbers = list(range(1,6))
print(numbers) # [1, 2, 3, 4, 5]
numbers[0]=10
print(numbers) # [10, 2, 3, 4, 5]
for i in numbers:
    i*=2
    print(i) # [20, 4, 6, 8, 10]
print(numbers) # [10, 2, 3, 4, 5]

colors = ['red', 'green', 'blue']
for e in colors:
    print(e) # red green blue
for e in colors:
    print(e*2) # redred greengreen blueblue
colors.append('gray') # добавить в конец
print (colors == ['red', 'green', 'blue', 'gray']) #True
colors.remove ('red') #del colors[0] #удалить элемент
print(colors) # ['green', 'blue', 'gray']

# ФУНКЦИИ
def f(x):
    return x**2

def f(x):
    if x==1:
        return 'Целое'
    elif x==2.3:
        return 23
    else:
        return

print(f(1))   # Целое
print(f(2.3)) # 23
print(f(8))   # None
print(type(f(1)))   # str
print(type(f(2.3))) # int
print(type(f(8)))   # NoneType