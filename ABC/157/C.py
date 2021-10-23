def main():
    n, m = map(int, input().split())
    sc = [list(map(int, input().split())) for _ in range(m)]

    cand = []
    for i in range(1000):
        num = len(str(i))
        if num != n:
            continue
        else:
            for j in sc:
                s, c = j:
                if num[s - 1] != c:
                    continue
            cand.append(int(num))
    print(min(cand) if cand else -1)

if __name__ == '__main__':
    main()
