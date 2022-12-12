import os
from pathlib import Path

import pytest

from helpers.timing import timing

day = os.path.basename(__file__).split(".")[0]


@timing
def parse(file: Path):
    return 0


@timing
def p1(data):
    return 0


@timing
def p2(data):
    return 0


@pytest.fixture
def test_data():
    return parse(Path(f"inputs/{day}.input.test"))


def test_p1(test_data):
    assert p1(test_data) == 1


def test_p2(test_data):
    assert p2(test_data) == 1


def main():
    data = parse(Path(f"inputs/{day}.input"))
    print(f"P1: {p1(data)}\nP2: {p2(data)}")


if __name__ == "__main__":
    main()
