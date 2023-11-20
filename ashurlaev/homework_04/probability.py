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

    def __exit__(self, *args):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)

    def add(self, x):
        self.data.append(x)

    def mean(self):
        if self.data:
            return sum(self.data) / len(self.data)
        else:
            return None

    def variance(self):
        if self.data:
            mean_vale = self.mean()
            return sum((x - mean_vale) ** 2 for x in self.data) / len(self.data)
        else:
            return None
