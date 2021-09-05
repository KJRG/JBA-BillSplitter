from math import log


def calculate_result(x, base):
    if base <= 1:
        return log(x)
    return log(x, base)


input_x = int(input())
input_base = int(input())
print(round(calculate_result(input_x, input_base), 2))
