

class ComplexNumber:
    def __init__(self, r, i):
        self.real = r
        self.imag = i

    def __add__(self, another):
        r_sum = self.real + another.real
        i_sum = self.imag + another.imag
        return ComplexNumber(r_sum, i_sum)

    def __sub__(self, another):
        r_diff = self.real - another.real
        i_diff = self.imag - another.imag
        return ComplexNumber(r_diff, i_diff)

    def __mul__(self, another):
        if isinstance(another, ComplexNumber):
            r_prod = self.real * another.real - self.imag * another.imag
            i_prod = self.real * another.imag + self.imag * another.real
            return ComplexNumber(r_prod, i_prod)
        else:
            raise TypeError("Unsupported operand type: '{}'"
                            .format(type(another)))

    def __truediv__(self, another):
        if isinstance(another, ComplexNumber):
            denominator = another.real**2 + another.imag**2
            r_quot = ((self.real * another.real + self.imag * another.imag)
                      / denominator)
            i_quot = ((self.imag * another.real - self.real * another.imag)
                      / denominator)
            return ComplexNumber(r_quot, i_quot)
        else:
            raise TypeError("Unsupported operand type: '{}'"
                            .format(type(another)))

    def __str__(self):
        return f"({self.real}, {self.imag})"
