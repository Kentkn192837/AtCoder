def main():
    A, B, C = map(int, input().split())

    flag = False

    for i in range(1, B + 1):
        if (A * i) % B == C:
            flag = True
            break
    
    if flag:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
