def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    a.insert(0, 0)
    i = 1
    ans = 1
    for _ in range(100010):
        if a[i] == 2:
            print(ans)
            exit()
        i = a[i]
        ans += 1
    print(-1)

if __name__ == '__main__':
    main()
