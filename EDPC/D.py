n, W = map(int, input().split())
wv = [list(map(int, input().split())) for i in range(n)]

# dp = [[0] * (W + 1)] * (n + 1)
dp = [[0] * (W + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    w, v = wv[i - 1]
    for j in range(W + 1):
        if w <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
        else:
            dp[i][j] = dp[i - 1][j]
print(max(dp[-1]))
