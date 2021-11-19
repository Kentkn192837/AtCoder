def main():
    n = input().zfill(4)
    pre = int(n[:2])
    rea = n[-2:]
    if rea == '00':
        print(pre)
    else:
        print(pre + 1)

if __name__ == '__main__':
    main()
