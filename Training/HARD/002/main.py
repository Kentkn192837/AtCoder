MOD = 10 ** 9 + 7

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    ans1 = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                ans1 += 1
    ans1 *= k
    ans2 = 0
    for i in range(n):
        for j in range(n):
            if a[i] > a[j]:
                ans2 += 1
    ans2 *= k * (k - 1) // 2
    ans = ans1 + ans2
    print(ans % MOD)

if __name__ == '__main__':
    main()
