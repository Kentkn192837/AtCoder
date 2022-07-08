import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

MOD = 10 ** 9 + 7
n, a, b = map(int, input().split())
print(combinations_count(4, 2))
