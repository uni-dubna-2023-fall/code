class ComplexNumber:
    def __init__(self, realnoe, mnimoe):
        self.realnoe = realnoe
        self.mnimoe = mnimoe

    def __add__(self, novoe):
        return ComplexNumber((self.realnoe + novoe.realnoe), (self.mnimoe + novoe.mnimoe))

    def __sub__(self, novoe):
        return ComplexNumber(self.realnoe - novoe.realnoe, self.mnimoe - novoe.mnimoe)

    def __mul__(self, novoe):
        if isinstance(novoe, ComplexNumber):
            return ComplexNumber(self.realnoe * novoe.realnoe - self.mnimoe * novoe.mnimoe, self.mnimoe * novoe.realnoe + self.realnoe * novoe.mnimoe)

    def __truediv__(self, novoe):
            realnoe = ((self.realnoe * novoe.realnoe + self.mnimoe * novoe.mnimoe) / (novoe.mnimoe^2 + novoe.realnoe^2))
            mnimoe = ((self.mnimoe * novoe.realnoe + self.realnoe * novoe.mnimoe) / (novoe.mnimoe^2 + novoe.realnoe^2))
            return ComplexNumber(realnoe, mnimoe)
    def __str__(self):
        return f"({self.realnoe}, {self.mnimoe})"