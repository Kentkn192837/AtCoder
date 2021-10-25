import math
from collections import Counter

def combinations_count(n):
    return math.factorial(n) // (math.factorial(n - 2) * math.factorial(2))

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_mod = list(map(lambda x: x % 200, a))
    combinations = []
    counter = Counter(a_mod)
    values = [i for i in counter.values() if i > 1]
    for i in values:
        combinations.append(combinations_count(i))
    print(sum(combinations))

if __name__ == '__main__':
    main()
