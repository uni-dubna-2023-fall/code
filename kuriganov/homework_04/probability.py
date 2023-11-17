import json

class ProbabilityMoments:
    def __init__(self, filename):
        self.filename = filename
        self.data = {'n': 0, 'mean': 0, 'variance': 0, 'sum': 0, 'sum_squares': 0}

    def __enter__(self):
        with open(self.filename, 'r') as file:
            self.data = json.load(file)
        return self

    def __exit__(self, *args):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)

    def add(self, x):
        self.data['n'] += 1
        self.data['sum'] += x
        self.data['sum_squares'] += x ** 2

    def mean(self):
        if self.data['n'] != 0:
            return self.data['mean']
        return 0

    def variance(self):
        if self.data['n'] != 0:
            return (self.data['sum_squares'] - (self.data['sum'] ** 2) / self.data['n']) / self.data['n']
        return 0
