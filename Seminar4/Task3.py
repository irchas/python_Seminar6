""" 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
2) без функции sort() """

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
        
print(f'{my_func()}')