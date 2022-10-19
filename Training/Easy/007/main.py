def checkbingo(flag):
    # 横がビンゴかどうか
    for i in range(0, 9, 3):
        if flag[i] and flag[i+1] and flag[i+2]:
            return 1

    # 縦がビンゴかどうか
    for i in range(3):
        if flag[i] and flag[i+3] and flag[i+6]:
            return 1

    # 斜めがビンゴかどうか
    if flag[0] and flag[4] and flag[8]:
        return 1
    if flag[2] and flag[4] and flag[6]:
        return 1
    
    return 0


def main():
    bingo = []
    flag = [False] * 9
    for _ in range(3):
        a, b, c = map(int, input().split())
        bingo.append(a)
        bingo.append(b)
        bingo.append(c)

    N = int(input())

    for _ in range(N):
        num = int(input())
        if num not in bingo:
            continue
        flag[bingo.index(num)] = True

    result = checkbingo(flag)
    print("Yes" if result else "No")

if __name__ == '__main__':
    main()
