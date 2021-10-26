def main():
    s = input()
    ans = 0
    for i in range(10000):
        flag = [False] * 10
        now = i
        for j in range(4):
            flag[now % 10] = True
            now //= 10
        flag2 = True
        for j in range(10):
            if s[j] == 'o' and not flag[j]:
                flag2 = False
            if s[j] == 'x' and flag[j]:
                flag2 = False
        ans += flag2
    print(ans)

if __name__ == '__main__':
    main()
