def n_ary(n, k):
    s = ''
    while n >= k:
        s += str(n % k)
        n = n // k
    s += str(n)
    return len(s[::-1])

n, k = map(int, input().split())
result = n_ary(n, k)
print(result)
