# 27-07-2022
def int_filter(fn):
    def inner_fun(*args):
        return fn([data for data in args if isinstance(data, int)])
    return inner_fun


@int_filter
def add(*args):
    return sum([num for num in args[0]])


print(add(10, 20, 'hello'))


