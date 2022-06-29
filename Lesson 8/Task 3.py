def type_logger(func):
    def wrapper(*args):
        result = {i: type(i) for i in args}
        return result
    return wrapper


@type_logger
def calc_cube(*args):
    res = [arg**3 for arg in args]
    return res


if __name__ == '__main__':
    a = calc_cube(5)
    print(a)
    b = calc_cube(12, 8)
    print(b)