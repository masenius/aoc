import time

import numpy as np
import pytest


def parse(input_data: str):
    return np.array([[int(x) for x in input_data.split(",")].count(i) for i in range(9)], dtype=np.int64)


def calc_growth(population: np.array, generations: int):
    for day in range(generations):
        population = np.roll(population, -1)
        population[6] += population[8]
    return population.sum()


def p1(data):
    return calc_growth(population=data, generations=80)


def p2(data):
    return calc_growth(population=data, generations=256)


@pytest.fixture
def test_data():
    with open("inputs/d06.input.test") as f:
        return parse(f.read())


def test_p1(test_data):
    assert p1(test_data) == 5934


def test_p2(test_data):
    assert p2(test_data) == 26984457539


def main():
    with open("inputs/d06.input") as f:
        data = parse(f.read())
    t0 = time.perf_counter()
    print(f"P1: {p1(data)}. {(time.perf_counter() - t0) * 1000:.2f} ms")
    print(f"P2: {p2(data)}. {(time.perf_counter() - t0) * 1000:.2f} ms")


if __name__ == "__main__":
    main()
