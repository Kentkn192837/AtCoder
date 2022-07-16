def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]
    print(f'N: {N}')
    print(f'M: {M}')
    print(f'C: {C}')
    print(*B)
    print(A)

if __name__ == '__main__':
    main()
