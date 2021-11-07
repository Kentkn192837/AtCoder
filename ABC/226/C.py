def training(menus, time, t, k, a):
    for menu in menus:
        if a[menu - 1] != []:
            time = training(a[menu - 1], time, t, k, a)
        time += t[menu - 1]
    return time

def main():
    n = int(input())
    t = []
    k = []
    a = []
    time = 0
    for _ in range(n):
        line = list(map(int, input().split()))
        t.append(line.pop(0))
        k.append(line.pop(0))
        a.append(line)
    time = training(a[-1], time, t, k, a)
    time += t[-1]
    print(time)

if __name__ == '__main__':
    main()
