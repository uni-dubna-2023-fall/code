class ComplexNumber:
    def __init__(self, real, im):
        self.real = real
        self.im = im

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            real = self.real + other.real
            im = self.im + other.im
            return ComplexNumber(real, im)
        else:
            raise TypeError("Нельзя складывать ComplexNumber с другим типом")

    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            real = self.real - other.real
            im = self.im - other.im
            return ComplexNumber(real, im)
        else:
            raise TypeError("Нельзя вычитать из ComplexNumber другой тип")

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            real = self.real * other.real - self.im * other.im
            im = self.real * other.im + self.im * other.real
            return ComplexNumber(real, im)
        else:
            raise TypeError("Нельзя умножать ComplexNumber на другой тип")

    def __truediv__(self, other):
        if isinstance(other, ComplexNumber):
            denom = other.real**2 + other.im**2
            real = (self.real * other.real + self.im * other.im) / denom
            im = (self.im * other.real - self.real * other.im) / denom
            return ComplexNumber(real, im)
        else:
            raise TypeError("Нельзя делить ComplexNumber на другой тип")

    def __str__(self):
        return f"({self.real}, {self.im})"
