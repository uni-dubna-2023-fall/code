import json
import math
class ProbabilityMoments:
    def __init__(self, filename):
        self.filename = filename
        with open(filename, 'w') as f:
            f.close()
        pass

    def __enter__(self):
        with open(self.filename, 'r') as file:
            self.file_data = json.load(file)
        return self.file_data

    def __exit__(self, parametr):
        with open(self.filename, 'w') as f:
            json.dump(parametr, f)
        pass

    def add(self, x):
        with open(self.filename, 'a') as f:
            json.dump(x, f)
        pass

    def mean(self):
        res=0
        for i in range(1, len(self.file_data)):
            res += self.file_data[i]
            self.mu = res / len(self.file_data)
        return self.mu

    def variance(self):
        res = 0
        for i in range(1, len(self.file_data)):
            res += ((self.file_data[i] - self.mu) ** 2)
        self.sigma = math.sqrt(res / len(self.file_data))
        return self.sigma