from abc import ABC
from abc import abstractmethod


class clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def how_much(self):
        pass


class coat(clothes):
    def __init__(self, name, v):
        super().__init__(name)
        self.v = v

    @property
    def calc_cunsumption(self):
        return f'{self.v // 6.5 + 0.5} m fabric spent on {self.name} coat'

    def how_much(self):
        print('It`s very expensive')


class suit(clothes):
    def __init__(self, name, h):
        super().__init__(name)
        self.h = h

    @property
    def calc_consumption(self):
        return f'{2 * self.h + 0.3} m fabric spent on {self.name} suit'

    def how_much(self):
        print('It`s very cheap')


if __name__ == '__main__':
    coat_1 = coat('brand_one', 43)
    print(coat_1.calc_cunsumption)
    coat_1.how_much()

    suit_1 = suit('brand_two', 180)
    print(suit_1.calc_consumption)
    suit_1.how_much()