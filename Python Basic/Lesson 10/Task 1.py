class Matrix:
    i = 0

    def __init__(self, optional_one, optional_two=None):
        Matrix.i += 1
        self.optional_one = optional_one
        self.optional_two = optional_two

    def __str__(self):
        if self.optional_two is None:
            for i in self.optional_one:
                print(" ".join(map(str, i)))
        else:
            for i in self.optional_one:
                print(" ".join(map(str, i)))
            for j in self.optional_two:
                print(" ".join(map(str, j)))

    def __add__(self, other):
        result = []
        for i in range(len(self.optional_one)):
            result.append([self.optional_one[i][j] + other[i][j] for j in range(len(self.optional_one[0]))])
        for i in result:
            print(" ".join(map(str, i)))

    def sum_matrix(self):
        if self.optional_two:
            result = []
            for i in range(len(self.optional_one)):
                result.append(
                    [self.optional_one[i][j] + self.optional_two[i][j] for j in range(len(self.optional_one[0]))])
            for i in result:
                print(" ".join(map(str, i)))
        else:
            print('None')


if __name__ == '__main__':
    data_one = Matrix([[31, 22, 56, 89], [37, 43, 76, 8]])
    data_one.__str__()

    data_two = Matrix([[1, 1, 1, 1], [1, 1, 1, 1]])
    data_two.__str__()

    data_one.__add__(data_two.optional_one)

    answer = Matrix([[31, 22], [37, 43], [51, 86]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    answer.__str__()
    answer.sum_matrix()
