class ComplexNumber:
    def __init__(self, x, y):
        self.re = x
        self.im = y

    def __add__(self, x):
        c = ComplexNumber(0, 0)
        c.re = self.re + x.re
        c.im = self.im + x.im
        return c

    def __sub__(self, x):
        c = ComplexNumber(0, 0)
        c.re = self.re - x.re
        c.im = self.im - x.im
        return c

    def __mul__(self, other):
        c = ComplexNumber(0, 0)
        c.re = self.re * other.re - self.im * other.im
        c.im = self.re * other.im - self.im * other.re
        return c

    def __truediv__(self, other):
        if other == 0:
            return ComplexNumber(self.re / other, self.im / other)

    def __str__(self):
        return f'({self.re}, {self.im})'


c1 = ComplexNumber(1, 1)
c2 = ComplexNumber(2, 3)
c = c1 + c2
print(c)
c1 = ComplexNumber(1, 1)
c2 = ComplexNumber(1, -1)
print(c1 / 2)
