import math

def shift(dx, dy):
    def decorator(func):
        def wrapper(*args):
            new_args = []
            for x, y in args:
                new_x = x + dx
                new_y = y + dy
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

def rotate(theta):
    def decorator(func):
        def wrapper(*args):
            new_args = []
            cos_theta = math.cos(math.radians(theta))
            sin_theta = math.sin(math.radians(theta))
            for x, y in args:
                new_x = x * cos_theta - y * sin_theta
                new_y = x * sin_theta + y * cos_theta
                new_args.append((new_x, new_y))
            return func(*new_args)
        return wrapper
    return decorator
def compute(*args):
    for point in args:
        print(point)
