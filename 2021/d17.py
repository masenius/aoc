import os
import re
import time
from itertools import product

import pytest

day = os.path.basename(__file__).split(".")[0]


def parse(file: str):
    return [int(val) for val in re.findall(r"-?\d+", open(file).read())]


def p1(data):
    x1, x2, y2, y1 = data
    valids = []
    minx = (x1 + 1) / 2
    maxx = (x2 + 1) / 2
    for ivx, ivy in product(range(minx, maxx), range(1, 1000)):
        vx, vy = ivx, ivy
        x, y = 0, 0
        maxy = 0
        while x <= x2 and y >= y2:
            if y > maxy:
                maxy = y
            if x1 <= x <= x2 and y1 >= y >= y2:
                valids.append(maxy)
                break
            x += vx
            y += vy
            vx -= 1 if vx > 0 else 0
            vy -= 1
    return max(valids)


def p2(data):
    x1, x2, y2, y1 = data
    valids = 0
    minx = int((x1 + 1) / 2)
    maxx = int((x2 + 1) / 2) + 1
    for ivx, ivy in product(range(minx, maxx), range(-1000, 1000)):
        if ivx % 10 == 0:
            print(ivx, ivy)
        vx, vy = ivx, ivy
        x, y = 0, 0
        while x <= x2 and y >= y2:
            if x1 <= x <= x2 and y1 >= y >= y2:
                valids += 1
                break
            x += vx
            y += vy
            vx -= 1 if vx > 0 else 0
            vy -= 1
    return valids


@pytest.fixture
def test_data():
    return parse(f"inputs/{day}.input.test")


def test_p1(test_data):
    assert p1(test_data) == 45


def test_p2(test_data):
    assert p2(test_data) == 112


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
