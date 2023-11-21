import math


def shift(func):
    def wrapper(*args):
        shifted_args = [(x + args[0][0], y + args[0][1]) for x, y in args]
        return func(*shifted_args)

    return wrapper


def reflect(func):
    def wrapper(*args):
        reflected_args = [(-x, -y) for x, y in args]
        return func(*reflected_args)

    return wrapper


def rotate(func):
    def wrapper(*args):
        angle = args[0][0]
        rotated_args = [
            (
                x * math.cos(math.radians(angle))
                - y * math.sin(math.radians(angle)),
                x * math.sin(math.radians(angle))
                + y * math.cos(math.radians(angle)),
            )
            for x, y in args[1:]
        ]
        return func(*rotated_args)

    return wrapper
