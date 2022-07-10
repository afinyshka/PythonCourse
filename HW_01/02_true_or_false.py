# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# ¬ not инверсия - отрицание
# ⋁ or  дизъюнкция - логическое сложение
# ⋀ and конъюнкция - логическое умножение

x = int(input('Enter x = '))
y = int(input('Enter y = '))
z = int(input('Enter z = '))
print ((not(x or y or z)) == (not x and not y and not z))