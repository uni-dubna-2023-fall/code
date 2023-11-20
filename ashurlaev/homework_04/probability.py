import math


class ProbabilityMoments:
    def __init__(self):
        self.data = []

    def add(self, x, y):
        self.data.append((x, y))

    def mean(self):
        if not self.data:
            return None
        sum_x = sum(x for x, _ in self.data)
        sum_y = sum(y for _, y in self.data)
        return sum_x / len(self.data), sum_y / len(self.data)

    def variance(self):
        if len(self.data) < 2:
            return 0
        mean_x, mean_y = self.mean()
        var_x = sum((x - mean_x) ** 2 for x, _ in self.data) / len(self.data)
        var_y = sum((y - mean_y) ** 2 for _, y in self.data) / len(self.data)
        return var_x, var_y

    def shift(self, dx, dy):
        shifted_data = [(x + dx, y + dy) for x, y in self.data]
        self.data = shifted_data

    def reflect(self):
        reflected_data = [(-x, -y) for x, y in self.data]
        self.data = reflected_data

    def rotate(self, angle):
        radians = math.radians(angle)
        rotated_data = [(x * math.cos(radians) - y * math.sin(radians),
                         x * math.sin(radians) + y * math.cos(radians))
                        for x, y in self.data]
        self.data = rotated_data


moments = ProbabilityMoments()