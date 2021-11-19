def main():
    a, b = map(int, input().split())
    for c in range(256):
        if a ^ c == b:
            print(c)
            exit()

if __name__ == '__main__':
    main()
