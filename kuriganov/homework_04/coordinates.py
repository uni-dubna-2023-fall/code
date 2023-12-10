import math


def shift(dx, dy):
    def decorator(func):
        def wrapper(*args):
            changed_args = []
            for x, y in args:
                changed_args.append((x + dx, y + dy))
            return func(*changed_args)
        return wrapper

    return decorator


def reflect(func):
    def wrapper(*args):
        reflected_args = []
        for x, y in args:
            reflected_args.append((-x, -y))
        return func(*reflected_args)

    return wrapper


def rotate(angle):
    def decorator(func):
        def wrapper(*args):
            rotated_args = []
            cos_angle = math.cos(math.radians(angle))
            sin_angle = math.sin(math.radians(angle))
            for x, y in args:
                rotated_x = x * cos_angle - y * sin_angle
                rotated_y = x * sin_angle + y * cos_angle
                rotated_args.append((rotated_x, rotated_y))
            return func(*rotated_args)

        return wrapper

    return decorator
