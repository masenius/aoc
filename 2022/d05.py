import os
import re
from copy import deepcopy
from pathlib import Path

import pandas as pd
import pytest

from helpers.timing import timing

day = os.path.basename(__file__).split(".")[0]


@timing
def parse(file: Path):
    crates, instructions = file.open().read().split("\n\n")
    df = (
        pd.DataFrame(
            [re.findall(r" ?(\[[A-Z]\]| .) ?", row) for row in crates.split("\n")]
        )
        .replace("\[", "", regex=True)
        .replace("\]", "", regex=True)
    )

    stacks = []
    for name, values in df[:-1].items():
        stacks.append([ch for ch in values.iloc[::-1] if ch and ch.isalpha()])

    instructions = [
        [int(x) for x in re.findall("\d+", row)] for row in instructions.split("\n")
    ]

    return stacks, instructions


@timing
def p1(data):
    stacks, instructions = data
    stacks = deepcopy(stacks)
    for instruction in instructions:
        move, from_, to = instruction
        stacks[to - 1].extend(reversed(stacks[from_ - 1][-move:]))
        stacks[from_ - 1] = stacks[from_ - 1][:-move]

    return "".join(stack[-1] for stack in stacks)


@timing
def p2(data):
    stacks, instructions = data
    stacks = deepcopy(stacks)
    for instruction in instructions:
        move, from_, to = instruction
        stacks[to - 1].extend(stacks[from_ - 1][-move:])
        stacks[from_ - 1] = stacks[from_ - 1][:-move]

    return "".join(stack[-1] for stack in stacks)


@pytest.fixture
def test_data():
    return parse(Path(f"inputs/{day}.input.test"))


def test_p1(test_data):
    assert p1(test_data) == "CMZ"


def test_p2(test_data):
    assert p2(test_data) == "MCD"


def main():
    data = parse(Path(f"inputs/{day}.input"))
    print(f"P1: {p1(data)}\nP2: {p2(data)}")


if __name__ == "__main__":
    main()
