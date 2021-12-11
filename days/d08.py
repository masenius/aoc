import time

import pytest


def parse(input_data: str):
    data = []
    for row in input_data.split("\n"):
        signals, output = row.split("|")
        data.append([
            signals.strip().split(),
            output.strip().split()
        ])
    return data


def p1(data):
    count = 0
    for signals, outputs in data:
        for output in outputs:
            # 6 2 5 5 4 5 6 3 7 6
            if len(output) in (2, 4, 3, 7):
                count += 1
    return count


def p2(data):
    output_sum = 0
    for signals, outputs in data:
        digits = [None] * 10
        for signal in signals:
            if len(signal) == 2:
                digits[1] = signal
            if len(signal) == 4:
                digits[4] = signal
            if len(signal) == 3:
                digits[7] = signal
            if len(signal) == 7:
                digits[8] = signal
        for signal in signals:
            if len(signal) == 6:
                if len(set(signal).intersection(set(digits[1]))) == 1:
                    digits[6] = signal
                elif len(set(signal).intersection(set(digits[4]))) == 4:
                    digits[9] = signal
                else:
                    digits[0] = signal
        for signal in signals:
            if len(signal) == 5:
                if len(set(signal).intersection(set(digits[1]))) == 2:
                    digits[3] = signal
                elif len(set(signal).intersection(set(digits[1])).intersection(set(digits[6]))) == 1:
                    digits[5] = signal
                else:
                    digits[2] = signal
        mapper = {"".join(sorted(v)): i for i, v in enumerate(digits)}
        num = int("".join([str(mapper["".join(sorted(output))]) for output in outputs]))
        output_sum += num
    return output_sum


@pytest.fixture
def test_data():
    with open("inputs/d08.input.test") as f:
        return parse(f.read())


def test_p1(test_data):
    assert p1(test_data) == 26


def test_p2(test_data):
    assert p2(test_data) == 61229


def main():
    with open("inputs/d08.input") as f:
        data = parse(f.read())

    t0 = time.perf_counter()
    print(f"P1: {p1(data)}. {(time.perf_counter() - t0) * 1000:.2f} ms")
    print(f"P2: {p2(data)}. {(time.perf_counter() - t0) * 1000:.2f} ms")


if __name__ == "__main__":
    main()
