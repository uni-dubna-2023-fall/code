import math


def shift(x0, y0):
    def shift(compute):
        def shiftcomp(*args):
            dop = []
            for el in range(len(args)):
                x = args[el][0]
                x = x + x0
                y = args[el][1]
                y = y + y0
                row = (x, y)
                dop.append(row)
            args1 = tuple(dop)
            return compute(*args1)
        return shiftcomp
    return shift


def reflect(compute):
    def refcomp(*args):
        dop = []
        for el in range(len(args)):
            x = args[el][0]
            if x == 0.0:
                x = 0.0
            else:
                x = -x
            y = args[el][1]
            if y == 0.0:
                y = 0.0
            else:
                y = -y
            row = (x, y)
            dop.append(row)
        args1 = tuple(dop)
        return compute(*args1)
    return refcomp


def rotate(fi):
    def rotate(compute):
        def rotatecomp(*args):
            fi1 = (math.pi * fi) / 180
            dop = []
            for el in range(len(args)):
                x = args[el][0]
                y = args[el][1]
                x1 = x * math.cos(fi1) + (-1.0) * y * math.sin(fi1)
                y1 = x * math.sin(fi1) + y * math.cos(fi1)
                row = (x1, y1)
                dop.append(row)
            args1 = tuple(dop)
            return compute(*args1)
        return rotatecomp
    return rotate
