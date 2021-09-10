N = int(input())
k = 1
while N >= 1:
    if N / 2 > 1:
        N /= 2 ** k
        k += 1
    else:
        break
print(N)
