import time

import numpy as np
import pytest


def parse(input_data: str):
    return np.array(input_data.split(","), dtype=np.int64)


def p1(data: np.array):
    return np.abs(data - np.median(data)).sum()


def p2(data: np.array):
    return (lambda x: x * (x + 1) / 2)(np.abs(data - np.floor(data.mean()))).sum()


@pytest.fixture
def test_data():
    with open("inputs/d07.input.test") as f:
        return parse(f.read())


def test_p1(test_data):
    assert p1(test_data) == 37


def test_p2(test_data):
    assert p2(test_data) == 168


def main():
    with open("inputs/d07.input") as f:
        data = parse(f.read())

    t0 = time.perf_counter()
    print(f"P1: {p1(data)}. {(time.perf_counter() - t0) * 1000:.2f} ms")
    t0 = time.perf_counter()
    print(f"P2: {p2(data)}. {(time.perf_counter() - t0) * 1000:.2f} ms")


if __name__ == "__main__":
    main()
