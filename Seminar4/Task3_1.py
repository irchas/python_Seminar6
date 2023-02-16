""" 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
2) используя функцию sort() """

def my_func(*arg):
    arg1 = int(input("Введите первое число: "))
    arg2 = int(input("Введите второе число: "))
    arg3 = int(input("Введите второе число: "))
    my_list = [arg1, arg2, arg3]
    my_list_1 = sorted(my_list)
    print(my_list_1)
    sum = my_list_1[-1] + my_list_1[-2]
    return sum
        
print(f'{my_func()}')