import os
import time
from io import StringIO
from itertools import combinations
from math import dist

import numpy as np
import pytest

day = os.path.basename(__file__).split(".")[0]


def parse(file: str):
    scanners = []
    for s in open(file).read().split("\n\n"):
        _, *beacons = s.split("\n")
        scanners.append([np.genfromtxt(StringIO(beacon), delimiter=",", dtype=np.int) for beacon in beacons])
    return scanners


def p1(data):
    beacon_distances = []
    for scanner in data:
        distances = set()
        for s1, s2 in combinations(scanner, 2):
            distances.add(dist(s1, s2))
        beacon_distances.append(distances)

    for s1, s2 in combinations(beacon_distances, 2):
        overlapping_beacons = s1.intersection(s2)
        if len(overlapping_beacons) >= 12:
            bp = 1


    return 0


def p2(data):
    return 0


@pytest.fixture
def test_data():
    return parse(f"inputs/{day}.input.test")


def test_p1(test_data):
    assert p1(test_data) == 1


def test_p2(test_data):
    assert p2(test_data) == 1


def main():
    input_file = f'inputs/{day}.input'

    t0 = time.perf_counter()
    data = parse(input_file)
    print(
        f"P1: "
        f"{p1(data)} "
        f"{(time.perf_counter() - t0) * 1000:.2f} ms"
    )

    t0 = time.perf_counter()
    data = parse(input_file)
    print(
        f"P2: "
        f"{p2(data)} "
        f"{(time.perf_counter() - t0) * 1000:.2f} ms"
    )


if __name__ == "__main__":
    main()
