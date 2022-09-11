"""
Второй вариант, через функцию
"""

import math


def func():
    d = float(input('Enter rounder (at 0.1 to 0.0000000001) '))
    if 10**(-1) >= d >= 10**(-10):
        print(round(math.pi, (len(str(d))-2)))
    else:
        print('rounder out of range at 0.1 to 0.0000000001')


func()