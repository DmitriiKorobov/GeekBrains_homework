import math


class number(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.x = complex(a, b)

    def __add__(self, other):
        return f'sum {self.x} and {other.x}: {complex((self.a + other.a), (self.b + other.b))}'


if __name__ == '__main__':
    example_one = number(8, 2)
    example_two = number(1, 3)
    print(example_one + example_two)
