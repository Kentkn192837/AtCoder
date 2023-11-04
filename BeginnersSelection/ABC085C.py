def count_bill(n, y):
    ten_thousand = int(y / 10000)
    five_thousand = int(y / 5000)
    thousand = int(y / 1000)
    choices = []
    for i in range(ten_thousand + 1):
        for j in range(five_thousand + 1):
            for k in range(thousand + 1):
                if 10000 * i + 5000 * j + 1000 * k == y and i + j + k == n:
                    choices.append([i, j, k])
    return choices

def judge(ans):
    if ans:
        print(*ans[0], sep=' ')
        return
    print(-1, -1, -1)

if __name__ == '__main__':
    n, y = map(int, input().split())
    ans = count_bill(n, y)
    judge(ans)
