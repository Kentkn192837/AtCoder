def main():
    N, A, B = map(int, input().split())
    S = list(input())

    cnt_b = 0   # 数えた海外の学生の人数
    ok = 0      # 合格者数

    for s in S:
        if s == 'c':
            print("No")
            continue

        if s == 'a':
            if A + B > ok:
                ok += 1
                print("Yes")
                continue
            else:
                print("No")
                continue
        
        if s == 'b':
            cnt_b += 1
            if A + B > ok and cnt_b <= B:
                ok += 1
                print("Yes")
                continue
            else:
                print("No")
                continue

if __name__ == '__main__':
    main()
