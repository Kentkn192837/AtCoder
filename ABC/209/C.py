MOD = 10 ** 9 + 7

def main():
    n = int(input())    
    c = list(map(int, input().split()))
    c.sort()
    ans = 1
    for i in range(n):
        ans = ans * max(0, c[i] - i) % MOD
    print(ans)

if __name__ == '__main__':
    main()
