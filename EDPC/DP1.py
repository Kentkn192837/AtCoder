def main():
    n = [1, 5, 3, -2, -10, 9, 4]
    dp = [0] * (len(n) + 1)
    print(dp)
    for i in range(1, len(n) + 1):
        dp[i] = max(dp[i-1], dp[i-1] + n[i-1])
    print(dp)

if __name__ == '__main__':
    main()
