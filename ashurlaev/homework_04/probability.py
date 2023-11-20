import json
import os


class AnalyzeData:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data_points = []

    def __enter__(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file_handle:
                self.data_points = json.load(file_handle)
        return self

    def __exit__(self, *exc_info):
        with open(self.file_path, 'w') as file_handle:
            json.dump(self.data_points, file_handle)

    def append_data(self, new_data):
        self.data_points.append(new_data)

    def calculate_mean(self):
        if self.data_points:
            total_sum = sum(self.data_points)
            num_points = len(self.data_points)
            return total_sum / num_points
        else:
            return None

    def calculate_std_dev(self):
        if len(self.data_points) >= 2:
            mean_value = self.calculate_mean()
            var_sum = sum((point - mean_value) ** 2 for point in self.data_points)
            return (var_sum / len(self.data_points)) ** 0.5
        else:
            return 0
