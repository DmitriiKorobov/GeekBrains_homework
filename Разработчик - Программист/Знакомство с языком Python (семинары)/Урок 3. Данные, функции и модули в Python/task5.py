"""
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""

answer = []
tmp = [1, 1, 0, 1, -1]
f1 = 1
f2 = - 1
f3 = f4 = 1
k = int(input())
answer.extend(tmp)

for i in range(2, k):
    f1, f2 = f2, f1 - f2
    answer.append(f2)
answer.reverse()

for i in range(2, k):
    f3, f4 = f4, f3 + f4
    answer.append(f4)

print(answer)

