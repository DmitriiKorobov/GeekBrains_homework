from Task 4 import *


class improved_storage(Storage):
    def __init__(self, storage_places, department):
        super().__init__(storage_places, used_place=0, storage_lst=[])
        self.department = department

    def add_to_storage(self, device, department):
        self.used_place += 1
        self.storage_lst.append((device.name, department))
        print(f'{device.name} added, in the storage to {department}, {self.storage_places - int(self.used_place)} '
              f'places left')


if __name__ == '__main__':
    my_printer_2 = Printer('002', 'my_printer_2', 'green')
    my_printer_2.print_text('Error')

    my_fridge_2 = Fridge('002', 'my_fridge_2', '-700')
    my_fridge_2.froze_meal('meat')

    town_storage = improved_storage(50, 'first_department')

    town_storage.add_to_storage(my_printer_2, 'first_department')
    town_storage.add_to_storage(my_fridge_2, 'second_department')

    print(f'Now in the storage: {town_storage.storage_lst}')