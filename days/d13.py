import os
import re
import time
from io import StringIO

import numpy as np
import pytesseract
import pytest
from PIL import Image

day = os.path.basename(__file__).split(".")[0]


def parse(file: str):
    x_y, folds = open(file).read().split("\n\n")
    coords = np.genfromtxt(StringIO(x_y), delimiter=",", dtype=np.int64)
    folds = [(int(item[1]), 0) if item[0] == "x" else (0, int(item[1])) for item in re.findall(r"([xy])=(\d+)", folds)]
    paper = np.zeros((coords[:, 0].max() + 1, coords[:, 1].max() + 1))
    for x, y in coords:
        paper[x, y] = 1
    return paper, folds


def p1(paper, folds):
    x, y = folds[0]
    overlap = np.flip(paper[x + 1:, :], 0) if x else np.flip(paper[:, y+1:], 1)
    paper = paper[0:x, :] if x else paper[:, 0:y]
    paper += overlap
    return np.count_nonzero(paper)


def get_string(paper):
    padded = np.flip(np.rot90(np.pad(paper, pad_width=1, mode='constant', constant_values=0)), 0)
    padded[padded == 0] = 255
    img = Image.fromarray(padded).convert("1")
    return pytesseract.image_to_string(img, lang='eng', config='--psm 10 --oem 3').strip()


def p2(paper, folds):
    for fold in folds:
        x, y = fold
        overlap = np.flip(paper[x + 1:, :], 0) if x else np.flip(paper[:, y + 1:], 1)
        paper = paper[0:x, :] if x else paper[:, 0:y]
        paper += overlap
    return get_string(paper)


@pytest.fixture
def test_data():
    return parse(f"inputs/{day}.input.test")


def test_p1(test_data):
    paper, folds = test_data
    assert p1(paper, folds) == 17


def test_p2(test_data):
    paper, folds = test_data
    assert p2(paper, folds) == "O"


def main():
    input_file = f'inputs/{day}.input'

    t0 = time.perf_counter()
    paper, folds = parse(input_file)
    print(
        f"P1: "
        f"{p1(paper, folds)} "
        f"{(time.perf_counter() - t0) * 1000:.2f} ms"
    )

    t0 = time.perf_counter()
    paper, folds = parse(input_file)
    print(
        f"P2: "
        f"{p2(paper, folds)} "
        f"{(time.perf_counter() - t0) * 1000:.2f} ms"
    )


if __name__ == "__main__":
    main()
