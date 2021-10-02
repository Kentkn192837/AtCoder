import math

n = int(input())
x = [int(x) for x in input().split()]
p = math.floor(sum(x) / len(x))
squares = list(map(lambda x: (x - p) ** 2, x))
cand_1 = sum(squares)

p = math.ceil(sum(x) / len(x))
squares = list(map(lambda x: (x - p) ** 2, x))
cand_2 = sum(squares)
print(min(cand_1, cand_2))
