def main():
    a, b, c = map(int, input().split())
    result = sorted([a, b, c])
    print("Yes") if b == result[1] else print("No")

if __name__ == '__main__':
    main()
