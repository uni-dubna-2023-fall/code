

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        real_sum = self.real + other.real
        imag_sum = self.imag + other.imag
        return ComplexNumber(real_sum, imag_sum)

    def __sub__(self, other):
        real_diff = self.real - other.real
        imag_diff = self.imag - other.imag
        return ComplexNumber(real_diff, imag_diff)

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            real_prod = self.real * other.real - self.imag * other.imag
            imag_prod = self.real * other.imag + self.imag * other.real
            return ComplexNumber(real_prod, imag_prod)
        else:
            raise TypeError("Unsupported operand type: '{}'"
                            .format(type(other)))

    def __truediv__(self, other):
        if isinstance(other, ComplexNumber):
            denominator = other.real ** 2 + other.imag ** 2
            real_quot = ((self.real * other.real + self.imag * other.imag)
                         / denominator)
            imag_quot = ((self.imag * other.real - self.real * other.imag)
                         / denominator)
            return ComplexNumber(real_quot, imag_quot)
        else:
            raise TypeError("Unsupported operand type: '{}'"
                            .format(type(other)))

    def __str__(self):
        return f"({self.real}, {self.imag})"
