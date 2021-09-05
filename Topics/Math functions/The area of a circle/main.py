from math import pi, pow


def circle_area(r):
    return pi * pow(r, 2)


radius = int(input())
print(round(circle_area(radius), 2))
