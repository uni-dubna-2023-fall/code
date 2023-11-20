class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imag + other.imag)
        else:
            raise ValueError("Unsupported operand type for +: {}"
                             .format(type(other)))

    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real - other.real, self.imag - other.imag)
        else:
            raise ValueError("Unsupported operand type for -: {}"
                             .format(type(other)))

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            # (a + bi)(c + di) = (ac - bd) + (ad + bc)i
            real_part = self.real * other.real - self.imag * other.imag
            imag_part = self.real * other.imag + self.imag * other.real
            return ComplexNumber(real_part, imag_part)
        else:
            raise ValueError("Unsupported operand type for *: {}"
                             .format(type(other)))

    def __truediv__(self, other):
        if isinstance(other, ComplexNumber):
            # (a + bi)/(c + di) = (ac + bd)/(c^2 + d^2) + (bc - ad)/(c^2 + d^2)i
            denominator = other.real**2 + other.imag**2
            real_part = (self.real * other.real + self.imag * other.imag
                         ) / denominator
            imag_part = (self.imag * other.real - self.real * other.imag
                         ) / denominator
            return ComplexNumber(real_part, imag_part)
        else:
            raise ValueError("Unsupported operand type for /: {}"
                             .format(type(other)))

    def __str__(self):
        return "({}, {})".format(self.real, self.imag)
