class ProbabilityMoments:
    def __init__(self, filename):
        self.filename = filename
        self.sum = 0
        self.squared_sum = 0
        self.count = 0


    def __enter__(self):  
        try:
            with open(self.filename, 'r') as f:
                data = f.read().split(',')
                if len(data) == 3:
                    self.sum = float(data[0])
                    self.squared_sum = float(data[1])
                    self.count = int(data[2])
        except FileNotFoundError:
            pass
        return self


    def __exit__(self, *args):
        with open(self.filename, 'w') as f:
            f.write(f"{self.sum},{self.squared_sum},{self.count}")


    def add(self, x):
        self.sum += x
        self.squared_sum += x ** 2
        self.count += 1


    def mean(self):
        if self.count == 0:
            return 0
        return self.sum / self.count


    def variance(self):
        if self.count <= 1:
            return 0
        return (self.squared_sum / self.count) - (self.mean() ** 2)