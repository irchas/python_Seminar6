"""
5. Сделайте профилирование кода любого или любых выполненных заданий
с помощью модуля timeit, опишите результат """
""" Проверка фукнции показала, что функция первая занимает меньше времени, чем вторая"""
from timeit import timeit
print(timeit("""
def my_func(*arg):
    arg1 = int(input("Введите первое число: "))
    arg2 = int(input("Введите второе число: "))
    arg3 = int(input("Введите второе число: "))
    my_list = [arg1, arg2, arg3]
    my_list_1 = sorted(my_list)
    print(my_list_1)
    sum = my_list_1[-1] + my_list_1[-2]
    return sum
""", number=10000))

from timeit import timeit
print(timeit("""
def my_func(*arg):
    arg1 = int(input("Введите первое число: "))
    arg2 = int(input("Введите второе число: "))
    arg3 = int(input("Введите второе число: "))
    if arg1 >= arg2 and arg2 > arg3:
        max_1 = arg1
        max_2 = arg2
    elif arg1 > arg2 and arg3 > arg2:
        max_1 = arg1
        max_2 = arg3
    elif arg2 >= arg3 and arg3 > arg1:
        max_1 = arg2
        max_2 = arg3
    elif arg2 > arg3 and arg1 > arg3:
        max_1 = arg2
        max_2 = arg1
    elif arg3 >= arg2 and arg2 > arg1:
        max_1 = arg3
        max_2 = arg2
    else:
        max_1 = arg3
        max_2 = arg1
    sum = max_1 + max_2
    return sum
""", number=10000))