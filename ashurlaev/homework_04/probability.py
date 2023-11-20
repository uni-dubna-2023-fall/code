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
        with open(self.fn, 'w') as file
            json.dump(self.data, file)

    def append_data(self, new_data):
        self.data.append(new_data)

    def calculate_mean(self):
        if not self.data:
           return None
        else:
            total_sum = sum(self.data)
            num_points = len(self.data)
            return total_sum / num_points
            

    def calculate_std_dev(self):
        if len(self.data) >= 2:
            mean_value = self.calculate_mean()
            sum = sum((point - mean_value) ** 2 for point in self.data)
            return ((sum / len(self.data))** 0.5)
        else:
            return 0
