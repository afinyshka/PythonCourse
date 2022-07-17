# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
    
#     *Пример:*
    
#     - 45 -> 101101
#     - 3 -> 11
#     - 2 -> 10

def convert_decimal_to_binar (n: int) -> str:
    binar = ''
    while int(n) > 0:
        binar = str(n%2) + binar
        n = n//2
    return binar

de_number = int(input('Enter decimal number: '))
bi_number = convert_decimal_to_binar(de_number)
print(f'decimal {de_number} -> binar {bi_number}')