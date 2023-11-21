import math


def shift(dx, dy):
        def wrapper(*args):
            new_args = []
            for x, y in args:
                new_args.append((x + dx, y + dy))
            return func(*new_args)

        return wrapper()



def reflect(func):
    def wrapper(*args):
        new_args = []
        for x, y in args:
            new_args.append((-x, -y))
        return func(*new_args)

    return wrapper()


def rotate(phi):
        def wrapper(*args):
            new_args = []
            cos = math.cos(math.radians(phi))
            sin = math.sin(math.radians(phi))
            for x, y in args:
                new_args.append((x * cos - y * sin, x * sin + y * cos))
            return func(*new_args)

        return wrapper()

