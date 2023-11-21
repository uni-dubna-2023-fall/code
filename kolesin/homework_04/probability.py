import json


class ProbabilityMoments:
    def __init__(self, filename):
        self.filename = filename
        self.data = []

    def __enter__(self):
        try:
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = []

        return self

    def __exit__(self, *args):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)

    def add(self, x):
        self.data.append(x)

    def mean(self):
        if len(self.data) == 0:
            return 0

        total = sum(self.data)
        return total / len(self.data)

    def variance(self):
        n = len(self.data)
        if n < 2:
            return 0

        mean_value = self.mean()
        squared_diff = [(x - mean_value) ** 2 for x in self.data]
        total = sum(squared_diff)
        variance = (total / len(self.data)) ** 0.5
        return variance
