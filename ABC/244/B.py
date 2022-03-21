def main():
    N = int(input())
    T = list(input())

    cnt = 0
    x = 0
    y = 0
    for t in T:
        if t == 'R':
            cnt += 1
        elif t == 'S':
            dirction = cnt % 4
            if dirction == 0: x += 1
            if dirction == 1: y -= 1
            if dirction == 2: x -= 1
            if dirction == 3: y += 1
    print('{} {}'.format(x, y))

if __name__ == '__main__':
    main()
