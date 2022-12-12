import os
from io import StringIO
from pathlib import Path

import numpy as np
import pytest

from helpers.timing import timing

day = os.path.basename(__file__).split(".")[0]


@timing
def parse(file: Path):
    return np.genfromtxt(StringIO(file.open().read().replace("-", ",")), delimiter=",", dtype=int)


@timing
def p1(data):
    full_overlaps = 0
    for row in data:
        intersection = set(range(row[0], row[1] + 1)) & set(range(row[2], row[3] + 1))
        if len(intersection) == row[1] - row[0] + 1 or len(intersection) == row[3] - row[2] + 1:
            full_overlaps += 1
    return full_overlaps


@timing
def p2(data):
    full_overlaps = 0
    for row in data:
        intersection = set(range(row[0], row[1] + 1)) & set(range(row[2], row[3] + 1))
        if intersection:
            full_overlaps += 1
    return full_overlaps


@pytest.fixture
def test_data():
    return parse(Path(f"inputs/{day}.input.test"))


def test_p1(test_data):
    assert p1(test_data) == 2


def test_p2(test_data):
    assert p2(test_data) == 4


def main():
    input_file = Path(f"inputs/{day}.input")

    data = parse(input_file)

    print(
        f"P1: {p1(data)} | "
        f"P2: {p2(data)}"
    )


if __name__ == "__main__":
    main()
