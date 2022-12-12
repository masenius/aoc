import time

import numpy as np
import pytest

day = 10


def parse(input_data: str):
    return np.array([list(row) for row in input_data.split("\n")])


closing_lookup = {")": "(", "]": "[", "}": "{", ">": "<"}


def p1(data):
    score = {")": 3, "]": 57, "}": 1197, ">": 25137}
    illegals = []
    for row in data:
        stack = []
        for bracket in row:
            if bracket in "[{(<":
                stack.append(bracket)
            elif closing_lookup[bracket] == stack[-1]:
                stack.pop(-1)
            else:
                illegals.append(bracket)
                break
    return sum([score[x] for x in illegals])


def p2(data):
    score = {"(": 1, "[": 2, "{": 3, "<": 4}
    legals = []
    for row in data:
        stack = []
        for bracket in row:
            if bracket in "[{(<":
                stack.append(bracket)
            elif closing_lookup[bracket] == stack[-1]:
                stack.pop(-1)
            else:
                break
        else:
            total_score = 0
            for x in stack[::-1]:
                total_score = total_score * 5 + score[x]
            legals.append(total_score)
    return sorted(legals)[len(legals) // 2]


@pytest.fixture
def test_data():
    with open(f"inputs/d{day}.input.test") as f:
        return parse(f.read())


def test_p1(test_data):
    assert p1(test_data) == 26397


def test_p2(test_data):
    assert p2(test_data) == 288957


def main():
    with open(f"inputs/d{day}.input") as f:
        data = parse(f.read())

    t0 = time.perf_counter()
    print(f"P1: {p1(data)} {(time.perf_counter() - t0) * 1000:.2f} ms")
    t0 = time.perf_counter()
    print(f"P2: {p2(data)} {(time.perf_counter() - t0) * 1000:.2f} ms")


if __name__ == "__main__":
    main()
