import os.path
import json
import math


class ProbabilityMoments:
    def __init__(self, filename):
        self.filelist = []
        self.file = filename

    def __enter__(self):
        if os.path.isfile(self.file):
            with open(self.file) as f:
                raw = f.read()
                self.filelist = json.loads(raw)
            return self
        else:
            return self

    def __exit__(self, *args):
        with open(self.file, "w") as f:
            raw = json.dumps(self.filelist)
            f.write(raw)

    def add(self, x):
        self.filelist.append(x)

    def mean(self):
        return (sum(self.filelist) / len(self.filelist))

    def variance(self):
        means = sum(self.filelist) / len(self.filelist)
        res = 0
        for i in self.filelist:
            res += (i - means) * (i - means)
        vari = math.sqrt(res / len(self.filelist))
        return vari
