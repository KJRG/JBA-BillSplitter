import math

degrees = int(input())
radians = math.radians(degrees)
cotangent = math.cos(radians) / math.sin(radians)
print(round(cotangent, 10))
