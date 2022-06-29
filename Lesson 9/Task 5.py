class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Start draw')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
        self.title = title

    def draw(self):
        print(f'"{self.title}" - written by pen')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
        self.title = title

    def draw(self):
        print(f'"{self.title}" - written by pencil')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
        self.title = title

    def draw(self):
        print(f'"{self.title}" - written by handle')


if __name__ == '__main__':
    pen = Pen('Random text written by pen')
    pen.draw()
    pencil = Pencil('Random text written by pencil')
    pencil.draw()
    handle = Handle('Random text written by handle')
    handle.draw()
