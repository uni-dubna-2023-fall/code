import math


class ProbabilityMoments:
    def __init__(self):
        self.d = []

    def add(self, x, y):
        self.d.append((x, y))

    def mean(self):
        if not self.d:
            return None
        sum_x = sum(x for x, _ in self.d)
        sum_y = sum(y for _, y in self.d)
        return sum_x / len(self.d), sum_y / len(self.d)

    def variance(self):
        if len(self.d) < 2:
            return 0
        mean_x, mean_y = self.mean()
        var_x = sum((x - mean_x) ** 2 for x, _ in self.d) / len(self.d)
        var_y = sum((y - mean_y) ** 2 for _, y in self.d) / len(self.d)
        return var_x, var_y

    def shift(self, dx, dy):
        shifted_d = [(x + dx, y + dy) for x, y in self.d]
        self.d = shifted_d

    def reflect(self):
        reflected_d = [(-x, -y) for x, y in self.d]
        self.d = reflected_d

    def rotate(self, angle):
        radians = math.radians(angle)
        rotated_d = [(x * math.cos(radians) - y * math.sin(radians),
            x * math.sin(radians) + y * math.cos(radians)) for x, y in self.d]
        self.d = rotated_d
