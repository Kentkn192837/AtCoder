def calc(n, a, x, y):
    if n > a:
        discounted = n - a
        return a * x + discounted * y
    else:
        return n * x

n, a, x, y = map(int, input().split())
result = calc(n, a, x, y)
print(result)
