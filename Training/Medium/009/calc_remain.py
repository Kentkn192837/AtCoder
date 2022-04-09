def main():
    a = int(input('a:'))
    b = int(input('b:'))

    for i in range(1, 20):
        print(a * i, "%", b, "=", a * i % b)

if __name__ == '__main__':
    main()
