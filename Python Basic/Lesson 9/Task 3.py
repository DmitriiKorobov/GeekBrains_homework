class Worker:
    __income = {
        'wage': 100000,
        'bonus%': 25
    }

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = self.__income


class Position(Worker):

    def get_full_name(self):
        print(f'Name: {self.name} {self.surname}')

    def get_total_income(self):
        print(f"Monthly salary is {self.income['wage']}$ + bonus {self.income['wage'] // 100 * 25}$")


if __name__ == '__main__':
    employee = Position('Random_name', 'Random_position')
    employee.get_full_name()
    employee.get_total_income()
    print(f'{employee.name} is {employee.position}')
