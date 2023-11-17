class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        real_sum = self.real + other.real
        imag_sum = self.imaginary + other.imaginary
        return ComplexNumber(real_sum, imag_sum)

    def __sub__(self, other):
        real_diff = self.real - other.real
        imag_diff = self.imaginary - other.imaginary
        return ComplexNumber(real_diff, imag_diff)

    def __mul__(self, other):
        real_prod = (self.real * other.real) - (self.imaginary * other.imaginary)
        imag_prod = (self.real * other.imaginary) + (self.imaginary * other.real)
        return ComplexNumber(real_prod, imag_prod)

    def __truediv__(self, other):
        divisor = (other.real**2 + other.imaginary**2)
        real_quot = ((self.real * other.real) + (self.imaginary * other.imaginary)) / divisor
        imag_quot = ((self.imaginary * other.real) - (self.real * other.imaginary)) / divisor
        return ComplexNumber(real_quot, imag_quot)

    def __str__(self):
        return "({}, {})".format(self.real, self.imaginary)
