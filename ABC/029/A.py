def main():
    s = list(input())
    ans = 0
    i = 0
    while i < len(s) - 1:
        if s[i] == 'B' and s[i + 1] == 'W':
            s[i], s[i + 1] = s[i + 1], s[i]
            ans += 1
            i = 0
            continue
        i += 1
    print(ans)

if __name__ == '__main__':
    main()
