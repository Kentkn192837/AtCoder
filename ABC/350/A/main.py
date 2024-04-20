def main():
    S = input()
    end = int(S[-3:])
    if end >= 350:
        print("No")
        return

    if end == 316 or 0:
        print("No")
        return

    if end == 0:
        print("No")
        return

    print("Yes")

if __name__ == '__main__':
    main()
