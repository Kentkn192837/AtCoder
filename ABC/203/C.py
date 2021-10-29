from decimal import Decimal, ROUND_HALF_UP
from collections import Counter, deque
from copy import deepcopy

def test_write(x, variable):
    print('{}: {}'.format(variable, x))

def main():
    n, k = map(int, input().split())
    a = []
    b = []
    for _ in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)

    pre_position = 0
    position = 0
    while k > 0:
        position += k
        k = 0
        friends = []
        for i, val in enumerate(a):
            if pre_position <= val and val <= position:
                friends.append(b[i])
        pre_position = position
        k = sum(friends)
    print(position)

if __name__ == '__main__':
    main()
