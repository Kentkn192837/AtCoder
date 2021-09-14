def calc(a, b):
    return a / 100 * b

a, b = [int(x) for x in input().rstrip().split(' ')]
print(calc(a, b))
