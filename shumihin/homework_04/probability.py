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
        if not self.data:
            return None
        sum = 0
        for i in self.data:
            sum += i
            answer = sum / len(self.data)
        return answer

    def variance(self):
        if len(self.data) < 2:
            return 0
        mean_val = self.mean()
        sum = 0
        for x in self.data:
            sum += (x - mean_val) ** 2
        answer = (sum / len(self.data)) ** 0.5
        return answer
