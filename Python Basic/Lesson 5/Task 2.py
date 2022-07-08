def odd_to_i(start, end):
    numbers = (num for num in range(start, end + 1, 2))
    return numbers


print(*odd_to_i(1, 15))
