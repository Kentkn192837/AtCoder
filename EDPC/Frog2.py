def dp(h, k):
    dp = [0]
    dp.append(abs(h[1] - h[0]))
    for i in range(2, len(h)):
        cand = []
        for j in range(k, 0, -1):
            if i - j >= 0:
                cand.append(abs(h[i] - h[i - j]) + dp[i - j])
        dp.append(min(cand))
    return dp

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    ans = dp(h, k)
    print(ans[-1])

if __name__ == '__main__':
    main()
