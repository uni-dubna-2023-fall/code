class ComplexNumber:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def __add__(self, a):
        return ComplexNumber(self.re + a.re, self.im + a.im)

    def __sub__(self, a):
        return ComplexNumber(self.re - a.re, self.im - a.im)

    def __mul__(self, a):
        re = self.re * a.re - self.im * a.im
        im = self.re * a.im + self.im * a.re
        return ComplexNumber(re, im)

    def __truediv__(self, a):
        re = (self.re * a.re + self.im * a.im) / (a.re * a.re + a.im * a.im)
        im = (self.im * a.re - self.re * a.im) / (a.re * a.re + a.im * a.im)
        return ComplexNumber(re, im)

    def __str__(self):
        return f"({self.re}, {self.im})"
