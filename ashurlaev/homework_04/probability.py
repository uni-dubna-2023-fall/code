import math
from m import ProbabilityMoments

def shift(dx, dy):
    def decorator(func):
        def wrapper(*args):
            a_args = []
            for x, y in args:
                shifted_x = x + dx
                shifted_y = y + dy
                a_args.append((shifted_x, shifted_y))
            return func(*a_args)
        return wrapper
    return decorator


def reflect(func):
    def wrapper(*args):
        reflected_args = []
        for x, y in args:
            reflected_x = -x
            reflected_y = -y
            reflected_args.append((reflected_x, reflected_y))
        return func(*reflected_args)
    return wrapper


def rotate(angle):
    def decorator(func):
        def wrapper(*args):
            radians = math.radians(angle)
            povorot_args = []
            for x, y in args:
                rotated_x = x * math.cos(radians) - y * math.sin(radians)
                rotated_y = x * math.sin(radians) + y * math.cos(radians)
                povorot_args.append((rotated_x, rotated_y))
            return func(*povorot_args)
        return wrapper
    return decorator