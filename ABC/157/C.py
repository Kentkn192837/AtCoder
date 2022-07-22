def main():
    n, m = map(int, input().split())
    
    t = [-1] * n
    for _ in range(m):
        s, c = map(int, input().split())
        s -= 1
        if t[s] != -1 and t[s] != c:
            print(-1)
            exit()
        t[s] = c

    if n != 1:
        if t[0] == 0:
            print(-1)
            exit()
        if t[0] == -1:
            t[0] = 1
        for i in range(1, n):
            if t[i] == -1:
                t[i] = 0
    else:
        if t[0] == -1:
            t[0] = 0
    print(''.join(map(str, t)))

if __name__ == '__main__':
    main()
