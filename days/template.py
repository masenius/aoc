import os
import time

import pytest

day = os.path.basename(__file__).split(".")[0]


def parse(file: str):
    return 0


def p1(data):
    return 0


def p2(data):
    return 0


@pytest.fixture
def test_data():
    parse(f"inputs/{day}.input.test")


def test_p1(test_data):
    assert p1(test_data) == 1


def test_p2(test_data):
    assert p2(test_data) == 1


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
