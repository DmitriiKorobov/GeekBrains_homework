"""
Реализуйте алгоритм перемешивания списка.
"""
from random import randint

def shake(a):
    print('Old list', a)
    temp_list = []
    for i in range(len(a)):
        c = randint(0, len(a)-1)
        temp_list.append(a.pop(c))
    a.clear()
    a.extend(temp_list)
    print('New list', a)

a = int(input('Enter a for range (a, b) '))
b = int(input(f'Enter b for range ({a}, b) '))
create_list = [i for i in range(a, b+1)]

shake(create_list)