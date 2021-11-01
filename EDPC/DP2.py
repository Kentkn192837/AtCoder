"""
value(価値)を求めたいのでDPテーブル内で計算する値はvalueにする。
weightはDP
"""

def main():
    n = 6
    weight_limit = 9
    wv = [[2,3],[1,2],[3,6],[2,1],[1,3],[5,85]]
    dp = [[0] * (weight_limit + 1) for _ in range(n + 1)]
    print(*dp, sep='\n')
    print("-----------")

    for i in range(n + 1):
        for w in range(weight_limit + 1):
            if w >= wv[i-1][0]:
                dp[i][w] = max(dp[i-1][w - wv[i-1][0]] + wv[i-1][1], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    print(*dp, sep='\n')


if __name__ == '__main__':
    main()
