def odd_to_i(start, end):
    for num in range(start, end + 1, 2):
        yield num


print(*(odd_to_i(1, 15)), sep='\n')
