import json
import os


class ProbabilityMoments:
    def __init__(self, fn):
        self.fn = fn
        self.data = []

    def __enter__(self):
        if os.path.exists(self.fn):
            with open(self.fn, 'r') as file:
                self.data = json.load(file)
        return self

    def __exit__(self, *exc_info):
        with open(self.fn, 'w') as file:
            json.dump(self.data, file)

    def append(self, new_data):
        self.data.append(new_data)

    def calculate(self):
        if self.data:
            return  sum(self.data) / len(self.data)
        else:
            None

    def calculate(self):
        if len(self.data) >= 2:
            mean_value = self.calculate()
            summa = sum((h - mean_value) ** 2 for h in self.data)
            return ((summa / len(self.data)) ** 0.5)
        else:
            return 0
