import math


def shift(x_shift, y_shift):
    def decorator(func):
        def wrapper(*args):
            new_args = [(x + x_shift, y + y_shift) for x, y in args]
            return func(*new_args) if new_args else func()
        return wrapper
    return decorator


def reflect(func):
    def wrapper(*args):
        new_args = [(-x, -y) for x, y in args]
        return func(*new_args) if new_args else func()
    return wrapper


def rotate(angle):
    def decorator(func):
        def wrapper(*args):
            cos_angle = math.cos(math.radians(angle))
            sin_angle = math.sin(math.radians(angle))
            new_args = [(x * cos_angle - y * sin_angle, x * sin_angle + y * cos_angle) for x, y in args]
            return func(*new_args) if new_args else func()
        return wrapper
    return decorator
