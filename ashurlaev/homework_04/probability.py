import json
import os


class ProbabilityMoments:
    def __init__(self, filename):
        self.filename = filename
        self.data = []

    def __enter__(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                params = json.load(f)
            self.data = params['data']
        return self

    def __exit__(self, *args):
        params = {'data': self.data}
        with open(self.filename, 'w') as f:
            json.dump(params, f)

    def add(self, x):
        self.data.append(x)

    def mean(self):
        return sum(self.data) / len(self.data)

    def variance(self):
        mean = self.mean()
        summa = [(x - mean)**2 for x in self.data]
        return ((sum(summa) / len(self.data)) ** 0.5)
