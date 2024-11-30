def main():
    N = int(input())
    S = list(input())

    if N % 2 == 0:
        print("No")
        return

    for i in range(int(N / 2) - 1):
        if S[i] != '1':
            print("No")
            return

    if S[N // 2] != '/':
        print("No")
        return

    for i in range(int(N / 2) + 1, N):
        if S[i] != '2':
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()
