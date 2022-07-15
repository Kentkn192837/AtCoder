from math import ceil, floor

def main():
    N = int(input())
    X_ceil = ceil(N / 1.08)
    X_floor = floor(N / 1.08)
    # print(f'N: {N}')
    # print(f'X_ceil: {X_ceil}')
    # print(f'X_floor: {X_floor}')

    ans1 = int(X_ceil * 1.08)
    ans2 = int(X_floor * 1.08)
    # print(f'ans1: {ans1}')
    # print(f'ans2: {ans2}')

    if N == ans1:
        print(X_ceil)
        exit()
    if N == ans2:
        print(X_floor)
        exit()
    print(":(")

if __name__ == '__main__':
    main()
