import numpy as np
import pytest
from bitstring import Bits


def parse(input_data):
    return np.array([[int(x) for x in row] for row in input_data.strip().split("\n")])


def p1(data):
    gamma = [int((data[:, col] == 0).sum() > (data[:, col] == 1).sum()) for col in range(data[0, :].size)]
    epsilon = [(data[:, col] == 0).sum() < (data[:, col] == 1).sum() for col in range(data[0, :].size)]
    return Bits(gamma).uint * Bits(epsilon).uint


def p2(data):
    oxy, co2 = data, data
    for col in range(data[0, :].size):
        if oxy.shape[0] > 1:
            oxy = oxy[oxy[:, col] == int((oxy[:, col] == 0).sum() <= (oxy[:, col] == 1).sum())]
        if co2.shape[0] > 1:
            co2 = co2[co2[:, col] == int((co2[:, col] == 0).sum() > (co2[:, col] == 1).sum())]
    return Bits(oxy[0]).uint * Bits(co2[0]).uint


@pytest.fixture
def test_data():
    input_data = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""
    return parse(input_data)


def test_p1(test_data):
    assert p1(test_data) == 198


def test_p2(test_data):
    assert p2(test_data) == 230


def main():
    with open("inputs/d03.input") as f:
        data = parse(f.read())

    print(f"P1: {p1(data)}")
    print(f"P2: {p2(data)}")


if __name__ == "__main__":
    main()
