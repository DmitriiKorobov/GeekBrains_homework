class task_two(Exception):
    def __init__(self, text):
        self.text = text


def numbers(number_one=0, number_two=0):
    while True:
        number_one = int(input('Enter first number: '))
        number_two = int(input('Enter second number: '))
        if number_two == 0:
            raise task_two('ERROR')
        else:
            print(f'Result: {number_one/number_two}')


if __name__ == '__main__':

    try:
        numbers()
    except task_two as err:
        print(err)