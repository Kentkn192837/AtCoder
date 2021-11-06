def main():
    n = int(int(input()) * 1.08)
    price = 206
    if n < price:
        print('Yay!')
    elif n == price:
        print('so-so')
    else:
        print(':(')

if __name__ == '__main__':
    main()
