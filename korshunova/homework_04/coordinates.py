def shift(func):
    def wrapper(*args):
        radius_vector = args[0]    
        shifted_args = [(arg[0] + radius_vector[0], arg[1] + radius_vector[1]) for arg in args[1:]]
        result = func(*shifted_args)
        return result
    return wrapper


def reflect(func):
    def wrapper(*args):
        reflected_args = [(-arg[0], -arg[1]) for arg in args]
        result = func(*reflected_args)
        return result
    return wrapper


def rotate(func):
    def wrapper(*args):
        angle = args[0]
        angle_rad = math.radians(angle)
        rotated_args = [(arg[0] * math.cos(angle_rad) - arg[1] * math.sin(angle_rad),
                         arg[0] * math.sin(angle_rad) + arg[1] * math.cos(angle_rad)) for arg in args[1:]]
        result = func(*rotated_args)
        return result
    return wrapper


def compute(*args):
    pass


@shift
@reflect
@rotate
def compute_transformed(*args):
    return compute(*args)


import math
math.sin(0.0)