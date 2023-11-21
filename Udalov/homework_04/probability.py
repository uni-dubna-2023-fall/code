import json
import math


class ProbabilityMoments:
    def __init__(self, filename):
        self.file_data = {'values': []}
        self.filename = filename

    def __enter__(self):
        try:
            with open(self.filename, 'r') as file:
                self.file_data = json.load(file)
        except FileNotFoundError:
            pass
        return self

    def __exit__(self, *args):
        with open(self.filename, 'w') as f:
            json.dump(self.file_data, f)

    def add(self, x):
        self.file_data['values'].append(x)

    def mean(self):
        if self.file_data:
            return sum(self.file_data) / len(self.file_data)
        else:
            return None

    def variance(self):
        if len(self.file_data) < 2:
            return 0
        res = 0
        for i in range(1, len(self.file_data)):
            res += ((self.file_data[i] - self.mean()) ** 2)
        sigma = math.sqrt(res / len(self.file_data))
        return sigma
