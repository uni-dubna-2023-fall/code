class ComplexNumber:
    def __init__(self, real, imaginary):
        self.x = real
        self.y = imaginary

    def __add__(self, other):
        real = self.x + other.x
        imaginary = self.y + other.y
        answer = ComplexNumber(real, imaginary)
        return answer

    def __sub__(self, other):
        real = self.x - other.x
        imaginary = self.y - other.y
        answer = ComplexNumber(real, imaginary)
        return answer

    def __mul__(self, other):
        real = self.x * other.x - self.y * other.y
        imaginary = self.x * other.y + self.y * other.x
        answer = ComplexNumber(real, imaginary)
        return answer

    def __truediv__(self, other):
        denominator = other.x ** 2 + other.y ** 2
        real = (self.x * other.x + self.y * other.y) / denominator
        imaginary = (self.y * other.x - self.x * other.y) / denominator
        answer = ComplexNumber(real, imaginary)
        return answer

    def __str__(self):
        return f"({self.x}, {self.y})"
