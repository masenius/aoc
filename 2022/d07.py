from __future__ import annotations

import os
from dataclasses import dataclass
from math import inf
from pathlib import Path

import pytest

from helpers.timing import timing

day = os.path.basename(__file__).split(".")[0]


@timing
def parse(file: Path):
    return file.open().read().split("\n")


@dataclass
class File:
    name: list[str]
    parent: File | None
    children: dict | None = None
    size: int = 0


def get_sizes(file: File, sizes: list, limit: int = inf) -> int:
    if file.size:
        return file.size

    child_sizes = [get_sizes(child, sizes, limit=limit) for child in file.children.values()]

    size = sum(child_sizes)
    if size <= limit:
        sizes.append(size)

    return size


def generate_filesystem(data: list[str]):
    root = File(name=["/"], parent=None, children={})
    pwd = root

    for row in data:
        if row.startswith("$"):
            command, *args = row.split()[1:]
            if command == "cd":
                match args[0]:
                    case "..":
                        pwd = pwd.parent
                    case "/":
                        pwd = root
                    case _:
                        pwd = pwd.children.get(args[0])

            if command[0] == "ls":
                ...

        else:
            x, name = row.split()
            match x:
                case "dir":
                    pwd.children[name] = File(name=pwd.name + [name], parent=pwd, children={})
                case _:
                    pwd.children[name] = File(name=pwd.name + [name], parent=pwd, size=int(x))
    return root


@timing
def p1(data: list[str]):
    root = generate_filesystem(data)
    sizes = []
    get_sizes(root, sizes, limit=100_000)
    return sum(sizes)


@timing
def p2(data):
    root = generate_filesystem(data)
    sizes = []
    root_size = get_sizes(root, sizes)
    available_space = 70_000_000 - root_size
    for size in sorted(sizes):
        if available_space + size > 30_000_000:
            return size


@pytest.fixture
def test_data():
    return parse(Path(f"inputs/{day}.input.test"))


def test_p1(test_data):
    assert p1(test_data) == 95437


def test_p2(test_data):
    assert p2(test_data) == 24933642


def main():
    data = parse(Path(f"inputs/{day}.input"))
    print(f"P1: {p1(data)}\nP2: {p2(data)}")


if __name__ == "__main__":
    main()
