import re

import numpy as np
import pytest
from numpy import array


def parse(input_data: str):
    return np.array([re.findall(r"\d+", line) for line in input_data.split("\n")], dtype=np.int32)


def p1(data: array):
    grid = np.zeros((data.max() + 1, data.max() + 1))
    for x1, y1, x2, y2 in data:
        if x1 == x2 or y1 == y2:
            grid[min(x1, x2):max(x1, x2) + 1, min(y1, y2):max(y1, y2) + 1] += 1
    return (grid > 1).sum()


def p2(data: array):
    grid = np.zeros((data.max() + 1, data.max() + 1))
    for x1, y1, x2, y2 in data:
        if x1 == x2 or y1 == y2:
            grid[min(x1, x2):max(x1, x2) + 1, min(y1, y2):max(y1, y2) + 1] += 1
        else:
            x_range = range(x1, x2 + 1) or range(x1, x2 - 1, -1)
            y_range = range(y1, y2 + 1) or range(y1, y2 - 1, -1)
            for x, y in zip(x_range, y_range):
                grid[x, y] += 1
    return (grid > 1).sum()


@pytest.fixture
def test_data():
    with open("inputs/d05.input.test") as f:
        return parse(f.read())


def test_p1(test_data):
    assert p1(test_data) == 5


def test_p2(test_data):
    assert p2(test_data) == 12


def main():
    with open("inputs/d05.input") as f:
        data = parse(f.read())

    print(f"P1: {p1(data)}")
    print(f"P2: {p2(data)}")


if __name__ == "__main__":
    main()
