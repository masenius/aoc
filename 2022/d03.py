import os
from itertools import chain
from pathlib import Path

import pytest

from helpers.timing import timing

day = os.path.basename(__file__).split(".")[0]


@timing
def parse(file: str):
    return Path(file).open().read().split("\n")


def score(ch: str):
    return ord(ch) - 96 if ch.islower() else ord(ch) - 38


@timing
def p1(data):
    return sum(
        score(char)
        for char in chain.from_iterable(
            set(row[: len(row) // 2]) & set(row[len(row) // 2 :])
            for row in data
        )
    )


@timing
def p2(data):
    return sum(
        score(char)
        for char in chain.from_iterable(
            set(data[idx]) & set(data[idx + 1]) & set(data[idx + 2])
            for idx in range(0, len(data), 3)
        )
    )


@pytest.fixture
def test_data():
    return parse(f"inputs/{day}.input.test")


def test_p1(test_data):
    assert p1(test_data) == 157


def test_p2(test_data):
    assert p2(test_data) == 70


def main():
    input_file = f"inputs/{day}.input"

    data = parse(input_file)

    print(f"P1: {p1(data)} | " f"P2: {p2(data)}")


if __name__ == "__main__":
    main()
