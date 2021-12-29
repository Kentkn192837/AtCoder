def main():
    n = int(input())

    if n % 2 == 1:
        print(0)
        exit()
    
    ans = 0
    for i in range(1, n):
        # 5が出現する数を数える。ただし、numがnを超える場合を考慮する
        num = 2 * (5 ** i)
        if num > n:
            break
        ans += n // num
    
    print(ans)

if __name__ == '__main__':
    main()
