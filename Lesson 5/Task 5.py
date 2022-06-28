src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def generate(src):
    result = []
    for item in src:
        if src.count(item) == 1:
            result.append(item)
    return result


print(generate(src))


def answer(src):
    result = [item for item in src if src.count(item) == 1]
    return result


print(answer(src))
