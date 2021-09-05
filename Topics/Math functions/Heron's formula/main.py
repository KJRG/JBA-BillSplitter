# put your python code here
from math import sqrt


def herons_formula(a, b, c):
    p = (a + b + c) / 2
    p_a = (p - a)
    p_b = (p - b)
    p_c = (p - c)
    return sqrt(p * p_a * p_b * p_c)


input_a = int(input())
input_b = int(input())
input_c = int(input())

print(herons_formula(input_a, input_b, input_c))
