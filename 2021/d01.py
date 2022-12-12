import pytest


def p1(data):
    return sum(data[i] > data[i - 1] for i in range(1, len(data)))


def p2(data):
    return p1([sum(data[i - 2:i + 1]) for i in range(2, len(data))])


@pytest.fixture
def test_data():
    return [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def test_p1(test_data):
    assert p1(test_data) == 7


def test_p2(test_data):
    assert p2(test_data) == 5


def main():
    with open("inputs/d01.input") as f:
        data = [int(x) for x in f.read().split("\n")]
    print(f"P1: {p1(data)}")
    print(f"P2: {p2(data)}")


if __name__ == "__main__":
    main()
