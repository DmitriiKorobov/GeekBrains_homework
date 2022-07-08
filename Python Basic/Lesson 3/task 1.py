def num_translate_adv(number):
    numbers = {"one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять",
               "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}
    if number in numbers:
        print(numbers[number])
    elif number is not numbers:
        number = number.lower()
        print(numbers[number].capitalize())
    else:
        print('None')
