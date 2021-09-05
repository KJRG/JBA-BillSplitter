from math import exp


def sigmoid(x):
    return exp(x) / (exp(x) + 1)


input_x = int(input())
print(round(sigmoid(input_x), 2))
