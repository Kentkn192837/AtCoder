def main():
    s = input()
    n = len(s) + 1
    ans = [0] * n

    tmp = 1
    ens = list(enumerate(s))
    for i, c in ens:
        if c == '<':
            ans[i + 1] = tmp
            tmp += 1
        else:
            tmp = 1
    
    tmp = 1
    for i, c in reversed(ens):
        if c == '>':
            ans[i] = max(ans[i], tmp)
            tmp += 1
        else:
            tmp = 1
    print(sum(ans))

if __name__ == '__main__':
    main()
