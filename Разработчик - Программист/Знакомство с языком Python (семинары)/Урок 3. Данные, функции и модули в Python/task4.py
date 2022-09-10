"""
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
"""
numb = int(input('Enter number '))
tmp = ''

while numb > 0:
    tmp = str(numb % 2) + tmp
    numb //= 2

print(tmp)