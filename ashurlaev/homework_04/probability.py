import json
import os


class ProbabilityMoments:
    def __init__(self, path):
        self.path = path
        self.numbers = []

    def __enter__(self):
        if os.path.isfile(self.path):
            with open(self.path, 'r') as f:
                self.numbers = json.load(f)
        return self

    def __exit__(self, *exc):
        with open(self.path, 'w') as f:
            json.dump(self.numbers, f)

    def insert(self, value):
        self.numbers.append(value)

    def average(self):
        if self.numbers:
            return sum(self.numbers) / len(self.numbers)
        return None

    def deviation(self):
        if len(self.numbers) >= 2:
            avg = self.average()
            return (sum((n - avg) ** 2 for n in self.numbers) 
                    / len(self.numbers)) ** 0.5
        return 0
