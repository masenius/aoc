import os
import time
from collections import defaultdict
from itertools import pairwise

import pytest

day = os.path.basename(__file__).split(".")[0]


def parse(file: str):
    template, _, *insertions = open(file).read().split("\n")
    insertions = dict(insertion.split(" -> ") for insertion in insertions)
    return template, insertions


def solve(template, insertions, rounds):
    total = defaultdict(int)
    count = {key: 0 for key in insertions.keys()}
    for c1, c2 in pairwise(list(template)):
        count[f"{c1}{c2}"] += 1
        total[c1] += 1
        total[c2] += 1
    for _ in range(rounds):
        for k, v in count.copy().items():
            c1, c2 = list(k)
            count[k] -= v
            count[f"{c1}{insertions[k]}"] += v
            count[f"{insertions[k]}{c2}"] += v
            total[insertions[k]] += v
    return max(total.values()) - min(total.values())


def p1(template: str, insertions: dict):
    return solve(template, insertions, 10)


def p2(template: str, insertions: dict):
    return solve(template, insertions, 40)


@pytest.fixture
def test_data():
    return parse(f"inputs/{day}.input.test")


def test_p1(test_data):
    template, insertions = test_data
    assert p1(template, insertions) == 1588


def test_p2(test_data):
    template, insertions = test_data
    assert p2(template, insertions) == 2188189693529


def main():
    input_file = f'inputs/{day}.input'
    template, insertions = parse(input_file)

    t0 = time.perf_counter()
    print(
        f"P1: "
        f"{p1(template, insertions)} "
        f"{(time.perf_counter() - t0) * 1000:.2f} ms"
    )

    t0 = time.perf_counter()
    print(
        f"P2: "
        f"{p2(template, insertions)} "
        f"{(time.perf_counter() - t0) * 1000:.2f} ms"
    )


if __name__ == "__main__":
    main()
