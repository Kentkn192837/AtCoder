def main():
    A = list(map(int, input().split()))
    ans = A[0]
    for i in range(2, 0, -1):
        ans = A[ans]
    print(ans)

if __name__ == '__main__':
    main()
