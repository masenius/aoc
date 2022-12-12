import pytest
from days.d18 import parse, magnitude, explode, p1, p2, split

tc_magnitude = [
    ([9, 1], 29),
    ([1, 9], 21),
    ([[9, 1], [1, 9]], 129),
    ([[1, 2], [[3, 4], 5]], 143),
    ([[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]], 1384),
    ([[[[1, 1], [2, 2]], [3, 3]], [4, 4]], 445),
    ([[[[3, 0], [5, 3]], [4, 4]], [5, 5]], 791),
    ([[[[5, 0], [7, 4]], [5, 5]], [6, 6]], 1137),
    ([[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]], 3488),
]


@pytest.mark.parametrize("magnitude_case", tc_magnitude)
def test_magnitude(magnitude_case):
    assert magnitude(magnitude_case[0]) == magnitude_case[1]


tc_explode = [
    ([[[[[9, 8], 1], 2], 3], 4], [[[[0, 9], 2], 3], 4]),
    ([7, [6, [5, [4, [3, 2]]]]], [7, [6, [5, [7, 0]]]]),
    ([[6, [5, [4, [3, 2]]]], 1], [[6, [5, [7, 0]]], 3]),
    ([[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]], [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]]),
    ([[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]], [[3, [2, [8, 0]]], [9, [5, [7, 0]]]]),
]


@pytest.mark.parametrize("explode_case", tc_explode)
def test_explode(explode_case):
    s, r = explode_case
    assert explode(s)
    assert s == r


tc_split = [
    ([[[[0, 7], 4], [15, [0, 13]]], [1, 1]], [[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]]),
    ([[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]], [[[[0, 7], 4], [[7, 8], [0, [6, 7]]]], [1, 1]]),
]


@pytest.mark.parametrize("split_case", tc_split)
def test_split(split_case):
    s, r = split_case
    assert split(s)
    assert s == r


@pytest.fixture
def test_data():
    return parse(f"inputs/d18.input.test")


def test_p1(test_data):
    assert p1(test_data) == 4140


def test_p2(test_data):
    assert p2(test_data) == 3993
