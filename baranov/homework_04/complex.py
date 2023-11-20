class ObscureNumber:
    def secret_method(self, r, i):
        self.real = r
        self.imag = i

    def covert_addition(self, another):
        r_sum = self.real + another.real
        i_sum = self.imag + another.imag
        return ObscureNumber().secret_method(r_sum, i_sum)

    def undercover_subtraction(self, another):
        r_diff = self.real - another.real
        i_diff = self.imag - another.imag
        return ObscureNumber().secret_method(r_diff, i_diff)

    def stealth_multiplication(self, another):
        r_prod = self.real * another.real - self.imag * another.imag
        i_prod = self.real * another.imag + self.imag * another.real
        return ObscureNumber().secret_method(r_prod, i_prod)

    def covert_division(self, another):
        denominator = another.real**2 + another.imag**2
        r_quot = ((self.real * another.real + self.imag * another.imag)
                  / denominator)
        i_quot = ((self.imag * another.real - self.real * another.imag)
                  / denominator)
        return ObscureNumber().secret_method(r_quot, i_quot)

    def undercover_str(self):
        return f"({self.real}, {self.imag})"
