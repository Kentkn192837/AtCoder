from decimal import Decimal, ROUND_HALF_UP
from collections import Counter, deque

def test(variable, x):
    print('{}: {}'.format(variable, x))

def input_two_array(n):
    a = []
    b = []
    for _ in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    return a, b

# 素因数分解
def prime_factorize(n):
    x = []
    while n % 2 == 0:
        x.append(2)
        n //= 2
    f = 3
    while f*f <= n:
        if n % f == 0:
            x.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        x.append(n)
    return x

# 約数を列挙する関数
def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

# 素数を列挙する関数(エラトステネスの篩)
def prime_sieve(n):
    prime = [ True ] * (n + 1)

    LIMIT = int(n ** 0.5)
    for i in range(2, LIMIT + 1):
        if prime[i] == True:
            for j in range(2 * i, n + 1, i):
                prime[j] = False

    # n 以下の素数を小さい順に出力
    for i in range(2, n + 1):
        if prime[i] == True:
            print(i)

def main():

if __name__ == '__main__':
    main()
