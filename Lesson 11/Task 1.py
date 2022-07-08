import re


class Date:

    def __init__(self, date):
        self.date = date

    @classmethod
    def divide_date(cls, date):
        separation = date.split('-')
        day = int(separation[0])
        month = int(separation[1])
        year = int(separation[2])
        return day, month, year

    @staticmethod
    def validate_date(date):
        validate_date = re.compile(r'[0-3]\d-[0-1]\d-2022')
        if not validate_date.match(date):
            return f'Date {date} is NOT valid'
        return f'Date {date} is valid'


if __name__ == '__main__':
    example_one = '19-06-1988'
    example_two = '06-07-2022'
    print(Date.divide_date(example_one))
    print(Date.validate_date(example_one))
    print(Date.validate_date(example_two))
