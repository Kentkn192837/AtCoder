from math import floor
 
def calc(n, a, x):
    len_a = len(a)
    sum_a = sum(a)
    t = floor(x / sum_a)
    mul = sum_a * t
    times = len_a * t
    if mul > x:
        return times
    i = 0
    while True:
        mul += a[i % len_a]
        if mul > x:
            return times + i + 1
        i += 1
 
def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    x = int(input())
    result = calc(n, a, x)
    print(result)
 
if __name__ == '__main__':
    main()
