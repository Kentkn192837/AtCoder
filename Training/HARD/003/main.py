def main():
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    dp = [[10 ** 6] * w for _ in range(h)]

    ans = 0
    dp[0][0] = 0 if s[0][0] == '.' else 1

    for i in range(h):
        for j in range(w):

            if i - 1 >= 0:
                # 移動前後でマスの色が変化しない場合
                if s[i - 1][j] == s[i][j]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j])
                # 移動前の色が黒の場合
                elif s[i - 1][j] == '#':
                    dp[i][j] = min(dp[i][j], dp[i - 1][j])
                # 白から黒に移動する場合
                else:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
            
            if j - 1 >= 0:
                if s[i][j - 1] == s[i][j]:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1])
                elif s[i][j - 1] == '#':
                    dp[i][j] = min(dp[i][j], dp[i][j - 1])
                else:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
    
    print(dp[-1][-1])

if __name__ == '__main__':
    main()
