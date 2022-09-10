"""
Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""


def func(x):
    tmp = x.copy()
    answer = []
    for i in range(len(tmp)):
        answer.append(tmp.pop(0) * tmp.pop())
        if len(tmp) == 1:
            answer.append(tmp.pop() ** 2)
            break
    print(f'{x} => {answer}')


a = int(input('Enter number "a" for range (a, b) '))
b = int(input(f'Enter number "b" for range ({a}, b) '))
lst = [i for i in range(a, b + 1)]

func(lst)
