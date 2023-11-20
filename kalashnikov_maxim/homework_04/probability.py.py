import json

class ProbabilityMoments:
    def __init__(self, filename):
        """Конструктор принимает в качестве аргумента имя файла в котором сохраняются некоторые параметры случайной величины.
        Вам нужно самим решить, что именно сохранять и в каком формате.
        """
        self.ms = []
        self.fp = None
        self.state = "closed"
        self.name = filename

    def __enter__(self):
        """При вызве этого метода, нужно вычитывать параметры из файла, заданного в конструкторе.
        """
        self.fp = open(self.name)
        self.state = "open"
        return self

    def __exit__(self, *args):
        """При вызове этого метода, нужно сохранять параметры в файл.
        """
        self.state = "closed"
        self.fp.close()

    def add(self, x):
        """Добавить новое значение случайной величины к выборке.
        """
        self.ms.append(x['data'])

    def mean(self):
        """Вернуть среднее значение случайной величины на текущий момент.
        """
        self.average = sum(self.ms) / len(self.ms)
        return self.average

    def variance(self):
        """Вернуть дисперсию случайной величины на текущий момент.
        """
        s = sum([(x - self.average)**2 for x in self.ms]) / len(self.ms)
        return s**0.5


    def __str__(self):
        return f'{self.ms}'



with ProbabilityMoments("distribution.json") as pm:
    data = json.load(pm.fp)['ctRoot']
    for x in data:
        pm.add(x)
    print(pm.mean())
    print(pm.variance())
