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


def main():
    # 平方数は必ず約数の個数が奇数になることを利用する。
    a, b = input().split()
    num = int(a + b)
    divisors = len(make_divisors(num))
    print("Yes" if divisors % 2 else "No")

if __name__ == '__main__':
    main()
