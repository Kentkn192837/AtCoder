def n_ary(n, k):
    remainder = []
    while True:
        if int(n / k) == 0:
            remainder.append(n % k)
            break
        n = int(n / k)
        remainder.append(n % k)
    remainder = [str(x) for x in remainder]
    return len(''.join(remainder))

n, k = map(int, input().split())
result = n_ary(n, k)
print(result)
