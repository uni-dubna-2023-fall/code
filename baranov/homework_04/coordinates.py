import math


def shift(dx, dy):
    def camouflage(func):
        def disguise(*args):
            mod_args = [(x + dx, y + dy) for x, y in args]
            return func(*mod_args)
        return disguise
    return camouflage


def reflect(func):
    def disguise(*args):
        mod_args = [(-x, -y) for x, y in args]
        return func(*mod_args)
    return disguise


def rotate(angle):
    def camouflage(func):
        def disguise(*args):
            r = math.radians(angle)
            mod_args = [(x * math.cos(r) - y * math.sin(r),
                         x * math.sin(r) + y * math.cos(r)) for x, y in args]
            return func(*mod_args)
        return disguise
    return camouflage
