import logging
from numpy import random
import os.path
import os
import math


def test_complex_number(iter_homework):
    for p, m in iter_homework(4, "complex"):
        logging.info("Test ComplexNumber for %s", p)
        init_list = [
            (2.0, -2.0),
            (-3.0, -1.0),
            (1.0, 2.0),
            (-3.0, 1.0),
            (-1.0, 1.0),
        ]
        c = [m.ComplexNumber(*n) for n in init_list]
        cc = [complex(*n) for n in init_list]
        result = c[0] + c[1] - c[2] * c[3] / c[4]
        expected = cc[0] + cc[1] - cc[2] * cc[3] / cc[4]
        assert result.x == expected.real
        assert result.y == expected.imag
        assert str(result) == f"({expected.real}, {expected.imag})"


def test_probability_moments(iter_homework):
    for p, m in iter_homework(4, "probability"):
        logging.info("Test ProbabilityMoments for %s", p)
        interval1 = 0.02
        interval2 = 0.015
        mean = 1.0
        variance = 0.2
        x1 = random.normal(loc=mean, scale=variance, size=500)
        x2 = random.normal(loc=mean, scale=variance, size=500)
        filename = "/tmp/test_probability.json"
        if os.path.isfile(filename):
            os.unlink(filename)
        with m.ProbabilityMoments(filename) as pm:
            for xi1 in x1:
                pm.add(xi1)
        assert mean - interval1 < pm.mean() < mean + interval1
        assert variance - interval1 < pm.variance() < variance + interval1
        with m.ProbabilityMoments(filename) as pm:
            for xi2 in x2:
                pm.add(xi2)
        assert mean - interval2 < pm.mean() < mean + interval2
        assert variance - interval2 < pm.variance() < variance + interval2


def test_coordinates(iter_homework):
    def func(*points):
        return list(points)

    test_points = [(10.0, -10.0), (-10.0, 10.0), (-10.0, -10.0)]
    for p, m in iter_homework(4, "coordinates"):
        logging.info("Test coordinates for %s", p)
        newfunc = m.shift(1.0, 10.0)(func)
        assert newfunc(*test_points) == [
            (p[0] + 1.0, p[1] + 10.0) for p in test_points
        ]

        newfunc = m.reflect(func)
        assert newfunc(*test_points) == [(-p[0], -p[1]) for p in test_points]

        angleg = 45.0
        matrix = [
            [1.0 / math.sqrt(2.0), -1.0 / math.sqrt(2.0)],
            [1.0 / math.sqrt(2.0), 1.0 / math.sqrt(2.0)],
        ]

        newfunc = m.rotate(angleg)(func)
        rotated_points = []
        for point in test_points:
            rotated_points.append(
                (
                    sum([round(matrix[0][i] * point[i], 2) for i in range(2)]),
                    sum([round(matrix[1][i] * point[i], 2) for i in range(2)]),
                )
            )

        result = [
            (round(p[0], 2), round(p[1], 2)) for p in newfunc(*test_points)
        ]
        assert result == rotated_points
