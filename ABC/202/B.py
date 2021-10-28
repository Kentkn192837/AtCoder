def main():
    s = list(input())
    for i, val in enumerate(s):
        if val == '6':
            s[i] = '9'
        elif val == '9':
            s[i] = '6'
    print(''.join(reversed(s)))

if __name__ == '__main__':
    main()
