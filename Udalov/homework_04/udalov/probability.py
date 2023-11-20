import json
import math


class ProbabilityMoments:
    def __init__(self, filename):

        self.filename = filename

    def __enter__(self):
        with open(self.filename, 'r') as file:
            self.file_data = json.load(file)
        return self.file_data

    def __exit__(self, parametr):
        with open(self.filename, 'w') as f:
            json.dump(parametr, f)

    def add(self, x):
        self.file_data += x

    def mean(self):
        res = 0
        mu = 0
        for i in range(1, len(self.file_data)):
            res += self.file_data[i]
            mu = res / len(self.file_data)
        return mu

    def variance(self):
        res = 0
        sigma = 0
        for i in range(1, len(self.file_data)):
            res += ((self.file_data[i] - self.mean(self)) ** 2)
        sigma = math.sqrt(res / len(self.file_data))
        return sigma
