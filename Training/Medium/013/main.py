def main():
    N = int(input())
    for _ in range(N):
        t, x, y = map(int, input().split())
        if (t % 2) != ((x + y) % 2):
            print("No")
            return
        if t < (x + y):
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()
