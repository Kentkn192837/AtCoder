def main():
    h, w = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    
    dp = [[10 ** 6] * w for _ in range(h)]
    print(*dp, sep='\n')


if __name__ == '__main__':
    main()
