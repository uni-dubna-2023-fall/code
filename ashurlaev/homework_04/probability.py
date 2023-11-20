import json
import os


class ProbabilityMoments:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []

    def __enter__(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file_handle:
                self.data = json.load(file_handle)
        return self

    def __exit__(self, *exc_info):
        with open(self.file_path, 'w') as file_handle:
            json.dump(self.data, file_handle)

    def append_data(self, new_data):
        self.data.append(new_data)

    def calculate_mean(self):
        if self.data:
            total_sum = sum(self.data)
            num_points = len(self.data)
            return total_sum / num_points
        else:
            return None

    def calculate_std_dev(self):
        if len(self.data) >= 2:
            mean_value = self.calculate_mean()
            var_sum = sum((point - mean_value) ** 2 for point in self.data)
            return (var_sum / len(self.data)) ** 0.5
        else:
            return 0
