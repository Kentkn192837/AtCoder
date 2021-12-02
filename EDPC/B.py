"""
問題URL:https://atcoder.jp/contests/dp/tasks/dp_b
DP法練習
"""

def chmin(h, k):
    pass

def DP_search(h, k):
    dp = [0]
    dp.append(abs(h[1] - h[0]))
    for i in range(2, k):
        select_min = []
        for j in range(i, 1, -1):
            select_min.append(abs(h[i] - h[i - j]) + dp[i - j])
        dp.append(min(select_min))
    print(dp)

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    nodes = DP_search(h, k)
    # print(nodes[-1])

if __name__ == '__main__':
    main()
