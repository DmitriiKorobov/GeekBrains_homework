class error(Exception):
    def __init__(self, text):
        self.text = text


def create(data=0):
    example = []
    while data != 'stop':
        try:
            data = input('Enter example: ')
            if not data.isdigit():
                raise error(f'{data}" error')
            example.append(data)
        except error as err:
            print(err)


if __name__ == '__main__':
    create()
