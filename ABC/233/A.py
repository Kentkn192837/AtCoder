from math import ceil

def main():
    x, y = map(int, input().split())

    if y <= x:
        print(0)
        exit()
    else:
        ans = ceil((y - x) / 10)
        print(ans)

if __name__ == '__main__':
    main()
