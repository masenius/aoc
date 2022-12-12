import os
from io import StringIO

import numpy as np
import pytest

from helpers.timing import timing

day = os.path.basename(__file__).split(".")[0]


@timing
def parse(file: str):
    return np.array(
        [
            np.genfromtxt(StringIO(elf), delimiter="\n").sum()
            for elf in open(file).read().split("\n\n")
        ]
    )


@timing
def p1(data):
    return data.max()


@timing
def p2(data):
    return np.sort(data)[-3:].sum()


@pytest.fixture
def test_data():
    return parse(f"inputs/{day}.input.test")


def test_p1(test_data):
    assert p1(test_data) == 24000


def test_p2(test_data):
    assert p2(test_data) == 45000


def main():
    input_file = f"inputs/{day}.input"

    data = parse(input_file)

    print(
        f"P1: {p1(data)} | "
        f"P2: {p2(data)}"
    )


if __name__ == "__main__":
    main()
