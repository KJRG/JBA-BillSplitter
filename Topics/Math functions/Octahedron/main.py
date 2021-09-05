from math import sqrt, pow


def octahedron_area(a):
    return 2 * sqrt(3) * pow(a, 2)


def octahedron_volume(a):
    return (1 / 3) * sqrt(2) * pow(a, 3)


edge_length = int(input())
area = octahedron_area(edge_length)
volume = octahedron_volume(edge_length)
print(round(area, 2), round(volume, 2))
