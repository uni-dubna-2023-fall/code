import json
import os


class ProbabilityMoments:
    def __init__(self, filename):
        self.filename = filename
        self.data = []

    def __enter__(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)

    def add(self, x):
        self.data.append(x)

    def mean(self):
        return sum(self.data) / len(self.data) if self.data else None

    def variance(self):
        n = len(self.data)
        if n < 2:
            return None
        mean_val = self.mean()
        if mean_val is not None:
            return sum((x - mean_val) ** 2 for x in self.data) / (n-1)   # This line is changed
        return None
