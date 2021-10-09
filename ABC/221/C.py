n = sorted(list(map(int, list(input()))), reverse=True)
# print(n)

a = n[0:len(n):2]
b = n[1:len(n):2]

for i in range(min(len(a), len(b))):
    if a[i] != b[i]:
        a[i], b[i] = b[i], a[i]
        break

a = int(''.join(list(map(str, a))))
b = int(''.join(list(map(str, b))))
print(a * b)
