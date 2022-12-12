from dataclasses import dataclass
from queue import PriorityQueue
from typing import List

import numpy as np


@dataclass
class Node:
    position: tuple
    parent: object = None
    g: int = 0
    h: int = 0

    def __lt__(self, other):
        return self.g < other.g or self.h < other.h


def get_path(node: Node) -> List:
    path = []
    current = node
    while current is not None:
        path.append(current.position)
        current = current.parent
    return path[::-1]


def search(maze: np.array, start: tuple, end: tuple) -> List:
    start = Node(position=start)
    end = Node(position=end)

    open_nodes = PriorityQueue()
    visited = []

    open_nodes.put(start)

    moves = [[-1, 0], [0, -1], [1, 0], [0, 1]]

    while not open_nodes.empty():
        current = open_nodes.get()
        visited.append(current.position)

        if current.position == end.position:
            return get_path(current)

        children = []
        for move in moves:
            new_position = (current.position[0] + move[0], current.position[1] + move[1])

            if maze[new_position[0], new_position[1]] == 1 or new_position in visited:
                continue

            children.append(Node(new_position, parent=current))

        for child in children:
            child.g = current.g + 1
            child.h = abs(child.position[0] - end.position[0]) + abs(child.position[1] - end.position[1])

            existing = [open_nodes.queue[i] for i in range(open_nodes.qsize()) if open_nodes.queue[i].position == child.position]
            if existing and existing[0].g < child.g:
                continue

            open_nodes.put(child)


def main():
    maze = np.array([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 0, 0, 0, 0, 1, 1],
        [1, 0, 1, 0, 0, 1, 1, 0, 1, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
        [1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ])
    result = search(maze, (1, 1), (8, 8))
    print(result)


if __name__ == "__main__":
    main()
