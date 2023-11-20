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
            pass
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
            None

    def variance(self):
        mu = self.mean()
        if self.data:
            return (sum((x - mu) ** 2 for x in self.data)) / len(self.data)
        else:
            None
