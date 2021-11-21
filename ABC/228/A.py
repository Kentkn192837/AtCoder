def main():
    s, t, x = map(int, input().split())
    times = t - s
    if times > 0:
        print('Yes' if x < t else 'No')
    else:
        print('Yes' if x > s else 'No')

if __name__ == '__main__':
    main()
