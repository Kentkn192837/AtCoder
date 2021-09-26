from math import ceil
 
def calc(n, a, x):
    len_a = len(a)
    sum_a = sum(a)
    t = ceil(x / sum_a)
    mul = sum_a * t
    i = 0
    while True:
        if (mul - a[-(i + 1)]) < x:
            return t * len_a - i
        mul -= a[-(i + 1)]
        i += 1
 
def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    x = int(input())
    result = calc(n, a, x)
    print(result)
 
if __name__ == '__main__':
    main()
