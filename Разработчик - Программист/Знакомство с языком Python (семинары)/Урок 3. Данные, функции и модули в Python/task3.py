"""
Задайте список из вещественных чисел.
Напишите программу, которая найдёт разницу между максимальным и
минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""


def func(x):
    max_num = 0.0
    min_num = round(x[0] - int(x[0]), 4)
    for i in range(len(x)):
        if max_num < x[i] - int(x[i]):
            max_num = round(x[i] - int(x[i]), 4)
        if min_num > x[i] - int(x[i]) != 0:
            min_num = round(x[i] - int(x[i]), 4)
    print(f'{x} => {max_num - min_num}')


lst = [1.1, 1.2, 3.1, 5, 10.01]
func(lst)
