def main():
    L, R = map(int, input().split())
    S = input()
    cat = S[L-1:R]
    cat = cat[::-1]
    ans = S[:L-1] + cat + S[R:]
    print(ans)

if __name__ == '__main__':
    main()
