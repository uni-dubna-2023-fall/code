import math

def shift(dx, dy):
    def decorator(func):
        def wrapper(*args):
            new_args = [(x + dx, y + dy) for x, y in args]
            return func(*new_args)
        return wrapper
    return decorator

def reflect(func):
    def wrapper(*args):
        new_args = [(-x, -y) for x, y in args]
        return func(*new_args)
    return wrapper

def rotate(angle):
    def decorator(func):
        def wrapper(*args):
            r = math.radians(angle)
            new_args = [(x * math.cos(r) - y * math.sin(r),
                         x * math.sin(r) + y * math.cos(r)) for x, y in args]
            return func(*new_args)
        return wrapper
    return decorator

def compute(*args):
    for point in args:
        print(point)