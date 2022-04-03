def main():
    A, B = map(int, input().split())
    tap = 1
    cnt = 0
    while tap < B:
        tap -= 1
        tap += A
        cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()
