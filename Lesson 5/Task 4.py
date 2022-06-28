src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def answer(src):
    lst = list(zip(src[1:], src))
    result = []
    for item in lst:
        if item[1] < item[0]:
            result.append(item[0])
    return result


print(answer(src))
