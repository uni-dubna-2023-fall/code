import math


def shift(dx, dy):
    def decorator(func):
        def wrapper(*args):
            new_args = []
            for point in range(len(args)):
                x = (args[point][0] + dx)
                y = (args[point][1] + dy)
                dop = ((x, y))
                new_args.append(dop)
            res = tuple(new_args)
            return func(*res)
        return wrapper
    return decorator


def reflect(func):
    def wrapper(*args):
        new_args = []
        for point in range(len(args)):
            x = (-args[point][0])
            y = (-args[point][1])
            dop = ((x, y))
            new_args.append(dop)
        res = tuple(new_args)
        return func(*res)
    return wrapper


def rotate(angle):
    def decorator(func):
        def wrapper(*args):
            new_args = []
            for point in range(len(args)):
                r = math.radians(angle)
                x = (args[point][0] * math.cos(r)
                     - args[point][1] * math.sin(r))
                y = (args[point][0] * math.sin(r)
                     + args[point][1] * math.cos(r))
                dop = ((x, y))
                new_args.append(dop)
            res = tuple(new_args)
            return func(*res)
        return wrapper
    return decorator
