def main():
    a, b, x = map(int, input().split())

    cnt_a = 0
    cnt_b = 0

    if a == 0:
        cnt_a = 0
    else:
        cnt_a = (a - 1) // x + 1
    
    cnt_b = b // x + 1
    print(cnt_b - cnt_a)    

if __name__ == '__main__':
    main()
