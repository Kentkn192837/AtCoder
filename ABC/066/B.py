def main():
    s = input()
    s = s[:-1]
    while True:
        if len(s) % 2 == 0:
            left = s[:int(len(s) / 2)]
            right = s[int(len(s) / 2):]
            if left == right:
                break
        s = s[:-1]
    print(len(s))

if __name__ == '__main__':
    main()
