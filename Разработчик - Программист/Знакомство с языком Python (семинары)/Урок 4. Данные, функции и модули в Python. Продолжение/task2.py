"""
Задайте натуральное число N.
Напишите программу, которая составит список простых множителей числа N.
"""

n = int(input('Enter number for N '))
divisor = 2
simple_lst = []
while n >= divisor:
    if n % divisor == 0:
        simple_lst.append(divisor)
        n = n / divisor
        divisor = 2
    else:
        divisor += 1

print(simple_lst)