import os
import time
from dataclasses import dataclass
from heapq import heappop, heappush
from itertools import product
from typing import List

import numpy as np
import pytest

day = os.path.basename(__file__).split(".")[0]


@dataclass
class Node:
    position: tuple
    g: int = 0
    f: int = 0
    parent: object = None

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f


def search(maze: np.array, start: tuple, end: tuple) -> List:
    start = Node(position=start)
    end = Node(position=end)

    open_nodes = []
    closed_nodes = set()

    heappush(open_nodes, start)

    moves = [[-1, 0], [0, -1], [1, 0], [0, 1]]

    while open_nodes:
        current = heappop(open_nodes)
        closed_nodes.add(current.position)
        maze[current.position[0], current.position[1]] = 0

        if current.position == end.position:
            print(len(closed_nodes))
            return current.g

        children = []
        for move in moves:
            new_position = (current.position[0] + move[0], current.position[1] + move[1])

            if maze[new_position[0], new_position[1]] == 0 or new_position in closed_nodes:
                continue

            children.append(Node(new_position, parent=current))

        for child in children:
            child.g = current.g + maze[child.position[0], child.position[1]]
            child.f = child.g # + (abs(child.position[0] - end.position[0]) + abs(child.position[1] - end.position[1])) * 2

            if child not in open_nodes or child.f < [node for node in open_nodes if node == child][0].f:
                heappush(open_nodes, child)




def parse(file: str):
    return np.genfromtxt(file, delimiter=1, dtype=int)


def p1(maze: np.array):
    padded = np.pad(maze, pad_width=1, mode='constant', constant_values=0)
    return search(padded, (1, 1), (padded.shape[0] - 2, padded.shape[1] - 2))


def p2(maze: np.array):
    expanded_maze = np.zeros((maze.shape[0] * 5, maze.shape[1] * 5))
    for x, y in product(range(5), range(5)):
        m = maze + x + y
        m[m > 9] %= 9
        expanded_maze[x * maze.shape[0]:(x + 1) * maze.shape[0], y * maze.shape[1]:(y+1) * maze.shape[1]] = m
    expanded_maze = np.pad(expanded_maze, pad_width=1, mode="constant", constant_values=0)
    return search(expanded_maze, (1, 1), (expanded_maze.shape[0] - 2, expanded_maze.shape[1] - 2))


@pytest.fixture
def test_data():
    return parse(f"inputs/{day}.input.test")


def test_p1(test_data):
    assert p1(test_data) == 40


def test_p2(test_data):
    assert p2(test_data) == 315


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
