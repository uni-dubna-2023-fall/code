class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        sum_real = self.real + other.real
        sum_imaginary = self.imaginary + other.imaginary
        return ComplexNumber(sum_real, sum_imaginary)

    def __sub__(self, other):
        diff_real = self.real - other.real
        diff_imaginary = self.imaginary - other.imaginary
        return ComplexNumber(diff_real, diff_imaginary)

    def __mul__(self, other):
        product_real = self.real * other.real - self.imaginary * other.imaginary
        product_imaginary = (
            self.real * other.imaginary + self.imaginary * other.real
        )
        return ComplexNumber(product_real, product_imaginary)

    def __truediv__(self, other):
        div_real = (
            self.real * other.real + self.imaginary * other.imaginary
        ) / (other.real**2 + other.imaginary**2)
        div_imaginary = (
            self.imaginary * other.real - self.real * other.imaginary
        ) / (other.real**2 + other.imaginary**2)
        return ComplexNumber(div_real, div_imaginary)

    def __str__(self):
        if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} - {abs(self.imaginary)}i"
