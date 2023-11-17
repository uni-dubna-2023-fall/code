import math


def shift(x_shift, y_shift):
    def decorator(func):
        def wrapper(*args):
            new_args = []
            for x, y in args:
                new_x = x + x_shift
                new_y = y + y_shift
                new_args.append((new_x, new_y))
            return func(*new_args)
        return wrapper
    return decorator


def reflect(func):
    def wrapper(*args):
        new_args = []
        for x, y in args:
            new_x = -x
            new_y = -y
            new_args.append((new_x, new_y))
        return func(*new_args)
    return wrapper


def rotate(angle):
    def decorator(func):
        def wrapper(*args):
            new_args = []
            cos_angle = math.cos(math.radians(angle))
            sin_angle = math.sin(math.radians(angle))
            for x, y in args:
                new_x = x * cos_angle - y * sin_angle
                new_y = x * sin_angle + y * cos_angle
                new_args.append((new_x, new_y))
            return func(*new_args)
        return wrapper
    return decorator


def compute(*args):
    for point in args:
        print(point)
