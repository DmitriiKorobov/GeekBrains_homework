class Cell:
    def __init__(self, nucleus_num):
        self.nucleus_num = nucleus_num

    def __add__(self, other):
        cell_3 = Cell(self.nucleus_num + other.nucleus_num)
        return cell_3

    def __str__(self):
        return f'{self.nucleus_num} cells'

    def __sub__(self, other):
        if self.nucleus_num >= other.nucleus_num:
            return Cell(self.nucleus_num - other.nucleus_num)
        else:
            return 'residual of cells is less 0'

    def __mul__(self, other):
        cell_3 = Cell(self.nucleus_num * other.nucleus_num)
        return cell_3

    def __floordiv__(self, other):
        cell_3 = Cell(self.nucleus_num // other.nucleus_num)
        return cell_3

    def __truediv__(self, other):
        cell_3 = Cell(self.nucleus_num / other.nucleus_num)
        return cell_3

    def make_order(self, cells_num):
        rows_num = self.nucleus_num // cells_num
        last_row_num = self.nucleus_num % cells_num

        return ('*' * cells_num + '\n') * rows_num + '*' * last_row_num,


if __name__ == '__main__':
    cell_1 = Cell(2500)
    cell_2 = Cell(17)
