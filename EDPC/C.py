n = int(input())
todo_list = [list(map(int, input().split())) for _ in range(n)]
dp = [todo_list[0]]
for i in range(1, n):
    dp.append([0] * 3)
    dp[i][0] = max(dp[i - 1][1], dp[i - 1][2]) + todo_list[i][0]
    dp[i][1] = max(dp[i - 1][2], dp[i - 1][0]) + todo_list[i][1]
    dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + todo_list[i][2]
print(max(dp[-1]))
