from collections import Counter

def main():
    n = int(input())
    s = [input() for _ in range(n)]

    c = Counter(s)
    val_max = max(c.values())
    ans = sorted(list(set([i for i in s if c[i] == val_max])))
    print(*ans, sep='\n')

if __name__ == '__main__':
    main()
