def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    cnt = 0

    for _ in range(N):
        A = list(map(int, input().split()))
        result = C
        for a, b in zip(A, B):
            result += a * b
        if result <= 0:
            continue
        cnt += 1

    print(cnt)

if __name__ == '__main__':
    main()
