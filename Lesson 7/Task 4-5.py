import os
from pathlib import Path as P


def make(directory):
    date = {
        100: 0,
        1000: 0,
        10000: 0,
        100000: 0
    }
    dir_link = P.cwd()

    for file in os.listdir(fr'{dir_link}\{directory}'):
        if os.stat(fr'{dir_link}\{directory}\{file}').st_size <= 100:
            date[100] += 1
        elif os.stat(fr'{dir_link}\{directory}\{file}').st_size <= 1000:
            date[1000] += 1
        elif os.stat(fr'{dir_link}\{directory}\{file}').st_size <= 10000:
            date[10000] += 1
        else:
            date[100000] += 1

    with open(f'{directory}_summary.json', 'w', encoding='utf-8') as f:
        f.write(str(date))

    return date


if __name__ == '__main__':
    directory = input('Please enter directory: ')
    print(make(directory))
