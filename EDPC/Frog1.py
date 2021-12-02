n = int(input())
h = list(map(int, input().split()))
dp = [0]
dp.append(abs(h[1] - h[0]))
for i in range(2, len(h)):
    dp.append( min(abs(h[i] - h[i - 2]) + dp[i - 2], abs(h[i] - h[i - 1]) + dp[i - 1]) )
print(dp[-1])
