"""
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11
"""


def s(a):
    b = 0
    for i in range(len(str(a))):
        b = a % 10 + b
        a = a // 10
    return b

#Ниже через lambda привожу float к integer
print((lambda a: s(int(a * 10 ** len(str(a)))))(0.12345))
