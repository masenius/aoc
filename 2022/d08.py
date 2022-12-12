import os
from pathlib import Path

import numpy as np
import pytest

from helpers.timing import timing

day = os.path.basename(__file__).split(".")[0]


@timing
def parse(file: Path):
    return np.genfromtxt(file.open(), delimiter=1, dtype=int)


@timing
def p1(data: np.ndarray):
    result = np.zeros_like(data, int)
    for _ in range(4):
        for x, y in np.ndindex(data.shape):
            lower = [tree < data[x, y] for tree in data[x, y + 1:]]
            result[x, y] |= all(lower)
        data, result = map(np.rot90, (data, result))
    return result.sum()


def score(array: list, value) -> int:
    try:
        return array.index(value) + 1
    except ValueError:
        return len(array)


@timing
def p2(data):
    result = np.ones_like(data, int)
    for _ in range(4):
        for x, y in np.ndindex(data.shape):
            lower = [tree < data[x, y] for tree in data[x, y + 1:]]
            result[x, y] *= score(lower, False)
        data, result = map(np.rot90, (data, result))
    return result.max()


@pytest.fixture
def test_data():
    return parse(Path(f"inputs/{day}.input.test"))


def test_p1(test_data):
    assert p1(test_data) == 21


def test_p2(test_data):
    assert p2(test_data) == 8


def main():
    data = parse(Path(f"inputs/{day}.input"))
    print(f"P1: {p1(data)}\nP2: {p2(data)}")


if __name__ == "__main__":
    main()
