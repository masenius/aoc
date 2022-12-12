import pytest


def parse(input_data):
    data = []
    for row in input_data.split("\n"):
        command, value = row.split()
        match command:
            case "forward":
                data.append((int(value), 0))
            case "up":
                data.append((0, -int(value)))
            case "down":
                data.append((0, int(value)))
    return data


def p1(data):
    total = (0, 0)
    for coordinate in data:
        total = tuple(map(sum, zip(coordinate, total)))
    return total[0] * total[1]


def p2(data):
    x, y, aim = 0, 0, 0
    for coordinate in data:
        forward, change = coordinate
        x += forward
        y += aim * forward
        aim += change

    return x * y


@pytest.fixture
def test_data():
    input_data = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""
    return parse(input_data)


def test_p1(test_data):
    assert p1(test_data) == 150


def test_p2(test_data):
    assert p2(test_data) == 900


def main():
    with open("inputs/d02.input") as f:
        data = parse(f.read())

    print(f"P1: {p1(data)}")
    print(f"P2: {p2(data)}")


if __name__ == "__main__":
    main()
