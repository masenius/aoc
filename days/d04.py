import numpy as np
import pytest


def parse(input_data):
    c, *b = input_data.split("\n\n")
    calls = np.array(c.split(","), dtype=int)
    boards = np.array([[row.split() for row in board.split("\n")] for board in b], dtype=int)
    return calls, boards


def p1(calls, boards):
    for call in calls:
        for b in boards:
            b[b == call] = -1
            if (b.sum(axis=0) == -5).any() or (b.sum(axis=1) == -5).any():
                return b[b != -1].sum() * call


def p2(calls, boards):
    winners = {}
    for call in calls:
        for idx, b in enumerate(boards):
            if idx not in winners.keys():
                b[b == call] = -1
                if (b.sum(axis=0) == -5).any() or (b.sum(axis=1) == -5).any():
                    winners[idx] = b[b != -1].sum() * call
    return list(winners.values())[-1]


@pytest.fixture
def test_data():
    with open("inputs/d04.input.test") as f:
        return parse(f.read())


def test_p1(test_data):
    calls, boards = test_data
    assert p1(calls, boards) == 4512


def test_p2(test_data):
    calls, boards = test_data
    assert p2(calls, boards) == 1924


def main():
    with open("inputs/d04.input") as f:
        calls, boards = parse(f.read())

    print(f"P1: {p1(calls, boards)}")
    print(f"P2: {p2(calls, boards)}")


if __name__ == "__main__":
    main()
