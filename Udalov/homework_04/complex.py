class ComplexNumber:
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real,
                             self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real,
                             self.imag - other.imag)

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real * other.real
                                 - self.imag * other.imag,
                                 self.imag * other.real
                                 + self.real * other.imag)

    def __str__(self):
        return f"({self.real}, {self.imag})"

    def __truediv__(self, other):
        if isinstance(other, ComplexNumber):
            sr, si, oR, oi = self.real, self.imag, \
                other.real, other.imag
            r = float(oR ** 2 + oi ** 2)
            return ComplexNumber((sr * oR + si * oi) / r,
                                 (si * oR - sr * oi) / r)
