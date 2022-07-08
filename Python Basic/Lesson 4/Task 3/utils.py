import sys

sys.path.append('/Volumes/Macintosh HD/Homework (GeekBrains)/Python Basics/Lesson 4/Task 2')
from Task_2 import *

print(f'List of currency codes{char_code}')
answer = (input(f'Select currency code: '))
print(currency_rates(answer))
