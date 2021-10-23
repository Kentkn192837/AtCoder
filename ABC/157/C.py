def main():
    n, m = map(int, input().split())
    sc = [list(map(int, input().split())) for _ in range(m)]
    
    cand = [0] * n
    comp = []
    cand[sc[0][0] - 1] = sc[0][1]
    comp.append(sc[0][0] - 1)
    for i in range(1, m):
        if sc[i][0] in comp:
            if sc[i][1] != cand[cand.index(sc[i][0] - 1)]:
                print(-1)
                exit()
        cand[sc[i][0] - 1] = sc[i][1]
        comp.append(sc[i][0] - 1)
    cand = list(map(str, cand))
    ans = ''.join(cand)
    ans = str(int(ans))
    print(ans if len(ans) == n else -1)

if __name__ == '__main__':
    main()
