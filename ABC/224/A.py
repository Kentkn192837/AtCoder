def main():
    s = input()
    if s.find('er', len(s) - 2, len(s)) != -1:
        print('er')
    else:
        print('ist')

if __name__ == '__main__':
    main()
