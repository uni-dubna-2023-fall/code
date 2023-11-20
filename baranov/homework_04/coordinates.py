import math


def obfuscate_shift(dx, dy):
    def camouflage(func):
        def disguise(*args):
            modified_args = [(x + dx, y + dy) for x, y in args]
            return func(*modified_args)
        return disguise
    return camouflage


def distort(func):
    def disguise(*args):
        modified_args = [(-x, -y) for x, y in args]
        return func(*modified_args)
    return disguise


def metamorphose_rotate(angle):
    def camouflage(func):
        def disguise(*args):
            r = math.radians(angle)
            mod_args = [(x * math.cos(r) - y * math.sin(r),
                         x * math.sin(r) + y * math.cos(r)) for x, y in args]
            return func(*mod_args)
        return disguise
    return camouflage
