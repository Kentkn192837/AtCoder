def calc(n, a, b):
    ans = 0
    for i in range(1, n + 1):
        trans = sum(map(int, list(str(i))))
        if trans >= a and trans <= b:
            ans += i
    return ans

n, a, b = map(int, input().split())
ans = calc(n, a, b)
print(ans)
