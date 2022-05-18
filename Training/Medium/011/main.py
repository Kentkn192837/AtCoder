def input_two_array(n):
    a = []
    b = []
    for _ in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    return a, b

def l1_distance(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def main():
    N, M = map(int, input().split())
    a, b = input_two_array(N)       # 学生の座標
    c, d = input_two_array(M)       # チェックポイントの座標 

    for i in range(N):
        candidate = []
        for j in range(M):
            candidate.append(l1_distance(a[i], c[j], b[i], d[j]))
        print(candidate.index(min(candidate)) + 1)

if __name__ == '__main__':
    main()
