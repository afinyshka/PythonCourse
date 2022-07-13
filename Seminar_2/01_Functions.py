def func(param_1: int, param_2: int, param_3: int, param_4: int=10) -> float:
    summ = param_1 + param_2 + param_3 + param_4
    return summ
    

print(func(1, 2, 3, 4))

# функции с кортежами и словарями

def func(param_1, *args, **keys) -> int:
    print(param_1, args, keys)
    

func(1, 645, 856, 234, 745, 756, 123, 3423, key_1=123, key_2=55)