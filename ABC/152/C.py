def main():
    n = int(input())
    p = list(map(int, input().split()))

    i_count = 0
    minimum = p[0]
    for i in p:
        if i <= minimum:
            i_count += 1
        minimum = min(minimum, i)
    print(i_count)

if __name__ == '__main__':
    main()
