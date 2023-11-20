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
 