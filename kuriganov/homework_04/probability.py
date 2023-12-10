import json


class ProbabilityMoments:
    def __init__(self, filename):
        self.filename = filename
        self.data = {"values": []}

    def __enter__(self):
        try:
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            pass
        return self

    def __exit__(self, *args):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)

    def add(self, x):
        self.data["values"].append(x)

    def mean(self):
        values = self.data["values"]
        if values:
            return sum(values) / len(values)
        else:
            return None

    def variance(self):
        values = self.data["values"]
        n = len(values)
        if n > 1:
            mean_value = self.mean()
            return (sum([(x - mean_value) ** 2 for x in values]) / (n))**0.5
        else:
            return None
