class Road:

    def __init__(self, width, length, weight, depth):
        self._width = width
        self._length = length
        self._weight = weight
        self._depth = depth

    def calc_mas(self):
        mass = self._width * self._length * self._weight * self._depth
        print(f'the mass of asphalt required to cover {mass // 1000} tonnes.')


if __name__ == '__main__':
    main_road = Road(20, 5000, 25, 5)
    main_road.calc_mas()