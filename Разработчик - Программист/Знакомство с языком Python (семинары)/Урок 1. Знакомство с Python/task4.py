"""
Напишите программу, которая принимает на вход координаты
двух точеки находит расстояние между ними в 2D пространстве.
"""
xa = int(input('Enter xa for A (xa, ya) '))
ya = int(input(f'Enter xa for A ({xa}, ya) '))
xb = int(input('Enter xa for B (xb, yb) '))
yb = int(input(f'Enter xa for B ({xb}, yb) '))
answer = ((xb - xa)**2 + (yb - ya)**2)**0.5
print(f'A ({xa},{ya}); B ({xb},{yb}) -> {round(answer, 2)}')