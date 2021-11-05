def main():
    a, b, c = map(int, input().split())
    if abs(a) == abs(b):
        print('=')
    elif a > 0 and b > 0:
        if a < b:
            print('<')
        else:
            print('>')
    elif a < 0 and b < 0:
        if a < b:
            if c % 2 == 0:
                print('>')
            else:
                print('<')
        elif a > b:
            if c % 2 == 0:
                print('<')
            else:
                print('>')
    elif a < 0 and b > 0:
        if c % 2 == 1:
            print('<')
        else:
            print('>' if abs(a) > abs(b) else '<')
    elif a > 0 and b < 0:
        if c % 2 == 1:
            print('>')
        else:
            print('>' if abs(a) > abs(b) else '<')

if __name__ == '__main__':
    main()
