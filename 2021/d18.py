import ast
import os
import time
from typing import List

day = os.path.basename(__file__).split(".")[0]


def parse(file: str):
    return [ast.literal_eval(item) for item in open(file).read().split("\n")]


def magnitude(s):
    if isinstance(s, int):
        return s
    return magnitude(s[0]) * 3 + magnitude(s[-1]) * 2


def add_to_right(s, addition):
    if isinstance(s, int):
        return s + addition
    return [s[0], add_to_right(s[1], addition)]


def add_to_left(s, addition):
    if isinstance(s, int):
        return s + addition
    return [add_to_left(s[0], addition), s[1]]


def explode(s: List, depth: int = 1, lr: List = None):
    for idx, item in enumerate(s):
        if isinstance(item, int):
            return False
        if depth < 4:
            lr_ = []
            if explode(item, depth + 1, lr_):
                return True
            return False
        lr[0], lr[1] = item
        s[idx] = 0
        if idx:
            s[0] += lr[0]
        else:
            s[1] += lr[1]
        return True


def explode_(s, d=0):
    if isinstance(s, int):
        return False, s, 0, 0
    if d < 4:
        exploded, next_num, left, right = explode(s[0], d + 1)
        if exploded:
            s = [next_num, add_to_left(s[1], right)]
            return True, s, left, 0
        exploded, next_num, left, right = explode(s[1], d + 1)
        if exploded:
            s = [add_to_right(s[0], left), next_num]
            return True, s, 0, right
        return False, s, 0, 0
    else:
        return True, 0, s[0], s[1]


def split(s: List) -> bool:
    for idx, item in enumerate(s):
        if isinstance(item, int):
            if item >= 10:
                s[idx] = [item // 2, (item + 1) // 2]
                return True
        else:
            if split(s[idx]):
                return True
    return False


def add(a, b):
    s = [a, b]
    while True:
        exploded, s, _, _ = explode(s)
        if not exploded:
            if not split(s):
                break
    return s


def p1(data):
    s = data[0]
    for i in range(1, len(data)):
        s = add(s, data[i])
    return magnitude(s)


def p2(data):
    max_s = 0
    for a in data:
        for b in data:
            if a != b:
                c = add(a, b)
                s = magnitude(c)
                if s > max_s:
                    max_s = s
    return max_s


def main():
    input_file = f"inputs/{day}.input"

    t0 = time.perf_counter()
    data = parse(input_file)
    print(f"P1: " f"{p1(data)} " f"{(time.perf_counter() - t0) * 1000:.2f} ms")

    t0 = time.perf_counter()
    data = parse(input_file)
    print(f"P2: " f"{p2(data)} " f"{(time.perf_counter() - t0) * 1000:.2f} ms")


if __name__ == "__main__":
    main()
