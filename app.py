import math

import flask
import matplotlib.pyplot as plt


def area1(diagonal, aspect_ratio):
    side1 = diagonal / math.sqrt(aspect_ratio**2 + 1)
    side2 = aspect_ratio * side1
    return side1, side2


def area2(diagonal, pixels1, pixels2):
    return area1(diagonal, pixels1 / pixels2)


def main():
    side1, side2 = area2(31.5, 9, 16)
    print(side1, side2)


if __name__ == "__main__":
    main()
