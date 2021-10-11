import math

def calc_vmax(goods):
    v = []
    for i in goods:
        v.append(i[1])
    return max(v)

n, W = map(int, input().split())
goods = [list(map(int, input().split())) for i in range(n)]
vmax = calc_vmax(goods)

dp = [[math.inf] * (vmax + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(1, n + 1):
    for j in range(vmax):
        w, v = goods[i - 1]
        if j >= v:
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - v] + w)
        else:
            dp[i][j] = dp[i - 1][j]

ans = 0
for v in range(vmax):
    if dp[n][v] <= W:
        ans = max(ans, v)
print(ans)
