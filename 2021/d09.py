import time
from functools import reduce
from itertools import product

import numpy as np
import pytest


def parse(input_data: str):
    data = np.array([list(row) for row in input_data.split("\n")], dtype=np.int64)
    x, y = data.shape
    outer = np.full((x + 2, y + 2), 9)
    outer[1:x + 1, 1:y + 1] = data
    return outer


def find_minimas(data):
    minimas = []
    for x, y in product(range(1, data.shape[0]), range(1, data.shape[1])):
        if (
            data[x - 1, y] > data[x, y] < data[x + 1, y]
            and data[x, y - 1] > data[x, y] < data[x, y + 1]
        ):
            minimas.append((x, y))
    return minimas


def p1(data):
    return sum([data[x, y] + 1 for x, y in find_minimas(data)])


def count_basin(coord, data, basin=None):
    if basin is None:
        basin = []
    x, y = coord
    basin.append(coord)
    for candidate in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if candidate not in basin and data[candidate[0], candidate[1]] != 9:
            count_basin(candidate, data, basin)
    return basin


def p2(data):
    return reduce(lambda x, y: x * y, [len(count_basin(minima, data)) for minima in find_minimas(data)][-3:])


@pytest.fixture
def test_data():
    with open("inputs/d09.input.test") as f:
        return parse(f.read())


def test_p1(test_data):
    assert p1(test_data) == 15


def test_p2(test_data):
    assert p2(test_data) == 1134


def main():
    with open("inputs/d09.input") as f:
        data = parse(f.read())

    t0 = time.perf_counter()
    print(f"P1: {p1(data)}. {(time.perf_counter() - t0) * 1000:.2f} ms")
    t0 = time.perf_counter()
    print(f"P2: {p2(data)}. {(time.perf_counter() - t0) * 1000:.2f} ms")


if __name__ == "__main__":
    main()
