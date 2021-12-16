import os
import time
from functools import reduce
from typing import List, Callable

import pytest

day = os.path.basename(__file__).split(".")[0]


def parse_literal(package: str, literals: List) -> str:
    literal, cont = [], True
    while cont:
        chunk, package = package[:5], package[5:]
        cont, num = int(chunk[0]), chunk[1:]
        literal.append(num)
    literals.append(int("".join(literal), 2))
    return package


def parse_operator(package: str, literals: List, versions: List) -> str:
    if package[0] == "0":
        length = int(package[1:16], 2)
        sub_packages, package = package[16:16 + length], package[16 + length:]
        while sub_packages:
            sub_packages = parse_package(sub_packages, literals, versions)
    elif package[0] == "1":
        num, package = int(package[1:12], 2), package[12:]
        for _ in range(num):
            package = parse_package(package, literals, versions)
    return package


def expression(type_id: int) -> Callable:
    return {
        0: lambda x: sum(x),
        1: lambda x: reduce(lambda a, b: a * b, x),
        2: lambda x: min(x),
        3: lambda x: max(x),
        4: lambda x: x[0],
        5: lambda x: x[0] > x[1],
        6: lambda x: x[0] < x[1],
        7: lambda x: x[0] == x[1],
    }[type_id]


def parse_package(package: str, literals: List, versions: List) -> str:
    versions.append(int(package[0:3], 2))
    type_id = int(package[3:6], 2)
    sub_literals = []

    package = (
        parse_literal(package[6:], sub_literals)
        if type_id == 4 else
        parse_operator(package[6:], sub_literals, versions)
    )
    literals.append(expression(type_id)(sub_literals))

    return package


def solve(data):
    package, versions, literals = bin(int(f"1{data}", 16))[3:], [], []
    parse_package(package, literals, versions)
    return sum(versions), literals[0]


tc1 = [
    ("D2FE28", 6),
    ("8A004A801A8002F478", 16),
    ("620080001611562C8802118E34", 12),
    ("C0015000016115A2E0802F182340", 23),
    ("A0016C880162017C3686B18A3D4780", 31)
]


@pytest.mark.parametrize("case", tc1, ids=lambda x: x[0])
def test_p1(case):
    assert solve(case[0])[0] == case[1]


tc2 = [
    ("C200B40A82", 3),
    ("04005AC33890", 54),
    ("880086C3E88112", 7),
    ("CE00C43D881120", 9),
    ("D8005AC2A8F0", 1),
    ("F600BC2D8F", 0),
    ("9C005AC2F8F0", 0),
    ("9C0141080250320F1802104A08", 1)
]


@pytest.mark.parametrize("case", tc2, ids=lambda x: x[0])
def test_p2(case):
    assert solve(case[0])[1] == case[1]


def main():
    input_file = f'inputs/{day}.input'

    t0 = time.perf_counter()
    data = open(input_file).read()
    p1, p2 = solve(data)

    print(
        f"P1: {p1}",
        f"P2: {p2}",
        f"Solve time: {(time.perf_counter() - t0) * 1000:.2f} ms"
    )


if __name__ == "__main__":
    main()
