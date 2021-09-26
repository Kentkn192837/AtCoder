a, b, c = map(int, input().split())
x = 1

while True:
    mul = x * c
    if mul < a:
        x += 1
        continue
    if mul > b:
        print(-1)
        break
    if a <= mul and mul <= b:
        print(mul)
        break
