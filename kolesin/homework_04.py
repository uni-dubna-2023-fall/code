class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        real_sum = self.real + other.real
        imaginary_sum = self.imaginary + other.imaginary
        return ComplexNumber(real_sum, imaginary_sum)

    def __sub__(self, other):
        real_diff = self.real - other.real
        imaginary_diff = self.imaginary - other.imaginary
        return ComplexNumber(real_diff, imaginary_diff)

    def __mul__(self, other):
        real_prod = self.real * other.real - self.imaginary * other.imaginary
        imaginary_prod = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_prod, imaginary_prod)

    def __truediv__(self, other):
        denominator = other.real**2 + other.imaginary**2
        real_quot = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imaginary_quot = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return ComplexNumber(real_quot, imaginary_quot)

    def __str__(self):
        return f"({self.real}, {self.imaginary})"
    
    ##
    import json

class ProbabilityMoments:
    def __init__(self, filename):
        self.filename = filename
        self.data = []

    def __enter__(self):
        try:
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = []

        return self

    def __exit__(self, *args):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)

    def add(self, x):
        self.data.append(x)

    def mean(self):
        if len(self.data) == 0:
            return 0

        total = sum(self.data)
        return total / len(self.data)

    def variance(self):
        if len(self.data) < 2:
            return 0

        mean_value = self.mean()
        squared_diff = [(x - mean_value) ** 2 for x in self.data]
        total = sum(squared_diff)
        return total / (len(self.data) - 1)
    
    ##
    import math

class Shift:
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy
    
    def __call__(self, func):
        def wrapper(*args):
            new_args = [(x + self.dx, y + self.dy) for x, y in args]
            return func(*new_args)
        return wrapper


class Reflect:
    def __call__(self, func):
        def wrapper(*args):
            new_args = [(-x, -y) for x, y in args]
            return func(*new_args)
        return wrapper


class Rotate:
    def __init__(self, angle):
        self.angle = angle
    
    def __call__(self, func):
        def wrapper(*args):
            r = math.radians(self.angle)
            new_args = [(x * math.cos(r) - y * math.sin(r),
                         x * math.sin(r) + y * math.cos(r)) for x, y in args]
            return func(*new_args)
        return wrapper