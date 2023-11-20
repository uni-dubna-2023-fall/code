from math import sin, cos, radians


def reverse_args(func):
    def rfunc(*args):
        return func(*reversed(args))

    return rfunc


@reverse_args
def my_func(first, second):
    print(f"First: {first}, Second: {second}")


def shift(dec_a, dec_b):
    def f(func):
        def rfunc(*args):
            a = dec_a + args[0]
            b = dec_b + args[1]
            return func(a, b)

        return rfunc

    return f


def rotate(angle):
    def f(func):
        def rfunc(*args):
            a, [x, y] = radians(angle), args
            Y = x * sin(a) + y * cos(a)
            X = x * cos(a) - y * sin(a)
            return func(X, Y)

        return rfunc

    return f


def relect(func):
    def wrapper(*args):
        a, b = -args[0], -args[1]
        return func(a, b)

    return wrapper


@shift(1, 2)
@relect
def my_func1(first, second):
    print(f"First: {first}, Second: {second}")


@rotate(180.0)
def my_func2(first, second):
    print(f"First: {first}, Second: {second}")


print(my_func2(1, 2))
