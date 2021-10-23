def main():
    n = int(input())
    s = list(input())
    q = int(input())
    for i in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            a -= 1
            b -= 1
            s[a], s[b] = s[b], s[a]
        elif t == 2:
            part_a = s[:n]
            part_b = s[n:2*n]
            s = part_b + part_a
    print(''.join(s))

if __name__ == '__main__':
    main()
