import json
import math


class ProbabilityMoments:
    def __init__(self, filename):
        self.filename = filename
        self.data = {'values': []}

    def __enter__(self):
        try:
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            pass
        return self

    def __exit__(self, *args):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)

    def add(self, x):
        self.data['values'].append(x)

    def mean(self):
        values = self.data['values']
        if not values:
            return None
        return sum(values) / len(values)

    def variance(self):
        values = self.data['values']
        if len(values) < 2:
            return 0
        mean_value = self.mean()
        variance = sum((x - mean_value) ** 2 for x in values
                       ) / (len(values) - 1)
        return math.sqrt(variance)
