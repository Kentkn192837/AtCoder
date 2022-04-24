def main():
    N = int(input())
    a = list(map(int, input().split()))

    cnt = [0] * (10 ** 5 + 2)
    for elm in a:
        cnt[elm] += 1
        cnt[elm + 1] += 1
        cnt[elm + 2] += 1
    
    print(max(cnt))

if __name__ == '__main__':
    main()
