import os
import time
from collections import defaultdict, Counter

import pytest

day = os.path.basename(__file__).split(".")[0]


def parse(file: str):
    graph = defaultdict(set)
    for n1, n2 in [cave.split("-") for cave in open(file).read().split("\n")]:
        if n1 != "end" and n2 != "start":
            graph[n1].add(n2)
        if n1 != "start" and n2 != "end":
            graph[n2].add(n1)
    return graph


def dfs(src: str, dst: str, graph: dict, paths: list, path: list = None, allow_twice=False):
    if path is None:
        path = [src]

    if src == dst:
        paths.append(path)
    else:
        for adjacent in graph[src]:
            twice = 2 not in Counter([cave for cave in path if cave.islower()]).values() if allow_twice else False
            if adjacent.isupper() or twice or adjacent not in path:
                path.append(adjacent)
                dfs(adjacent, dst, graph, paths, path, allow_twice=allow_twice)
                path.pop()


def p1(graph):
    paths = []
    dfs("start", "end", graph, paths)
    return len(paths)


def p2(graph):
    paths = []
    dfs("start", "end", graph, paths, allow_twice=True)
    return len(paths)


cases_p1 = [(f"inputs/{day}.input.test", 10), (f"inputs/{day}.input.test2", 19), (f"inputs/{day}.input.test3", 226)]
cases_p2 = [(f"inputs/{day}.input.test", 36), (f"inputs/{day}.input.test2", 103), (f"inputs/{day}.input.test3", 3509)]


@pytest.mark.parametrize("case", cases_p1)
def test_p1(case):
    file, paths = case
    assert p1(parse(file)) == paths


@pytest.mark.parametrize("case", cases_p2)
def test_p2(case):
    file, paths = case
    assert p2(parse(file)) == paths


def main():
    input_file = f'inputs/{day}.input'

    t0 = time.perf_counter()
    print(
        f"P1: "
        f"{p1(parse(input_file))} "
        f"{(time.perf_counter() - t0) * 1000:.2f} ms"
    )

    t0 = time.perf_counter()
    print(
        f"P2: "
        f"{p2(parse(input_file))} "
        f"{(time.perf_counter() - t0) * 1000:.2f} ms"
    )


if __name__ == "__main__":
    main()
