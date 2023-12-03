class ComplexNumber:
    def __init__(self, realnoe, mnimoe):
        self.realnoe = realnoe
        self.mnimoe = mnimoe

    def __add__(self, novoe):
        realnoe = self.realnoe + novoe.realnoe
        mnimoe = self.mnimoe + novoe.mnimoe
        return ComplexNumber(realnoe, mnimoe)

    def __sub__(self, novoe):
        realnoe = self.realnoe - novoe.realnoe
        mnimoe = self.mnimoe - novoe.mnimoe
        return ComplexNumber(realnoe, mnimoe)

    def __mul__(self, novoe):
        realnoe = self.realnoe * novoe.realnoe - self.mnimoe * novoe.mnimoe
        mnimoe = self.realnoe * novoe.mnimoe + self.mnimoe * novoe.realnoe
        return ComplexNumber(realnoe, mnimoe)

    def __truediv__(self, novoe):
        realnoe = self.realnoe * novoe.realnoe + self.mnimoe * novoe.mnimoe
        realnoe = realnoe / ((novoe.mnimoe ** 2) + (novoe.realnoe ** 2))
        mnimoe = self.mnimoe * novoe.realnoe - self.realnoe * novoe.mnimoe
        mnimoe = mnimoe / ((novoe.mnimoe ** 2) + (novoe.realnoe ** 2))
        return ComplexNumber(realnoe, mnimoe)

    def __str__(self):
        return f"({self.realnoe}, {self.mnimoe})"
