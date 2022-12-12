import os
from pathlib import Path

from helpers.timing import timing

day = os.path.basename(__file__).split(".")[0]


@timing
def p1(data):
    for idx, _ in enumerate(data):
        if len(set(data[idx:idx + 4])) == 4:
            return idx + 4


@timing
def p2(data):
    for idx, _ in enumerate(data):
        if len(set(data[idx:idx + 14])) == 14:
            return idx + 14


def test_p1():
    assert p1("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
    assert p1("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert p1("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert p1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert p1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11


def test_p2():
    assert p2("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
    assert p2("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
    assert p2("nppdvjthqldpwncqszvftbrmjlhg") == 23
    assert p2("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
    assert p2("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26


def main():
    data = Path(f"inputs/{day}.input").open().read().strip()
    print(f"P1: {p1(data)}\nP2: {p2(data)}")


if __name__ == "__main__":
    main()
