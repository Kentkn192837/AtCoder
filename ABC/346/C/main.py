def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = sorted(set(A))
    max_value = K if max(A) > K else max(A)
    print(max_value)

if __name__ == '__main__':
    main()
