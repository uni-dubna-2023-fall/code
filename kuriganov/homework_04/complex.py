class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def add(self, other):
        real_sum = self.real + other.real
        imaginary_sum = self.imaginary + other.imaginary
        return ComplexNumber(real_sum, imaginary_sum)

    def subtract(self, other):
        real_difference = self.real - other.real
        imaginary_difference = self.imaginary - other.imaginary
        return ComplexNumber(real_difference, imaginary_difference)

    def multiply(self, other):
        real_product = (self.real * other.real) - (self.imaginary * other.imaginary)
        imaginary_product = (self.real * other.imaginary) + (self.imaginary * other.real)
        return ComplexNumber(real_product, imaginary_product)

    def divide(self, other):
        denominator = (other.real ** 2) + (other.imaginary ** 2)
        real_quotient = ((self.real * other.real) + (self.imaginary * other.imaginary)) / denominator
        imaginary_quotient = ((self.imaginary * other.real) - (self.real * other.imaginary)) / denominator
        return ComplexNumber(real_quotient, imaginary_quotient)

    def modulus(self):
        return ((self.real ** 2) + (self.imaginary ** 2)) ** 0.5

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def __str__(self):
        if self.real == 0 and self.imaginary == 0:
            return "0"
        elif self.real == 0:
            return str(self.imaginary) + "i"
        elif self.imaginary == 0:
            return str(self.real)
        else:
            if self.imaginary > 0:
                return str(self.real) + " + " + str(self.imaginary) + "i"
            else:
                return str(self.real) + " - " + str(abs(self.imaginary)) + "i"
