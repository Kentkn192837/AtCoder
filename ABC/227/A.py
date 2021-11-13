def main():
    n, k, a = map(int, input().split())
    ans = (a + (k - 1)) % n
    print(n if ans == 0 else ans)

if __name__ == '__main__':
    main()
