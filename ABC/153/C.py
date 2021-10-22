def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    while h and k > 0:
        h.remove(max(h))
        k -= 1
    print(sum(h))

if __name__ == '__main__':
    main()
