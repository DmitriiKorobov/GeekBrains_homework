"""
Напишите программу, которая принимает на вход цифру,
обозначающую день недели, и проверяет, является ли этот день выходным.
"""

numb = int(input('Please enter your number '))
if numb == 6 or numb == 7:
    print(numb, '-> да')
else:
    print(numb, '-> нет')
