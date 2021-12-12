import os
import time

import numpy as np
import pytest
from scipy.signal import convolve

day = os.path.basename(__file__).split(".")[0]


def parse(file: str):
    return np.genfromtxt(file, delimiter=1)


def p1(data: np.array):
    mask = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    flashes = 0
    for _ in range(100):
        data += 1
        while (data > 9).any():
            flash = data > 9
            flashes += flash.sum()
            data += convolve(flash, mask, "same")
            data[flash] = -np.inf
        data[data < 0] = 0
    return flashes


def p2(data: np.array):
    mask = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    flashes = 0
    for step in range(1, 1000):
        data += 1
        while (data > 9).any():
            flash = data > 9
            flashes += flash.sum()
            data += convolve(flash, mask, "same")
            data[flash] = -np.inf
        data[data < 0] = 0
        if (data == 0).all():
            return step


@pytest.fixture
def test_data():
    return parse(f"inputs/{day}.input.test")


def test_p1(test_data):
    assert p1(test_data) == 1656


def test_p2(test_data):
    assert p2(test_data) == 195


def main():
    t0 = time.perf_counter()
    print(f"P1: {p1(parse(f'inputs/{day}.input'))} {(time.perf_counter() - t0) * 1000:.2f} ms")
    t0 = time.perf_counter()
    print(f"P2: {p2(parse(f'inputs/{day}.input'))} {(time.perf_counter() - t0) * 1000:.2f} ms")


if __name__ == "__main__":
    main()
