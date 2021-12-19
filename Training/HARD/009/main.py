def main():
    n, m = map(int, input().split())
    a = [input() for _ in range(n)]
    b = [input() for _ in range(m)]

    for di in range(n - m + 1):
        for dj in range(n - m + 1):
            for i in range(m):
                for j in range(m):
                    if a[i + di][j + dj] != b[i][j]:
                        break
                else:
                    continue
                break
            else:
                print('Yes')
                exit()

    print('No')
if __name__ == '__main__':
    main()
