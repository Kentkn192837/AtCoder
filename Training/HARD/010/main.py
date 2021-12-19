def two_pointer_tec(a, n, k):
    tmp = 0
    cur = 0
    ans = 0
    for i in range(n):
        if cur < n:
            while tmp < k:
                tmp += a[cur]
                cur += 1
                if cur == n:
                    break
        if tmp < k:
            break
        ans += n-1 - (cur - 1) + 1
        tmp -= a[i]
    return ans

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = two_pointer_tec(a, n, k)
    print(ans)

if __name__ == '__main__':
    main()
