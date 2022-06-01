numbers = 1
while numbers <= 100:
    number = str(numbers)
    sector = number[-1]
    if numbers == 11 or '5' <= sector <= '9' or sector == '0':
        print(numbers, 'процентов')
    elif numbers == 1:
        print(numbers, 'процент')
    elif '1' < sector <= '4':
        print(numbers, 'процента')
    numbers += 1
