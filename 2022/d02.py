import os
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from helpers.timing import timing

day = os.path.basename(__file__).split(".")[0]


@timing
def parse(file: str):
    return pd.read_csv(Path(file).open(), delimiter=" ", header=None)


@timing
def p1(data):
    df = data.replace(["A", "B", "C", "X", "Y", "Z"], [1, 2, 3, 1, 2, 3])
    df.loc[(df[1] - df[0]) % 3 == 2, 2] = 0
    df.loc[(df[1] - df[0]) % 3 == 0, 2] = 3
    df.loc[(df[1] - df[0]) % 3 == 1, 2] = 6
    return df[[1, 2]].to_numpy().sum()


@timing
def p2(data):
    df = data.replace(["A", "B", "C", "X", "Y", "Z"], [1, 2, 3, 0, 3, 6])
    df.loc[df[1] == 0, 2] = -np.fmod(1 - df[0], 3)
    df.loc[df[1] == 3, 2] = df[0]
    df.loc[df[1] == 6, 2] = -np.fmod(2 - df[0], 3)
    df.loc[df[2] <= 0, 2] = df[2] + 3
    return df[[1, 2]].to_numpy().sum()


@pytest.fixture
def test_data():
    return parse(f"inputs/{day}.input.test")


def test_p1(test_data):
    assert p1(test_data) == 15


def test_p2(test_data):
    assert p2(test_data) == 12


def main():
    input_file = f"inputs/{day}.input"

    data = parse(input_file)

    print(f"P1: {p1(data)}\n" f"P2: {p2(data)}")


if __name__ == "__main__":
    main()
