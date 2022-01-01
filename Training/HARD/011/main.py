from collections import Counter

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

def main():
    A, B = map(int, input().split())

    # 素因数分解を行う
    a = prime_factorize(A)
    b = prime_factorize(B)

    a = list(set(a))
    b = list(set(b))
    ab = a + b

    # 出現回数が2回のものを取り出す
    C = Counter(ab)
    div = [c[0] for c in C.items() if c[1] == 2]

    # 1も正の公約数なので追加する
    div.insert(0, 1)
    ans = len(div)
    print(ans)

if __name__ == '__main__':
    main()
