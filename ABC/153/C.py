def main():
    n, k = map(int, input().split())
    h = sorted(list(map(int, input().split())), reverse=True)
    
    ans = 0
    for i in range(n):
        if k > 0:
            h[i] = 0
            k -= 1
        ans += h[i]
    print(ans)

if __name__ == '__main__':
    main()
