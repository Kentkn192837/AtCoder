from itertools import combinations

def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    cand = list(combinations(xy, 3))
    cnt = 0
    for i in cand:
        x, y, z = i
        if (y[0] - x[0] == 0) and (z[0] - x[0] == 0):
            continue
        if (y[0] - x[0] != 0) and (z[0] - x[0] != 0):
            t_1 = (y[1] - x[1]) / (y[0] - x[0])
            t_2 = (z[1] - x[1]) / (z[0] - x[0])
            if t_1 == t_2:
                continue
        cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()
